// 创建合成
function createComposition(data) {
    var comp = app.project.items.addComp(
        data.name,
        data.res_x,
        data.res_y,
        data.pixelAspect || 1,
        data.duration,
        data.fps
    );

    // 设置工作区域的起始和结束时间
    // Houdini 第一帧是 time 0，所以需要 (frame - 1) / fps
    var startTime = (data.f_start - 1) / data.fps;
    var endTime = (data.f_end - 1) / data.fps;
    comp.workAreaStart = startTime;
    comp.workAreaDuration = endTime - startTime + (1 / data.fps);

    // 先取消所有项目的选中状态
    for (var i = 1; i <= app.project.numItems; i++) {
        app.project.item(i).selected = false;
    }

    // 选中并在查看器中打开合成
    comp.selected = true;
    comp.openInViewer();

    return comp;
}

function createCamera(comp, parms){
    // 检查分辨率和帧率是否匹配
    var warnings = [];

    // 检查分辨率
    if (parms.res_x && parms.res_y) {
        if (parms.res_x !== comp.width || parms.res_y !== comp.height) {
            warnings.push(
                "Houdini Resolution: " + parms.res_x + "x" + parms.res_y +
                "\nAE Comp Resolution: " + comp.width + "x" + comp.height
            );
        }
    }

    // 检查帧率
    if (parms.fps && parms.fps !== comp.frameRate) {
        warnings.push(
            "Houdini FPS: " + parms.fps +
            "\nAE Comp FPS: " + comp.frameRate
        );
    }

    // 弹出警告
    if (warnings.length > 0) {
        var message = "Camera [" + parms.name + "] Parameter Mismatch:\n\n";
        message += warnings.join("\n\n");
        message += "\n\nContinue to import?";
        if (!confirm(message)) {
            return null;  // User cancelled
        }
    }

    var cam = comp.layers.addCamera(parms.name,[0,0]);

    cam.name = parms.name;
    cam.startTime = 0;

    // 禁止自动朝向
    cam.autoOrient = AutoOrientType.NO_AUTO_ORIENT;

    // Position
    setPropertyAnimation(cam.property("Position"), parms.position);

    // Orientation
    setPropertyAnimation(cam.property("Orientation"), parms.orient);

    // POI = Position (模拟 One Node)
    // cam.property("Point of Interest").setValue(
    //     cam.property("Position").value
    // );

    // Zoom
    
    var zoomData = convertFovToZoom(parms.fov, comp.width);
    setPropertyAnimation(cam.property("Zoom"), zoomData);

    return cam;
}

// 将 FOV 转换为 Zoom
// Zoom = (Comp Width / 2) / tan(FOV / 2)
function convertFovToZoom(fovData, compWidth) {
    if (!fovData) return null;

    // 先检查是否是动画数据对象（包含 times 和 values）
    if (fovData.times && fovData.values) {
        var times = fovData.times;
        var values = fovData.values;
        var zoomValues = [];

        for (var i = 0; i < values.length; i++) {
            var fov = values[i];
            var zoom = (compWidth / 2) / Math.tan(fov * Math.PI / 180 / 2);
            zoomValues.push(zoom);
        }

        return { times: times, values: zoomValues };
    }

    // 如果是静态单值（数字）
    if (typeof fovData === "number") {
        var fov = fovData;
        var zoom = (compWidth / 2) / Math.tan(fov * Math.PI / 180 / 2);
        return zoom;
    }

    return null;
}

// 创建纯色
function createSolid(comp,parms) {
    var solid = comp.layers.addSolid(
        parms.color,
        parms.name,
        parms.width,
        parms.height,
        parms.pixelAspect,
        parms.duration
    );
    solid.moveToEnd(); // 移动到底层
    solid.startTime = 0;
    solid.threeDLayer = true; // 启用3D图层
    setPropertyAnimation(solid.property("Position"), parms.position);
    setPropertyAnimation(solid.property("Orientation"), parms.orient);
    return solid;
}

// 创建 Null
function createNull(comp, parms) {
    var nullLayer = comp.layers.addNull(parms.duration);
    nullLayer.name = parms.name;
    nullLayer.moveToEnd(); // 移动到底层
    nullLayer.startTime = 0;
    nullLayer.threeDLayer = true; // 启用3D图层
    setPropertyAnimation(nullLayer.property("Position"), parms.position);
    setPropertyAnimation(nullLayer.property("Orientation"), parms.orient);
    return nullLayer;
}

// 创建灯光
function createLight(comp, parms) {
    // 获取第一个位置值用于创建灯光
    var firstPos = getFirstPositionValue(parms.position);
    var light = comp.layers.addLight(parms.name, firstPos);
    light.moveToEnd();
    light.startTime = 0;

    // 根据灯光类型确定 AE LightType
    var lightType;
    if (parms.light_type === "SPOT") {
        lightType = LightType.SPOT;
    } else if (parms.light_type === "PAR") {
        lightType = LightType.PARALLEL;
    } else {
        // 默认 OMNI
        lightType = LightType.POINT;
    }

    // 直接设置灯光类型
    light.lightType = lightType;

    // 设置强度 (AE 强度范围是 0-100)
    if (parms.intensity !== undefined) {
        try {
            light.property("Intensity").setValue(parms.intensity * 100);
        } catch (e) {}
    }

    // 设置颜色
    if (parms.color) {
        try {
            light.property("Color").setValue(parms.color);
        } catch (e) {}
    }

    // 设置锥角（仅 SPOT）
    if (parms.light_type === "SPOT" && parms.cone_angle !== undefined) {
        try {
            light.property("Cone Angle").setValue(parms.cone_angle);
        } catch (e) {}
    }

    // 设置 Point of Interest（仅 SPOT 和 PAR）
    if (parms.light_type !== "OMNI" && parms.interest_pos) {
        try {
            setPropertyAnimation(light.property("Point of Interest"), parms.interest_pos);
        } catch (e) {}
    }

    // 设置位置
    setPropertyAnimation(light.property("Position"), parms.position);

    return light;
}

// 获取 position 的第一个值（用于创建灯光层时的初始位置）
// addLight 只需要 2D 位置 [x, y]
function getFirstPositionValue(positionData) {
    var pos;
    if (typeof positionData === "number") {
        pos = [0, 0, 0];
    } else if (positionData instanceof Array) {
        pos = positionData;
    } else if (positionData.values && positionData.values.length > 0) {
        pos = positionData.values[0];
    } else {
        pos = [0, 0, 0];
    }
    // 返回前两个元素 [x, y]
    return [pos[0], pos[1]];
}

// 设置属性动画（支持静态值和关键帧）
// valueData 可以是:
//   - 静态单值: number (用于 Zoom 等 1D 属性)
//   - 静态数组: [x, y, z] (用于 Position/Orientation 等 3D 属性)
//   - 动画对象: {times: [0,1,2], values: [val1,val2,...]}
function setPropertyAnimation(property, valueData) {
    if (!valueData) return;

    // 检查属性是否可用
    if (!property || !property.canSetExpression) {
        return;
    }

    // 检查是否是动画数据（有 times 和 values 字段）
    if (typeof valueData === "object" && valueData.times && valueData.values) {
        var times = valueData.times;
        var values = valueData.values;

        if (times.length !== values.length) {
            alert("Error: times and values length mismatch for " + property.name);
            return;
        }

        // 清除现有关键帧
        property.expression = "";
        if (property.numKeys > 0) {
            for (var i = property.numKeys; i >= 1; i--) {
                property.removeKey(i);
            }
        }

        // 添加关键帧
        for (var i = 0; i < times.length; i++) {
            property.setValueAtTime(times[i], values[i]);
        }
    } else if (valueData instanceof Array) {
        // 静态数组值 (使用 instanceof Array 代替 Array.isArray 以兼容旧版 AE)
        property.setValue(valueData);
    } else if (typeof valueData === "number") {
        // 静态单值 (用于 Zoom 等 1D 属性)
        property.setValue(valueData);
    }
}

// 创建遮罩
function createMask(solid,points){
    var shape = new Shape();
    for (var i = 0; i < points.length; i++) {
        points[i][0] = points[i][0];
        points[i][1] = points[i][1];
    }
    shape.vertices = points;

    var numPoints = shape.vertices.length;
    shape.inTangents = [];
    shape.outTangents = [];
    for (var i = 0; i < numPoints; i++) {
        shape.inTangents.push([0, 0]);
        shape.outTangents.push([0, 0]);
    }

    shape.closed = true;
    var mask = solid.Masks.addProperty("ADBE Mask Atom");
    mask.maskShape.setValue(shape);
}

// 导入预览序列到当前激活合成的最底层
function importPreviewSequence(previewData) {
    try {
        var comp = app.project.activeItem;
        if (!comp || !(comp instanceof CompItem)) {
            alert("Please select a composition first!");
            return null;
        }

        var sequencePath = previewData.sequence_path;

        // 导入文件序列
        var importOpts = new ImportOptions(File(sequencePath));
        importOpts.sequence = true;
        importOpts.forceAlphabetical = true;
        var footageItem = app.project.importFile(importOpts);

        if (footageItem) {
            // 将序列添加到合成
            var layer = comp.layers.add(footageItem);
            layer.name = "Preview_Sequence";

            // 移动到最底层
            layer.moveToEnd();

            return layer;
        }
    } catch (err) {
        alert("Import preview failed: " + err.toString());
    }
    return null;
}

app.beginUndoGroup("snail_toae");

// 活动合成
var activeComp = null;

// var jsonFile = File.openDialog("选择包含 points 的 JSON 文件", "*.json");
// var jsonFile = new File("C:/Users/72312/Desktop/toAe/data.json")
// 得到当前路径 + "data.json"
var scriptFile = File($.fileName);
var current_path = scriptFile.parent.fsName;
var jsonFile = new File(current_path + "/data.json");

if (jsonFile != null) {
    jsonFile.open("r");
    var jsonString = jsonFile.read();
    jsonFile.close();

    var jsonIsValid = true;
    try {
        if (typeof JSON !== "undefined" && JSON.parse) {
            jsonData = JSON.parse(jsonString);
        } else {
            jsonData = eval("(" + jsonString + ")");
        }
        // var jsonData = eval("(" + jsonString + ")");
        // var jsonData = JSON.parse(jsonString); # 我mklink之后JSON没有对象
        if (!jsonData) {
            alert("No valid data in JSON file");
            jsonIsValid = false;
        }
    } catch (err) {
        alert("JSON parse failed: " + err.toString());
        jsonIsValid = false;
    }

    if (jsonIsValid) {
        // 检查是否是纯预览数据（只有 __preview__）
        var isPreviewOnly = Object.keys(jsonData).length === 1 && jsonData["__preview__"] && jsonData["__preview__"].type === "preview";

        if (isPreviewOnly) {
            // 纯预览模式：直接导入序列到当前激活合成的最底层
            importPreviewSequence(jsonData["__preview__"]);
        } else {
            // 正常模式：处理合成数据、对象数据
            var hasComposition = false;
            for (var key in jsonData) {
                if (jsonData[key].type === "comp") {
                    hasComposition = true;
                    break;
                }
            }

            // 如果没有合成数据，使用当前选中的合成
            if (!hasComposition) {
                var currentComp = app.project.activeItem;
                if (currentComp && currentComp instanceof CompItem) {
                    activeComp = currentComp;
                } else {
                    alert("Please select a composition first!");
                }
            }

            if (activeComp || hasComposition) {
                for (var key in jsonData) {
                    oneData = jsonData[key];

                    // 处理合成类型
                    if (oneData.type === "comp") {
                        activeComp = createComposition(oneData);
                        continue;
                    }

                    // 确保有活动合成
                    if (!activeComp) {
                        continue;
                    }

                    oneData.pixelAspect = activeComp.pixelAspect;
                    oneData.duration = activeComp.duration;

                    // 根据 type 判断图层类型
                    if (oneData.type === "obj_cam") {
                        var layer = createCamera(activeComp, oneData);
                        if (layer === null) {
                            continue;
                        }
                    } else if (oneData.type === "obj_light") {
                        var layer = createLight(activeComp, oneData);
                    } else if (oneData.width === undefined) {
                        var layer = createNull(activeComp, oneData);
                    } else {
                        var layer = createSolid(activeComp, oneData);
                        if (oneData.mask && oneData.mask.length) {
                            createMask(layer, oneData.mask);
                        }
                    }
                }
            }
        }
    }
}

app.endUndoGroup();

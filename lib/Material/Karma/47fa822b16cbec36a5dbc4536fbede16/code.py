# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/stage/materiallibrary1")

# Code for /stage/materiallibrary1/random_uv
hou_node = hou_parent.createNode("subnet", "random_uv", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-8.47932, -0.19562))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(True)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("folder1", "Karma Material Builder", folder_type=hou.folderType.Collapsible, default_value=0, ends_tab_group=False)
hou_parm_template.setTags({"group_type": "collapsible", "sidefx::shader_isparm": "0"})
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("inherit_ctrl", "Inherit from Class", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Never","Always","Material Flag"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("shader_referencetype", "Class Arc", 1, default_value=(["n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r"]), default_expression=(["n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r"]), default_expression_language=([hou.scriptLanguage.Python]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["none","reference","inherit","specialize","represent"]), menu_labels=(["None","Reference","Inherit","Specialize","Represent"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"sidefx::shader_isparm": "0", "spare_category": "Shader"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("shader_baseprimpath", "Class Prim Path", 1, default_value=(["/__class_mtl__/`$OS`"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"script_action": "import loputils\nloputils.selectPrimsInParm(kwargs, False)", "script_action_help": "Select a primitive in the Scene Viewer or Scene Graph Tree pane.\nCtrl-click to select using the primitive picker dialog.", "script_action_icon": "BUTTONS_reselect", "sidefx::shader_isparm": "0", "sidefx::usdpathtype": "prim", "spare_category": "Shader"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.SeparatorParmTemplate("separator1")
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("tabmenumask", "Tab Menu Mask", 1, default_value=(["karma USD ^mtlxramp* ^hmtlxramp* ^hmtlxcubicramp* MaterialX parameter constant collect null genericshader subnet subnetconnector suboutput subinput"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"spare_category": "Tab Menu"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("shader_rendercontextname", "Render Context Name", 1, default_value=(["kma"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"sidefx::shader_isparm": "0", "spare_category": "Shader"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("shader_forcechildren", "Force Translation of Children", default_value=True)
hou_parm_template2.setTags({"sidefx::shader_isparm": "0", "spare_category": "Shader"})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /stage/materiallibrary1/random_uv/shader_referencetype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv")
hou_parm = hou_node.parm("shader_referencetype")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.StringKeyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r", hou.exprLanguage.Python)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.StringKeyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r", hou.exprLanguage.Python)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.StringKeyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r", hou.exprLanguage.Python)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.StringKeyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r", hou.exprLanguage.Python)
hou_parm.setKeyframe(hou_keyframe)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.0.547")
# Update the parent node.
hou_parent = hou_node

# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/stage/materiallibrary1/random_uv")

# Code for /stage/materiallibrary1/random_uv/__netbox1
hou_netbox = hou_parent.createNetworkBox("__netbox1")
hou_netbox.setPosition(hou.Vector2(-29.2458, -1.34428))
hou_netbox.setSize(hou.Vector2(9.26421, 1.13))
hou_netbox.setMinimized(False)
hou_netbox.setSelected(False)
hou_netbox.setAutoFit(False)
hou_netbox.setComment("添加uv噪波")
hou_netbox.setColor(hou.Color([0.52, 0.52, 0.52]))

# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/stage/materiallibrary1/random_uv")

# Code for /stage/materiallibrary1/random_uv/__netbox2
hou_netbox = hou_parent.createNetworkBox("__netbox2")
hou_netbox.setPosition(hou.Vector2(-22.9656, 1.80543))
hou_netbox.setSize(hou.Vector2(13.3648, 3.9999))
hou_netbox.setMinimized(False)
hou_netbox.setSelected(False)
hou_netbox.setAutoFit(False)
hou_netbox.setComment("中心旋转")
hou_netbox.setColor(hou.Color([0.52, 0.52, 0.52]))

# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/stage/materiallibrary1/random_uv")

# Code for /stage/materiallibrary1/random_uv/__netbox3
hou_netbox = hou_parent.createNetworkBox("__netbox3")
hou_netbox.setPosition(hou.Vector2(-15.6435, -2.58357))
hou_netbox.setSize(hou.Vector2(4.907, 2.95028))
hou_netbox.setMinimized(False)
hou_netbox.setSelected(False)
hou_netbox.setAutoFit(False)
hou_netbox.setComment("随机缩放")
hou_netbox.setColor(hou.Color([0.52, 0.52, 0.52]))

# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/stage/materiallibrary1/random_uv")

# Code for /stage/materiallibrary1/random_uv/__netbox4
hou_netbox = hou_parent.createNetworkBox("__netbox4")
hou_netbox.setPosition(hou.Vector2(-38.7881, -3.2974))
hou_netbox.setSize(hou.Vector2(8.63108, 1.455))
hou_netbox.setMinimized(False)
hou_netbox.setSelected(False)
hou_netbox.setAutoFit(False)
hou_netbox.setComment("噪波边界")
hou_netbox.setColor(hou.Color([0.52, 0.52, 0.52]))

# Code for /stage/materiallibrary1/random_uv/mtlxstandard_surface
hou_node = hou_parent.createNode("mtlxstandard_surface", "mtlxstandard_surface", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-3.91416, 0.0376))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxstandard_surface/folder0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxstandard_surface")
hou_parm = hou_node.parm("folder0")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("__inputgroup_Geometry", "collapsed")
hou_node.setUserData("__inputgroup_Base", "collapsed")
hou_node.setUserData("__inputgroup_Transmission", "collapsed")
hou_node.setUserData("__inputgroup_Emission", "collapsed")
hou_node.setUserData("__inputgroup_Subsurface", "collapsed")
hou_node.setUserData("__inputgroup_Thin Film", "collapsed")
hou_node.setUserData("__inputgroup_Specular", "collapsed")
hou_node.setUserData("__inputgroup_Sheen", "collapsed")
hou_node.setUserData("__inputgroup_Coat", "collapsed")
hou_node.setUserData("___Version___", "")
hou_node.setUserData("__inputgroup_", "collapsed")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/Material_Outputs_and_AOVs
hou_node = hou_parent.createNode("suboutput", "Material_Outputs_and_AOVs", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.18326, -3.8725))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/Material_Outputs_and_AOVs/name1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/Material_Outputs_and_AOVs")
hou_parm = hou_node.parm("name1")
hou_parm.deleteAllKeyframes()
hou_parm.set("surface")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.0.547")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/material_properties
hou_node = hou_parent.createNode("kma_material_properties", "material_properties", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-5.56962, -4.0225))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlximage1
hou_node = hou_parent.createNode("mtlximage", "mtlximage1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-7.14156, -0.243427))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlximage1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlximage1")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("color3")


# Code for /stage/materiallibrary1/random_uv/mtlximage1/file parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlximage1")
hou_parm = hou_node.parm("file")
hou_parm.deleteAllKeyframes()
hou_parm.set("$HFS/houdini/pic/Mandril.rat")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxtexcoord2
hou_node = hou_parent.createNode("mtlxtexcoord", "mtlxtexcoord2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-37.8802, 3.03236))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxtexcoord2/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxtexcoord2")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/uv_scale
hou_node = hou_parent.createNode("mtlxmultiply", "uv_scale", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-29.4954, 3.48551))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/uv_scale/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/uv_scale")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2")


# Code for /stage/materiallibrary1/random_uv/uv_scale/in2_vector2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/uv_scale")
hou_parm_tuple = hou_node.parmTuple("in2_vector2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((5, 5))


hou_node.setColor(hou.Color([1, 0.725, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxadd4
hou_node = hou_parent.createNode("mtlxadd", "mtlxadd4", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-22.1092, 4.54604))
if hou_parent.findNetworkBox("__netbox2") is not None:
    hou_parent.findNetworkBox("__netbox2").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxadd4/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxadd4")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2FA")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxcellnoise2d1
hou_node = hou_parent.createNode("mtlxcellnoise2d", "mtlxcellnoise2d1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-22.4316, -0.664301))
if hou_parent.findNetworkBox("__netbox1") is not None:
    hou_parent.findNetworkBox("__netbox1").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxmultiply5
hou_node = hou_parent.createNode("mtlxmultiply", "mtlxmultiply5", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-24.5379, -0.664301))
if hou_parent.findNetworkBox("__netbox1") is not None:
    hou_parent.findNetworkBox("__netbox1").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(True)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxmultiply5/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxmultiply5")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2")


# Code for /stage/materiallibrary1/random_uv/mtlxmultiply5/in2_vector2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxmultiply5")
hou_parm_tuple = hou_node.parmTuple("in2_vector2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1.1000000000000001, 1.1000000000000001))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/uv_rotate
hou_node = hou_parent.createNode("mtlxrotate2d", "uv_rotate", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-13.69, 4.54604))
if hou_parent.findNetworkBox("__netbox2") is not None:
    hou_parent.findNetworkBox("__netbox2").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/uv_rotate/amount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/uv_rotate")
hou_parm = hou_node.parm("amount")
hou_parm.deleteAllKeyframes()
hou_parm.set(216.5)


hou_node.setColor(hou.Color([1, 0.725, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxmodulo2
hou_node = hou_parent.createNode("mtlxmodulo", "mtlxmodulo2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-19.1779, 4.54604))
if hou_parent.findNetworkBox("__netbox2") is not None:
    hou_parent.findNetworkBox("__netbox2").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxmodulo2/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxmodulo2")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxsubtract1
hou_node = hou_parent.createNode("mtlxsubtract", "mtlxsubtract1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-16.602, 4.54604))
if hou_parent.findNetworkBox("__netbox2") is not None:
    hou_parent.findNetworkBox("__netbox2").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxsubtract1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxsubtract1")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2")


# Code for /stage/materiallibrary1/random_uv/mtlxsubtract1/in2_vector2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxsubtract1")
hou_parm_tuple = hou_node.parmTuple("in2_vector2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.5, 0.5))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxadd5
hou_node = hou_parent.createNode("mtlxadd", "mtlxadd5", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-11.4028, 4.54604))
if hou_parent.findNetworkBox("__netbox2") is not None:
    hou_parent.findNetworkBox("__netbox2").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxadd5/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxadd5")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2FA")


# Code for /stage/materiallibrary1/random_uv/mtlxadd5/in2_vector2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxadd5")
hou_parm_tuple = hou_node.parmTuple("in2_vector2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.5, 0.5))


hou_node.setComment("旋转之后位置还原")
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxrange1
hou_node = hou_parent.createNode("mtlxrange", "mtlxrange1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-15.9539, 3.25736))
if hou_parent.findNetworkBox("__netbox2") is not None:
    hou_parent.findNetworkBox("__netbox2").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxrange1/outlow parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxrange1")
hou_parm = hou_node.parm("outlow")
hou_parm.deleteAllKeyframes()
hou_parm.set(-90)


# Code for /stage/materiallibrary1/random_uv/mtlxrange1/outhigh parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxrange1")
hou_parm = hou_node.parm("outhigh")
hou_parm.deleteAllKeyframes()
hou_parm.set(180)


hou_node.setColor(hou.Color([1, 0.725, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxmultiply6
hou_node = hou_parent.createNode("mtlxmultiply", "mtlxmultiply6", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-11.4263, -0.0832847))
if hou_parent.findNetworkBox("__netbox3") is not None:
    hou_parent.findNetworkBox("__netbox3").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxmultiply6/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxmultiply6")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2FA")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxrange2
hou_node = hou_parent.createNode("mtlxrange", "mtlxrange2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-14.6753, -1.15357))
if hou_parent.findNetworkBox("__netbox3") is not None:
    hou_parent.findNetworkBox("__netbox3").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxrange2/inhigh parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxrange2")
hou_parm = hou_node.parm("inhigh")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.81699999999999995)


# Code for /stage/materiallibrary1/random_uv/mtlxrange2/outlow parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxrange2")
hou_parm = hou_node.parm("outlow")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.67800000000000005)


# Code for /stage/materiallibrary1/random_uv/mtlxrange2/outhigh parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxrange2")
hou_parm = hou_node.parm("outhigh")
hou_parm.deleteAllKeyframes()
hou_parm.set(1.1930000000000001)


hou_node.setColor(hou.Color([1, 0.725, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxadd6
hou_node = hou_parent.createNode("mtlxadd", "mtlxadd6", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-26.9408, -0.664301))
if hou_parent.findNetworkBox("__netbox1") is not None:
    hou_parent.findNetworkBox("__netbox1").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxadd6/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxadd6")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2FA")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxnoise2d1
hou_node = hou_parent.createNode("mtlxnoise2d", "mtlxnoise2d1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-35.4023, -2.6074))
if hou_parent.findNetworkBox("__netbox4") is not None:
    hou_parent.findNetworkBox("__netbox4").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxnoise2d1/amplitude parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxnoise2d1")
hou_parm = hou_node.parm("amplitude")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


hou_node.setColor(hou.Color([1, 0.725, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxmultiply8
hou_node = hou_parent.createNode("mtlxmultiply", "mtlxmultiply8", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-37.6057, -2.7574))
if hou_parent.findNetworkBox("__netbox4") is not None:
    hou_parent.findNetworkBox("__netbox4").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxmultiply8/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxmultiply8")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2")


# Code for /stage/materiallibrary1/random_uv/mtlxmultiply8/in2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxmultiply8")
hou_parm = hou_node.parm("in2")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.38700000000000001)


# Code for /stage/materiallibrary1/random_uv/mtlxmultiply8/in2_vector2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxmultiply8")
hou_parm_tuple = hou_node.parmTuple("in2_vector2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((11.300000000000001, 11.300000000000001))


hou_node.setColor(hou.Color([1, 0.725, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxsubtract2
hou_node = hou_parent.createNode("mtlxsubtract", "mtlxsubtract2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-33.2622, -2.6824))
if hou_parent.findNetworkBox("__netbox4") is not None:
    hou_parent.findNetworkBox("__netbox4").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxsubtract2/in2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxsubtract2")
hou_parm = hou_node.parm("in2")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxmultiply9
hou_node = hou_parent.createNode("mtlxmultiply", "mtlxmultiply9", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-31.104, -2.6824))
if hou_parent.findNetworkBox("__netbox4") is not None:
    hou_parent.findNetworkBox("__netbox4").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/random_uv/mtlxmultiply9/in2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/random_uv/mtlxmultiply9")
hou_parm = hou_node.parm("in2")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.64400000000000002)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/random_uv/mtlxrandomfloat1
hou_node = hou_parent.createNode("mtlxrandomfloat", "mtlxrandomfloat1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-18.9856, 3.25736))
if hou_parent.findNetworkBox("__netbox2") is not None:
    hou_parent.findNetworkBox("__netbox2").addNode(hou_node)
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(True)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxstandard_surface
hou_node = hou_parent.node("mtlxstandard_surface")
if hou_parent.node("mtlximage1") is not None:
    hou_node.setInput(1, hou_parent.node("mtlximage1"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/Material_Outputs_and_AOVs
hou_node = hou_parent.node("Material_Outputs_and_AOVs")
if hou_parent.node("mtlxstandard_surface") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxstandard_surface"), 0)
if hou_parent.node("material_properties") is not None:
    hou_node.setInput(1, hou_parent.node("material_properties"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlximage1
hou_node = hou_parent.node("mtlximage1")
if hou_parent.node("mtlxmultiply6") is not None:
    hou_node.setInput(3, hou_parent.node("mtlxmultiply6"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/uv_scale
hou_node = hou_parent.node("uv_scale")
if hou_parent.node("mtlxtexcoord2") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxtexcoord2"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxadd4
hou_node = hou_parent.node("mtlxadd4")
if hou_parent.node("uv_scale") is not None:
    hou_node.setInput(0, hou_parent.node("uv_scale"), 0)
if hou_parent.node("mtlxcellnoise2d1") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxcellnoise2d1"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxcellnoise2d1
hou_node = hou_parent.node("mtlxcellnoise2d1")
if hou_parent.node("mtlxmultiply5") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxmultiply5"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxmultiply5
hou_node = hou_parent.node("mtlxmultiply5")
if hou_parent.node("mtlxadd6") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxadd6"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/uv_rotate
hou_node = hou_parent.node("uv_rotate")
if hou_parent.node("mtlxsubtract1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxsubtract1"), 0)
if hou_parent.node("mtlxrange1") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxrange1"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxmodulo2
hou_node = hou_parent.node("mtlxmodulo2")
if hou_parent.node("mtlxadd4") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxadd4"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxsubtract1
hou_node = hou_parent.node("mtlxsubtract1")
if hou_parent.node("mtlxmodulo2") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxmodulo2"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxadd5
hou_node = hou_parent.node("mtlxadd5")
if hou_parent.node("uv_rotate") is not None:
    hou_node.setInput(0, hou_parent.node("uv_rotate"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxrange1
hou_node = hou_parent.node("mtlxrange1")
if hou_parent.node("mtlxrandomfloat1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxrandomfloat1"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxmultiply6
hou_node = hou_parent.node("mtlxmultiply6")
if hou_parent.node("mtlxadd5") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxadd5"), 0)
if hou_parent.node("mtlxrange2") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxrange2"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxrange2
hou_node = hou_parent.node("mtlxrange2")
if hou_parent.node("mtlxcellnoise2d1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxcellnoise2d1"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxadd6
hou_node = hou_parent.node("mtlxadd6")
if hou_parent.node("uv_scale") is not None:
    hou_node.setInput(0, hou_parent.node("uv_scale"), 0)
if hou_parent.node("mtlxmultiply9") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxmultiply9"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxnoise2d1
hou_node = hou_parent.node("mtlxnoise2d1")
if hou_parent.node("mtlxmultiply8") is not None:
    hou_node.setInput(2, hou_parent.node("mtlxmultiply8"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxmultiply8
hou_node = hou_parent.node("mtlxmultiply8")
if hou_parent.node("mtlxtexcoord2") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxtexcoord2"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxsubtract2
hou_node = hou_parent.node("mtlxsubtract2")
if hou_parent.node("mtlxnoise2d1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxnoise2d1"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxmultiply9
hou_node = hou_parent.node("mtlxmultiply9")
if hou_parent.node("mtlxsubtract2") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxsubtract2"), 0)
# Code to establish connections for /stage/materiallibrary1/random_uv/mtlxrandomfloat1
hou_node = hou_parent.node("mtlxrandomfloat1")
if hou_parent.node("mtlxcellnoise2d1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxcellnoise2d1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

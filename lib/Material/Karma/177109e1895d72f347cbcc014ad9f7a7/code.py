# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/stage/materiallibrary2")

# Code for /stage/materiallibrary2/Screen
hou_node = hou_parent.createNode("subnet", "Screen", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-8.47932, 1.95095))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

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
# Code for /stage/materiallibrary2/Screen/shader_referencetype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen")
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

hou_node.setUserData("___Version___", "20.0.547")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.0.547")
# Update the parent node.
hou_parent = hou_node

# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface
hou_node = hou_parent.createNode("mtlxstandard_surface", "mtlxstandard_surface", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(20.166, -1.66494))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/folder0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("folder0")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/base parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("base")
hou_parm.deleteAllKeyframes()
hou_parm.set(0)


# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/folder0_1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("folder0_1")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/specular_roughness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("specular_roughness")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.10000000000000001)


# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/folder0_5 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("folder0_5")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/coat parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("coat")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/coat_roughness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("coat_roughness")
hou_parm.deleteAllKeyframes()
hou_parm.set(0)


# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/coat_anisotropy parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("coat_anisotropy")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.021000000000000001)


# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/folder0_7 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("folder0_7")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /stage/materiallibrary2/Screen/mtlxstandard_surface/emission parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxstandard_surface")
hou_parm = hou_node.parm("emission")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("__inputgroup_Geometry", "collapsed")
hou_node.setUserData("__inputgroup_Transmission", "collapsed")
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

# Code for /stage/materiallibrary2/Screen/Material_Outputs_and_AOVs
hou_node = hou_parent.createNode("suboutput", "Material_Outputs_and_AOVs", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(22.8219, -4.67759))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/Material_Outputs_and_AOVs/name1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/Material_Outputs_and_AOVs")
hou_parm = hou_node.parm("name1")
hou_parm.deleteAllKeyframes()
hou_parm.set("surface")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "20.0.547")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.0.547")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/material_properties
hou_node = hou_parent.createNode("kma_material_properties", "material_properties", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(20.166, -6.30207))
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

# Code for /stage/materiallibrary2/Screen/mtlxtexcoord1
hou_node = hou_parent.createNode("mtlxtexcoord", "mtlxtexcoord1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-3.73711, -0.141266))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxtexcoord1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxtexcoord1")
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

# Code for /stage/materiallibrary2/Screen/mtlxline1
hou_node = hou_parent.createNode("mtlxline", "mtlxline1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(10.4883, 1.0402))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxline1/point1 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxline1")
hou_parm_tuple = hou_node.parmTuple("point1")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((-0.29999999999999999, 0.33000000000000002))


# Code for /stage/materiallibrary2/Screen/mtlxline1/point2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxline1")
hou_parm_tuple = hou_node.parmTuple("point2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.29999999999999999, 0.33000000000000002))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxrotate2d1
hou_node = hou_parent.createNode("mtlxrotate2d", "mtlxrotate2d1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(6.88649, -0.0662661))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

hou_node.setComment("uv旋转")
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxadd2
hou_node = hou_parent.createNode("mtlxadd", "mtlxadd2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(4.23059, -0.0662661))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxadd2/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxadd2")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2")


# Code for /stage/materiallibrary2/Screen/mtlxadd2/in2_vector2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxadd2")
hou_parm_tuple = hou_node.parmTuple("in2_vector2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((-0.5, -0.5))


hou_node.setComment("uv偏移到中间")
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxmultiply1
hou_node = hou_parent.createNode("mtlxmultiply", "mtlxmultiply1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.08121, -0.0662661))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxmultiply1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxmultiply1")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2")


# Code for /stage/materiallibrary2/Screen/mtlxmultiply1/in2_vector2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxmultiply1")
hou_parm_tuple = hou_node.parmTuple("in2_vector2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((5, 5))


hou_node.setComment("uv缩放")
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxmodulo1
hou_node = hou_parent.createNode("mtlxmodulo", "mtlxmodulo1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.57469, -0.0662661))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxmodulo1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxmodulo1")
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

# Code for /stage/materiallibrary2/Screen/mtlxadd1
hou_node = hou_parent.createNode("mtlxadd", "mtlxadd1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(14.8909, -0.716665))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxadd1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxadd1")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("color3")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxline2
hou_node = hou_parent.createNode("mtlxline", "mtlxline2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(10.4884, -2.39469))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxline2/point1 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxline2")
hou_parm_tuple = hou_node.parmTuple("point1")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((-0.29999999999999999, 0))


# Code for /stage/materiallibrary2/Screen/mtlxline2/point2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxline2")
hou_parm_tuple = hou_node.parmTuple("point2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.29999999999999999, 0))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxline3
hou_node = hou_parent.createNode("mtlxline", "mtlxline3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(10.4884, -6.6187))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxline3/point1 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxline3")
hou_parm_tuple = hou_node.parmTuple("point1")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((-0.29999999999999999, -0.33000000000000002))


# Code for /stage/materiallibrary2/Screen/mtlxline3/point2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxline3")
hou_parm_tuple = hou_node.parmTuple("point2")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.29999999999999999, -0.33000000000000002))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxadd3
hou_node = hou_parent.createNode("mtlxadd", "mtlxadd3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(17.2118, -1.99952))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxadd3/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxadd3")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("color3")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxmultiply2
hou_node = hou_parent.createNode("mtlxmultiply", "mtlxmultiply2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(12.4175, 2.21984))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxmultiply2/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxmultiply2")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("color3FA")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxcontrast1
hou_node = hou_parent.createNode("mtlxcontrast", "mtlxcontrast1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(10.4883, 2.29484))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxcontrast1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxcontrast1")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("color3")


# Code for /stage/materiallibrary2/Screen/mtlxcontrast1/in_color3 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxcontrast1")
hou_parm_tuple = hou_node.parmTuple("in_color3")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 0, 0))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxcontrast2
hou_node = hou_parent.createNode("mtlxcontrast", "mtlxcontrast2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(10.4883, -1.13574))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(True)

# Code for /stage/materiallibrary2/Screen/mtlxcontrast2/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxcontrast2")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("color3")


# Code for /stage/materiallibrary2/Screen/mtlxcontrast2/in_color3 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxcontrast2")
hou_parm_tuple = hou_node.parmTuple("in_color3")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 1))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxmultiply3
hou_node = hou_parent.createNode("mtlxmultiply", "mtlxmultiply3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(12.4088, -1.71038))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxmultiply3/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxmultiply3")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("color3FA")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxcontrast3
hou_node = hou_parent.createNode("mtlxcontrast", "mtlxcontrast3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(10.4884, -5.17207))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxcontrast3/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxcontrast3")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("color3")


# Code for /stage/materiallibrary2/Screen/mtlxcontrast3/in_color3 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxcontrast3")
hou_parm_tuple = hou_node.parmTuple("in_color3")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 1, 0))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary2/Screen/mtlxmultiply4
hou_node = hou_parent.createNode("mtlxmultiply", "mtlxmultiply4", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(12.7644, -6.15207))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary2/Screen/mtlxmultiply4/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary2/Screen/mtlxmultiply4")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("color3FA")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /stage/materiallibrary2/Screen/mtlxstandard_surface
hou_node = hou_parent.node("mtlxstandard_surface")
if hou_parent.node("mtlxadd3") is not None:
    hou_node.setInput(37, hou_parent.node("mtlxadd3"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/Material_Outputs_and_AOVs
hou_node = hou_parent.node("Material_Outputs_and_AOVs")
if hou_parent.node("mtlxstandard_surface") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxstandard_surface"), 0)
if hou_parent.node("material_properties") is not None:
    hou_node.setInput(1, hou_parent.node("material_properties"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxline1
hou_node = hou_parent.node("mtlxline1")
if hou_parent.node("mtlxrotate2d1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxrotate2d1"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxrotate2d1
hou_node = hou_parent.node("mtlxrotate2d1")
if hou_parent.node("mtlxadd2") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxadd2"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxadd2
hou_node = hou_parent.node("mtlxadd2")
if hou_parent.node("mtlxmodulo1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxmodulo1"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxmultiply1
hou_node = hou_parent.node("mtlxmultiply1")
if hou_parent.node("mtlxtexcoord1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxtexcoord1"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxmodulo1
hou_node = hou_parent.node("mtlxmodulo1")
if hou_parent.node("mtlxmultiply1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxmultiply1"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxadd1
hou_node = hou_parent.node("mtlxadd1")
if hou_parent.node("mtlxmultiply2") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxmultiply2"), 0)
if hou_parent.node("mtlxmultiply3") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxmultiply3"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxline2
hou_node = hou_parent.node("mtlxline2")
if hou_parent.node("mtlxrotate2d1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxrotate2d1"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxline3
hou_node = hou_parent.node("mtlxline3")
if hou_parent.node("mtlxrotate2d1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxrotate2d1"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxadd3
hou_node = hou_parent.node("mtlxadd3")
if hou_parent.node("mtlxadd1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxadd1"), 0)
if hou_parent.node("mtlxmultiply4") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxmultiply4"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxmultiply2
hou_node = hou_parent.node("mtlxmultiply2")
if hou_parent.node("mtlxcontrast1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxcontrast1"), 0)
if hou_parent.node("mtlxline1") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxline1"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxmultiply3
hou_node = hou_parent.node("mtlxmultiply3")
if hou_parent.node("mtlxcontrast2") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxcontrast2"), 0)
if hou_parent.node("mtlxline2") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxline2"), 0)
# Code to establish connections for /stage/materiallibrary2/Screen/mtlxmultiply4
hou_node = hou_parent.node("mtlxmultiply4")
if hou_parent.node("mtlxcontrast3") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxcontrast3"), 0)
if hou_parent.node("mtlxline3") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxline3"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

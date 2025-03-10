# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/mat")

# Code for /mat/karmamaterial
hou_node = hou_parent.createNode("subnet", "karmamaterial", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-2.02058, 0.360381))
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
# Code for /mat/karmamaterial/shader_referencetype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/karmamaterial")
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

# Code for /mat/karmamaterial/mtlxstandard_surface
hou_node = hou_parent.createNode("mtlxstandard_surface", "mtlxstandard_surface", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-0.2883, 0.0376))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /mat/karmamaterial/mtlxstandard_surface/folder0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/karmamaterial/mtlxstandard_surface")
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

# Code for /mat/karmamaterial/Material_Outputs_and_AOVs
hou_node = hou_parent.createNode("suboutput", "Material_Outputs_and_AOVs", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.42924, -2.5372))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /mat/karmamaterial/Material_Outputs_and_AOVs/name1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/karmamaterial/Material_Outputs_and_AOVs")
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

# Code for /mat/karmamaterial/material_properties
hou_node = hou_parent.createNode("kma_material_properties", "material_properties", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-0.2883, -3.87213))
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

# Code to establish connections for /mat/karmamaterial/Material_Outputs_and_AOVs
hou_node = hou_parent.node("Material_Outputs_and_AOVs")
if hou_parent.node("mtlxstandard_surface") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxstandard_surface"), 0)
if hou_parent.node("material_properties") is not None:
    hou_node.setInput(1, hou_parent.node("material_properties"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/stage/materiallibrary1")

# Code for /stage/materiallibrary1/anisotropy
hou_node = hou_parent.createNode("subnet", "anisotropy", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-3.25539, 4.53662))
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
hou_parm_template2.setTags({"script_action": "import lopshaderutils\nlopshaderutils.selectPrimFromInputOrFile(kwargs)", "script_action_help": "Select a primitive in the Scene Viewer or Scene Graph Tree pane.\nCtrl-click to select using the primitive picker dialog.", "script_action_icon": "BUTTONS_reselect", "sidefx::shader_isparm": "0", "sidefx::usdpathtype": "prim", "spare_category": "Shader"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.SeparatorParmTemplate("separator1")
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("tabmenumask", "Tab Menu Mask", 1, default_value=(["karma USD ^mtlxUsd* ^mtlxramp* ^hmtlxramp* ^hmtlxcubicramp* MaterialX parameter constant collect null genericshader subnet subnetconnector suboutput subinput"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
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
# Code for /stage/materiallibrary1/anisotropy/shader_referencetype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy")
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

hou_node.setUserData("wirestyle", "rounded")
hou_node.setUserData("___Version___", "20.5.410")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.5.410")
# Update the parent node.
hou_parent = hou_node

# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/stage/materiallibrary1/anisotropy")

# Code for /stage/materiallibrary1/anisotropy/__stickynote1
hou_sticky = hou_parent.createStickyNote("__stickynote1")
hou_sticky.setText("对象的UV需要处理,圆形中心需要再0,0")
hou_sticky.setTextSize(0)
hou_sticky.setTextColor(hou.Color((0, 0, 0)))
hou_sticky.setDrawBackground(True)
hou_sticky.setPosition(hou.Vector2(-16.8231, 7.84577))
hou_sticky.setSize(hou.Vector2(2.5, 0.987881))
hou_sticky.setMinimized(False)
hou_sticky.setSelected(False)
hou_sticky.setColor(hou.Color([1, 0.969, 0.522]))

# Code for /stage/materiallibrary1/anisotropy/mtlxstandard_surface
hou_node = hou_parent.createNode("mtlxstandard_surface", "mtlxstandard_surface", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-2.94726, 6.32339))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxstandard_surface/folder0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxstandard_surface")
hou_parm = hou_node.parm("folder0")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /stage/materiallibrary1/anisotropy/mtlxstandard_surface/metalness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxstandard_surface")
hou_parm = hou_node.parm("metalness")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /stage/materiallibrary1/anisotropy/mtlxstandard_surface/folder0_1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxstandard_surface")
hou_parm = hou_node.parm("folder0_1")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /stage/materiallibrary1/anisotropy/mtlxstandard_surface/specular_roughness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxstandard_surface")
hou_parm = hou_node.parm("specular_roughness")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.57299999999999995)


# Code for /stage/materiallibrary1/anisotropy/mtlxstandard_surface/specular_anisotropy parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxstandard_surface")
hou_parm = hou_node.parm("specular_anisotropy")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.61499999999999999)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("__inputgroup_Emission", "collapsed")
hou_node.setUserData("__inputgroup_", "collapsed")
hou_node.setUserData("__inputgroup_Thin Film", "collapsed")
hou_node.setUserData("___Version___", "")
hou_node.setUserData("__inputgroup_Coat", "collapsed")
hou_node.setUserData("__inputgroup_Subsurface", "collapsed")
hou_node.setUserData("__inputgroup_Transmission", "collapsed")
hou_node.setUserData("__inputgroup_Base", "collapsed")
hou_node.setUserData("__inputgroup_Sheen", "collapsed")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/anisotropy/Material_Outputs_and_AOVs
hou_node = hou_parent.createNode("suboutput", "Material_Outputs_and_AOVs", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.0305319, 2.0234))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/Material_Outputs_and_AOVs/name1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/Material_Outputs_and_AOVs")
hou_parm = hou_node.parm("name1")
hou_parm.deleteAllKeyframes()
hou_parm.set("surface")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "20.5.410")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.5.410")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/anisotropy/material_properties
hou_node = hou_parent.createNode("kma_material_properties", "material_properties", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-2.62537, -1.04762))
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

# Code for /stage/materiallibrary1/anisotropy/mtlxtexcoord1
hou_node = hou_parent.createNode("mtlxtexcoord", "mtlxtexcoord1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-29.1844, 6.19968))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxtexcoord1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxtexcoord1")
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

# Code for /stage/materiallibrary1/anisotropy/mtlxsubtract1
hou_node = hou_parent.createNode("mtlxsubtract", "mtlxsubtract1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-26.5285, 6.27468))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxsubtract1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxsubtract1")
hou_parm = hou_node.parm("signature")
hou_parm.deleteAllKeyframes()
hou_parm.set("vector2FA")


# Code for /stage/materiallibrary1/anisotropy/mtlxsubtract1/in2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxsubtract1")
hou_parm = hou_node.parm("in2")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /stage/materiallibrary1/anisotropy/mtlxsubtract1/in2_vector2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxsubtract1")
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

# Code for /stage/materiallibrary1/anisotropy/mtlxdistance1
hou_node = hou_parent.createNode("mtlxdistance", "mtlxdistance1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-16.147, 1.04229))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxdistance1/in2 parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxdistance1")
hou_parm_tuple = hou_node.parmTuple("in2")
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

# Code for /stage/materiallibrary1/anisotropy/mtlxrotate2d1
hou_node = hou_parent.createNode("mtlxrotate2d", "mtlxrotate2d1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-23.8726, 6.27468))
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

# Code for /stage/materiallibrary1/anisotropy/mtlxseparate2
hou_node = hou_parent.createNode("mtlxseparate2", "mtlxseparate2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-21.2167, 6.27468))
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

# Code for /stage/materiallibrary1/anisotropy/mtlxatan2
hou_node = hou_parent.createNode("mtlxatan2", "mtlxatan2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-18.5608, 6.27468))
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

# Code for /stage/materiallibrary1/anisotropy/mtlxremap1
hou_node = hou_parent.createNode("mtlxremap", "mtlxremap1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-15.9049, 6.49968))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxremap1/inlow parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxremap1")
hou_parm = hou_node.parm("inlow")
hou_parm.deleteAllKeyframes()
hou_parm.set(-3.1415926535897931)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("-$PI", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("-$PI", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("-$PI", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("-$PI", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /stage/materiallibrary1/anisotropy/mtlxremap1/inhigh parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxremap1")
hou_parm = hou_node.parm("inhigh")
hou_parm.deleteAllKeyframes()
hou_parm.set(3.1415926535897931)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("$PI", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("$PI", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("$PI", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("$PI", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/anisotropy/mtlxcombine2
hou_node = hou_parent.createNode("mtlxcombine2", "mtlxcombine2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-13.696, 1.08886))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxcombine2/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxcombine2")
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

# Code for /stage/materiallibrary1/anisotropy/mtlxgeompropvalue1
hou_node = hou_parent.createNode("mtlxgeompropvalue", "mtlxgeompropvalue1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-13.249, 4.39608))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxgeompropvalue1/geomprop parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxgeompropvalue1")
hou_parm = hou_node.parm("geomprop")
hou_parm.deleteAllKeyframes()
hou_parm.set("side")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/anisotropy/mtlxmix1
hou_node = hou_parent.createNode("mtlxmix", "mtlxmix1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-10.5931, 1.66098))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxmix1/signature parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxmix1")
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

# Code for /stage/materiallibrary1/anisotropy/mtlxmix2
hou_node = hou_parent.createNode("mtlxmix", "mtlxmix2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-8.13323, 6.36637))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxmix2/fg parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxmix2")
hou_parm = hou_node.parm("fg")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.26000000000000001)


hou_node.setComment("调整fg可以旋转反射角度")
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/anisotropy/mtlxunifiednoise2d1
hou_node = hou_parent.createNode("mtlxunifiednoise2d", "mtlxunifiednoise2d1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-7.9859, 1.97138))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxunifiednoise2d1/freq parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxunifiednoise2d1")
hou_parm_tuple = hou_node.parmTuple("freq")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((5, 1000))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /stage/materiallibrary1/anisotropy/mtlxbump1
hou_node = hou_parent.createNode("mtlxbump", "mtlxbump1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-5.45562, 3.78801))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /stage/materiallibrary1/anisotropy/mtlxbump1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/stage/materiallibrary1/anisotropy/mtlxbump1")
hou_parm = hou_node.parm("scale")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.002)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxstandard_surface
hou_node = hou_parent.node("mtlxstandard_surface")
if hou_parent.node("mtlxmix2") is not None:
    hou_node.setInput(9, hou_parent.node("mtlxmix2"), 0)
if hou_parent.node("mtlxbump1") is not None:
    hou_node.setInput(40, hou_parent.node("mtlxbump1"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/Material_Outputs_and_AOVs
hou_node = hou_parent.node("Material_Outputs_and_AOVs")
if hou_parent.node("mtlxstandard_surface") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxstandard_surface"), 0)
if hou_parent.node("material_properties") is not None:
    hou_node.setInput(1, hou_parent.node("material_properties"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxsubtract1
hou_node = hou_parent.node("mtlxsubtract1")
if hou_parent.node("mtlxtexcoord1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxtexcoord1"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxdistance1
hou_node = hou_parent.node("mtlxdistance1")
if hou_parent.node("mtlxtexcoord1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxtexcoord1"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxrotate2d1
hou_node = hou_parent.node("mtlxrotate2d1")
if hou_parent.node("mtlxsubtract1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxsubtract1"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxseparate2
hou_node = hou_parent.node("mtlxseparate2")
if hou_parent.node("mtlxrotate2d1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxrotate2d1"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxatan2
hou_node = hou_parent.node("mtlxatan2")
if hou_parent.node("mtlxseparate2") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxseparate2"), 0)
if hou_parent.node("mtlxseparate2") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxseparate2"), 1)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxremap1
hou_node = hou_parent.node("mtlxremap1")
if hou_parent.node("mtlxatan2") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxatan2"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxcombine2
hou_node = hou_parent.node("mtlxcombine2")
if hou_parent.node("mtlxremap1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxremap1"), 0)
if hou_parent.node("mtlxdistance1") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxdistance1"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxmix1
hou_node = hou_parent.node("mtlxmix1")
if hou_parent.node("mtlxtexcoord1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxtexcoord1"), 0)
if hou_parent.node("mtlxcombine2") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxcombine2"), 0)
if hou_parent.node("mtlxgeompropvalue1") is not None:
    hou_node.setInput(2, hou_parent.node("mtlxgeompropvalue1"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxmix2
hou_node = hou_parent.node("mtlxmix2")
if hou_parent.node("mtlxremap1") is not None:
    hou_node.setInput(1, hou_parent.node("mtlxremap1"), 0)
if hou_parent.node("mtlxgeompropvalue1") is not None:
    hou_node.setInput(2, hou_parent.node("mtlxgeompropvalue1"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxunifiednoise2d1
hou_node = hou_parent.node("mtlxunifiednoise2d1")
if hou_parent.node("mtlxmix1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxmix1"), 0)
# Code to establish connections for /stage/materiallibrary1/anisotropy/mtlxbump1
hou_node = hou_parent.node("mtlxbump1")
if hou_parent.node("mtlxunifiednoise2d1") is not None:
    hou_node.setInput(0, hou_parent.node("mtlxunifiednoise2d1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

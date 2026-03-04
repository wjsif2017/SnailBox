# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj/matnet2")

# Code for /obj/matnet2/redshift_hari
hou_node = hou_parent.createNode("redshift_vopnet", "redshift_hari", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-18.3922, 8.21214))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "20.0.547")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.0.547")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/matnet2/redshift_hari/redshift_material1
hou_node = hou_parent.createNode("redshift_material", "redshift_material1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0, -0.45))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "20.0.547")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.0.547")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/matnet2/redshift_hari/Hair1
hou_node = hou_parent.createNode("redshift::Hair", "Hair1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-2.80821, 0.501408))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /obj/matnet2/redshift_hari/Hair1/Internal_Reflection_0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("Internal_Reflection_0")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/matnet2/redshift_hari/Hair1/irefl_gloss parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("irefl_gloss")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.70499999999999996)


# Code for /obj/matnet2/redshift_hari/Hair1/Diffuse_1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("Diffuse_1")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/matnet2/redshift_hari/Hair1/Transmission_2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("Transmission_2")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/matnet2/redshift_hari/Hair1/Primary_Reflection_3 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("Primary_Reflection_3")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/matnet2/redshift_hari/Hair1/Transparency_4 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("Transparency_4")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/matnet2/redshift_hari/Hair1/Reflection_5 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("Reflection_5")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/matnet2/redshift_hari/Hair1/Cut_off_Override_6 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("Cut_off_Override_6")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/matnet2/redshift_hari/Hair1/Transparency_7 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("Transparency_7")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/matnet2/redshift_hari/Hair1/Transparency_Cut_off_Override_8 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/matnet2/redshift_hari/Hair1")
hou_parm = hou_node.parm("Transparency_Cut_off_Override_8")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("__inputgroup_General", "collapsed")
hou_node.setUserData("__inputgroup_Transparency", "collapsed")
hou_node.setUserData("__inputgroup_", "collapsed")
hou_node.setUserData("__inputgroup_Advanced", "collapsed")
hou_node.setUserData("___Version___", "20.0.547")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.0.547")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /obj/matnet2/redshift_hari/redshift_material1
hou_node = hou_parent.node("redshift_material1")
if hou_parent.node("Hair1") is not None:
    hou_node.setInput(0, hou_parent.node("Hair1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

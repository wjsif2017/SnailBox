# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/mat")

# Code for /mat/redshift_vopnet1
hou_node = hou_parent.createNode("redshift_vopnet", "redshift_vopnet1", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-13.9024, 11.4737))
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
hou_node.setUserData("snailBox_mat", "{\"group\": null, \"ignore\": 0, \"fav\": 1, \"mode\": 0}")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.0.547")
# Update the parent node.
hou_parent = hou_node

# Code for /mat/redshift_vopnet1/redshift_material1
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

# Code for /mat/redshift_vopnet1/StandardMaterial1
hou_node = hou_parent.createNode("redshift::StandardMaterial", "StandardMaterial1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-2.5236, 0))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /mat/redshift_vopnet1/StandardMaterial1/Base_0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Base_0")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/base_color parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm_tuple = hou_node.parmTuple("base_color")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 0.5, 0))


# Code for /mat/redshift_vopnet1/StandardMaterial1/base_color_weight parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("base_color_weight")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.71799999999999997)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Reflection_1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Reflection_1")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Transmission_2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Transmission_2")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Coat_6 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Coat_6")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Emission_7 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Emission_7")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Geometry_8 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Geometry_8")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Reflection_9 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Reflection_9")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Transmission_10 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Transmission_10")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Diffuse_11 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Diffuse_11")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Reflection_12 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Reflection_12")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Transmission_13 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Transmission_13")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Sheen_14 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Sheen_14")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Coat_15 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Coat_15")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/redshift_vopnet1/StandardMaterial1/Anisotropy_16 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/redshift_vopnet1/StandardMaterial1")
hou_parm = hou_node.parm("Anisotropy_16")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("__inputgroup_Advanced", "collapsed")
hou_node.setUserData("__inputgroup_", "collapsed")
hou_node.setUserData("___Version___", "20.0.547")
hou_node.setUserData("__inputgroup_Base Properties", "collapsed")
hou_node.setUserData("__inputgroup_Optimizations", "collapsed")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("20.0.547")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /mat/redshift_vopnet1/redshift_material1
hou_node = hou_parent.node("redshift_material1")
if hou_parent.node("StandardMaterial1") is not None:
    hou_node.setInput(0, hou_parent.node("StandardMaterial1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

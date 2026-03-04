# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/mat")

# Code for /mat/kma_hair_for_snow
hou_node = hou_parent.createNode("kma_hair", "kma_hair_for_snow", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-15.6337, 11.5791))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /mat/kma_hair_for_snow/baseColor parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_snow")
hou_parm_tuple = hou_node.parmTuple("baseColor")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.93800002336502075, 0.94853997230529785, 1))


# Code for /mat/kma_hair_for_snow/melanin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_snow")
hou_parm = hou_node.parm("melanin")
hou_parm.deleteAllKeyframes()
hou_parm.set(0)


# Code for /mat/kma_hair_for_snow/melaninRedness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_snow")
hou_parm = hou_node.parm("melaninRedness")
hou_parm.deleteAllKeyframes()
hou_parm.set(0)


# Code for /mat/kma_hair_for_snow/ior parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_snow")
hou_parm = hou_node.parm("ior")
hou_parm.deleteAllKeyframes()
hou_parm.set(1.3500000000000001)


# Code for /mat/kma_hair_for_snow/roughness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_snow")
hou_parm = hou_node.parm("roughness")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.45000000000000001)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("__inputgroup_Specular", "collapsed")
hou_node.setUserData("__inputgroup_Advanced", "collapsed")
hou_node.setUserData("__inputgroup_Diffuse", "collapsed")
hou_node.setUserData("___Version___", "")
hou_node.setUserData("__inputgroup_Color", "collapsed")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

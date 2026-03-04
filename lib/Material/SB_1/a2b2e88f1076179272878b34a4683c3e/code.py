# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/mat")

# Code for /mat/kma_hair_for_sand
hou_node = hou_parent.createNode("kma_hair", "kma_hair_for_sand", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-13.1101, 10.1667))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /mat/kma_hair_for_sand/g01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_sand")
hou_parm = hou_node.parm("g01")
hou_parm.deleteAllKeyframes()
hou_parm.set(2)


# Code for /mat/kma_hair_for_sand/baseColor parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_sand")
hou_parm_tuple = hou_node.parmTuple("baseColor")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 0.59052330255508423, 0.2369999885559082))


# Code for /mat/kma_hair_for_sand/melanin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_sand")
hou_parm = hou_node.parm("melanin")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.106)


# Code for /mat/kma_hair_for_sand/melaninRandomize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_sand")
hou_parm = hou_node.parm("melaninRandomize")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/kma_hair_for_sand/roughness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_sand")
hou_parm = hou_node.parm("roughness")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /mat/kma_hair_for_sand/roughnessRandomize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_sand")
hou_parm = hou_node.parm("roughnessRandomize")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/kma_hair_for_sand/diffuse parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_sand")
hou_parm = hou_node.parm("diffuse")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.10000000000000001)


# Code for /mat/kma_hair_for_sand/diffuseColor parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/kma_hair_for_sand")
hou_parm_tuple = hou_node.parmTuple("diffuseColor")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 0.66901999711990356, 0.25900000333786011))


hou_node.setComment("注意：该材质可能需要点数量恒定不变")
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

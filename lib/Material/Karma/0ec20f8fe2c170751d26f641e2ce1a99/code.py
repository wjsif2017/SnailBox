# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/mat")

# Code for /mat/snow_or_cloud_or_ww
hou_node = hou_parent.createNode("kma_pyropreview", "snow_or_cloud_or_ww", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-20.6809, 15.1539))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /mat/snow_or_cloud_or_ww/densityscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/snow_or_cloud_or_ww")
hou_parm = hou_node.parm("densityscale")
hou_parm.deleteAllKeyframes()
hou_parm.set(1000000)


# Code for /mat/snow_or_cloud_or_ww/shadowcolor parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/snow_or_cloud_or_ww")
hou_parm_tuple = hou_node.parmTuple("shadowcolor")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.7369999885559082, 0.8961150050163269, 1))


# Code for /mat/snow_or_cloud_or_ww/phase parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/snow_or_cloud_or_ww")
hou_parm = hou_node.parm("phase")
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

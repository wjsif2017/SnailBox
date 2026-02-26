# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/mat")

# Code for /mat/bubbles
hou_node = hou_parent.createNode("mtlxstandard_surface", "bubbles", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-18.1573, 12.9915))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /mat/bubbles/folder0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/bubbles")
hou_parm = hou_node.parm("folder0")
hou_parm.deleteAllKeyframes()
hou_parm.set(7)


# Code for /mat/bubbles/base parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/bubbles")
hou_parm = hou_node.parm("base")
hou_parm.deleteAllKeyframes()
hou_parm.set(0)


# Code for /mat/bubbles/specular_roughness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/bubbles")
hou_parm = hou_node.parm("specular_roughness")
hou_parm.deleteAllKeyframes()
hou_parm.set(0)


# Code for /mat/bubbles/specular_IOR parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/bubbles")
hou_parm = hou_node.parm("specular_IOR")
hou_parm.deleteAllKeyframes()
hou_parm.set(1.3300000000000001)


# Code for /mat/bubbles/transmission parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/bubbles")
hou_parm = hou_node.parm("transmission")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.90000000000000002)


# Code for /mat/bubbles/emission parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/bubbles")
hou_parm = hou_node.parm("emission")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.040000000000000001)


# Code for /mat/bubbles/thin_walled parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/bubbles")
hou_parm = hou_node.parm("thin_walled")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("__inputgroup_Geometry", "collapsed")
hou_node.setUserData("__inputgroup_Base", "collapsed")
hou_node.setUserData("__inputgroup_Transmission", "collapsed")
hou_node.setUserData("__inputgroup_Subsurface", "collapsed")
hou_node.setUserData("__inputgroup_Emission", "collapsed")
hou_node.setUserData("__inputgroup_Thin Film", "collapsed")
hou_node.setUserData("__inputgroup_Sheen", "collapsed")
hou_node.setUserData("__inputgroup_Specular", "collapsed")
hou_node.setUserData("__inputgroup_Coat", "collapsed")
hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

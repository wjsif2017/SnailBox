# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/mat")

# Code for /mat/principledshader1
hou_node = hou_parent.createNode("principledshader::2.0", "principledshader1", run_init_scripts=False, load_contents=True, exact_type_name=True)
snail_re_node.append(hou_node.path())
hou_node.move(hou.Vector2(-4.17169, -1.28706))
hou_node.setDebugFlag(False)
hou_node.setDetailLowFlag(False)
hou_node.setDetailMediumFlag(False)
hou_node.setDetailHighFlag(True)
hou_node.bypass(False)
hou_node.setCompressFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

# Code for /mat/principledshader1/specular_tint parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("specular_tint")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("(1-ch(\"metallic\"))*ch(\"reflecttint\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("(1-ch(\"metallic\"))*ch(\"reflecttint\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("(1-ch(\"metallic\"))*ch(\"reflecttint\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("(1-ch(\"metallic\"))*ch(\"reflecttint\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /mat/principledshader1/folder7 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("folder7")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/principledshader1/folder4 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("folder4")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/principledshader1/folder12 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("folder12")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/principledshader1/folder13 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("folder13")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/principledshader1/folder8 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("folder8")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/principledshader1/folder11 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("folder11")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/principledshader1/folder9 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("folder9")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /mat/principledshader1/baseBump_useTexture parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("baseBump_useTexture")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("ch(\"baseBumpAndNormal_enable\") && strcmp(chs(\"baseBumpAndNormal_type\"), \"bump\") == 0", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("ch(\"baseBumpAndNormal_enable\") && strcmp(chs(\"baseBumpAndNormal_type\"), \"bump\") == 0", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("ch(\"baseBumpAndNormal_enable\") && strcmp(chs(\"baseBumpAndNormal_type\"), \"bump\") == 0", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("ch(\"baseBumpAndNormal_enable\") && strcmp(chs(\"baseBumpAndNormal_type\"), \"bump\") == 0", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /mat/principledshader1/baseNormal_useTexture parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("baseNormal_useTexture")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("ch(\"baseBumpAndNormal_enable\") && strcmp(chs(\"baseBumpAndNormal_type\"), \"normal\") == 0", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("ch(\"baseBumpAndNormal_enable\") && strcmp(chs(\"baseBumpAndNormal_type\"), \"normal\") == 0", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("ch(\"baseBumpAndNormal_enable\") && strcmp(chs(\"baseBumpAndNormal_type\"), \"normal\") == 0", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("ch(\"baseBumpAndNormal_enable\") && strcmp(chs(\"baseBumpAndNormal_type\"), \"normal\") == 0", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /mat/principledshader1/shop_disable_displace_shader parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("shop_disable_displace_shader")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("!ch(\"dispInput_enable\") && !ch(\"dispTex_enable\") && !ch(\"dispNoise_enable\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("!ch(\"dispInput_enable\") && !ch(\"dispTex_enable\") && !ch(\"dispNoise_enable\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("!ch(\"dispInput_enable\") && !ch(\"dispTex_enable\") && !ch(\"dispNoise_enable\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("!ch(\"dispInput_enable\") && !ch(\"dispTex_enable\") && !ch(\"dispNoise_enable\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /mat/principledshader1/vm_displacebound parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/mat/principledshader1")
hou_parm = hou_node.parm("vm_displacebound")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("1.01*ch(\"dispInput_enable\")*ch(\"dispInput_max\") + ch(\"dispTex_enable\")*max(abs((1.0+ch(\"dispTex_offset\"))*ch(\"dispTex_scale\")), abs(ch(\"dispTex_offset\")*ch(\"dispTex_scale\"))) + ch(\"dispNoise_enable\")*abs(ch(\"dispNoise_amp\"))", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("1.01*ch(\"dispInput_enable\")*ch(\"dispInput_max\") + ch(\"dispTex_enable\")*max(abs((1.0+ch(\"dispTex_offset\"))*ch(\"dispTex_scale\")), abs(ch(\"dispTex_offset\")*ch(\"dispTex_scale\"))) + ch(\"dispNoise_enable\")*abs(ch(\"dispNoise_amp\"))", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("1.01*ch(\"dispInput_enable\")*ch(\"dispInput_max\") + ch(\"dispTex_enable\")*max(abs((1.0+ch(\"dispTex_offset\"))*ch(\"dispTex_scale\")), abs(ch(\"dispTex_offset\")*ch(\"dispTex_scale\"))) + ch(\"dispNoise_enable\")*abs(ch(\"dispNoise_amp\"))", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setExpression("1.01*ch(\"dispInput_enable\")*ch(\"dispInput_max\") + ch(\"dispTex_enable\")*max(abs((1.0+ch(\"dispTex_offset\"))*ch(\"dispTex_scale\")), abs(ch(\"dispTex_offset\")*ch(\"dispTex_scale\"))) + ch(\"dispNoise_enable\")*abs(ch(\"dispNoise_amp\"))", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolcount___", "176")
hou_node.setUserData("__inputgroup_Settings", "collapsed")
hou_node.setUserData("__inputgroup_Surface", "collapsed")
hou_node.setUserData("__inputgroup_Bump & Normals", "collapsed")
hou_node.setUserData("__inputgroup_Textures", "collapsed")
hou_node.setUserData("__inputgroup_Opacity", "collapsed")
hou_node.setUserData("___Version___", "")
hou_node.setUserData("__inputgroup_Displacement", "collapsed")
hou_node.setUserData("___toolid___", "convertGallery")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
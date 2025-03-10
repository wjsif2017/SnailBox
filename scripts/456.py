import json
import hou
import sn_callback


def bg_nodes(data):
    rel_nodes = []
    bg_dic = json.loads(data)
    for one in bg_dic:
        rel_node_path = one.get("relativetopath")
        if rel_node_path:
            node = hou.node(rel_node_path)
            if node:
                rel_nodes.append(node)
    return rel_nodes


def allnode(node, li=[]):
    for child in node.children():
        if child.isInsideLockedHDA():
            continue
        bg_userData = child.userData("backgroundimages")
        if bg_userData:
            rel_nodes = bg_nodes(bg_userData)
            if rel_nodes:
                li += rel_nodes
        allnode(child, li)
    return li


def reset_bg_event():
    try:
        all_bg_nodes = allnode(hou.node("/"))
        if all_bg_nodes:
            sn_callback.reset_node_bg_event(all_bg_nodes)
    except:
        hou.ui.setStatusMessage("SnailBox_Reset nodes background failed")


reset_bg_event()

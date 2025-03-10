from utils.allSetting import ALLSET
from utils.snailFun import *
from utils import fileThumb


def update_callback(**kwargs):
    try:
        node = kwargs.get("node")
        parm_name = kwargs.get("parm_name")
        node_name = node.name()
        node.removeAllEventCallbacks()
        h_version = float(ALLSET.h_version)
        if h_version < 20.5:
            call_fun2 = lambda **kwargs: node_changed_callback(
                **kwargs, old_name=node_name, parm_name=parm_name
            )
        else:
            call_fun2 = lambda **kwargs: node_changed_callback(**kwargs, parm_name=parm_name)
        node.addEventCallback(
            (
                hou.nodeEventType.NameChanged,
                hou.nodeEventType.BeingDeleted,
            ),
            call_fun2,
        )
        if parm_name:
            node.addParmCallback(parm_changed_callback, (parm_name,))
    except Exception as e:
        node = kwargs.get("node")
        msg = f"Snail_error_cb: update_callback {node} _ {e}"
        display_status(msg)


def reset_node_bg_event(nodes=[]):
    for node in nodes:
        try:
            filethumb = fileThumb.FileThumb(node=node)
            filethumb.reset_bg_event()
        except Exception as e:
            msg = f"Snail_error_cb: reset_node_bg_event {node} _ {e}"
            display_status(msg)


def node_changed_callback(**kwargs):
    try:
        event_type = kwargs.get("event_type")
        node = kwargs.get("node")
        if event_type == hou.nodeEventType.BeingDeleted:
            filethumb = fileThumb.FileThumb(node=node)
            filethumb.change_node_bg()
        elif event_type == hou.nodeEventType.NameChanged:
            old_name = kwargs.get("old_name")
            parm_name = kwargs.get("parm_name")
            new_path = node.path()
            old_path = new_path.rsplit("/", 1)[0] + "/" + old_name
            filethumb = fileThumb.FileThumb(node=node)
            filethumb.change_node_bg(old_path)
            update_callback(node=node, parm_name=parm_name)
    except Exception as e:
        node = kwargs.get("node")
        msg = f"Snail_error_cb: node_changed_callback {node} _ {e}"
        display_status(msg)
        node.removeAllEventCallbacks()


def parm_changed_callback(**kwargs):
    try:
        node = kwargs.get("node")
        parm_tuple = kwargs.get("parm_tuple")
        if not parm_tuple or not node:
            return
        filethumb = fileThumb.FileThumb(parm=parm_tuple[0])
        filethumb.update_node_bg()
    except Exception as e:
        node = kwargs.get("node")
        msg = f"Snail_error_cb: parm_changed_callback {node} _ {e}"
        display_status(msg)
        node.removeAllEventCallbacks()


def clear_node_bg(nodes=[]):
    nodes = hou.selectedNodes() if not nodes else []
    if not nodes:
        try:
            if ALLSET.language:
                msg = "你没有选择任何节点,将会删除所有当前界面所有背景图?"
            else:
                msg = "You have not selected any nodes, all backgroundImages on this network will be deleted?"
            res = hou.ui.displayMessage(msg, buttons=("OK", "Cancel"))
            if res == 1:
                return
            panetabs = [
                t
                for t in hou.ui.paneTabs()
                if t.type() == hou.paneTabType.NetworkEditor and t.isCurrentTab()
            ]
            if not panetabs:
                return
            parent_node = panetabs[0].pwd()
            parent_node.destroyUserData("backgroundimages")
        except Exception as e:
            display_status(f"Snail_error_cb: clear_node_bg _ {e}")
    else:
        for node in nodes:
            try:
                file_item = fileThumb.FileThumb(node=node)
                file_item.clear_node_bg()
            except Exception as e:
                display_status(f"Snail_error_cb: clear_node_bg {node} _ {e}")


def update_fileThumb():
    nodes = hou.selectedNodes()
    if not nodes:
        if ALLSET.language:
            msg = "请选择一个节点"
        else:
            msg = "Please select a node"
        hou.ui.displayMessage(msg)
        return
    else:
        for node in nodes:
            try:
                file_node = fileThumb.FileThumb(node=node, needParm=1)
                file_node.auto_update_node_bg()
            except Exception as e:
                display_status(f"Snail_error_cb: update_fileThumb {node} _ {e}")

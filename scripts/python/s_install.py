import hou
import os
import json


def h_version():
    h_v = hou.applicationVersion()
    h_v2 = ".".join(map(str, h_v[:2]))
    try:
        h_v3 = float(h_v2)
        return h_v3
    except:
        return 18.5


def write_json(s_path):
    try:
        pre_path = hou.getenv("HOUDINI_USER_PREF_DIR")
        j_path = os.path.join(pre_path, "packages")
        j_file = os.path.join(j_path, "SnailBox.json")
        os.makedirs(j_path, exist_ok=True)
        h_v = h_version()
        if h_v > 19.0:
            j_cont = {"enable": True, "env": [{"SnailBox": s_path}], "hpath": "$SnailBox"}
        else:
            j_cont = {"enable": True, "env": [{"SnailBox": s_path}], "path": "$SnailBox"}
        with open(j_file, "w", encoding="utf8") as f:
            json.dump(j_cont, f, indent=4)
        if h_v > 18.5:
            hou.ui.loadPackage(j_file)
        else:
            hou.ui.displayMessage(
                "Please restart houdini to load SnailBox and manually add shelf tool"
            )
            return False
        return True
    except:
        hou.ui.displayMessage("add SnailBox.json file to packages failed, please manually add it")


def add_shelf():
    try:
        s_shelve = hou.shelves.shelves().get("snail_box")
        if not s_shelve:
            raise Exception()
        shelf_set = hou.shelves.shelfSets().get("shelf_set_1")
        if not shelf_set:
            raise Exception()
        new_shelves = shelf_set.shelves() + (s_shelve,)
        shelf_set.setShelves(new_shelves)

        shelf_set2 = hou.shelves.shelfSets().get("solaris_1")
        if not shelf_set2:
            raise Exception()
        new_shelves2 = shelf_set2.shelves() + (s_shelve,)
        shelf_set2.setShelves(new_shelves2)
        return True
    except:
        hou.ui.displayMessage(
            "Auto add SnailBox shelf failed, please restart houdini and manually add it"
        )


def install_snailbox(s_path):
    res = write_json(s_path)
    if not res:
        return
    res2 = add_shelf()
    if not res2:
        return
    hou.ui.displayMessage("Install success!")

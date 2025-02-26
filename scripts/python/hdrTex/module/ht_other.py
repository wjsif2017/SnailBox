import os
import re
from utils.snailFun import *


class More_scan:
    def __init__(self, set_obj):
        self.set_obj = set_obj
        self.scan_types = {
            "Dirt_gumroad80": {
                "fn": self.g_80,
                "tip_zh": [
                    "*  原资源或作者地址：https://www.artstation.com/artwork/Kk1Ro",
                    "*  资源下载地址: https://www.cger.com/site/23018.html",
                ],
                "tip_en": [
                    "*  Author and assets site：https://www.artstation.com/artwork/Kk1Ro",
                ],
                "group_preset": {"ratio": 1.0, "level": "Default", "node": "H_Tex"},
            },
        }

    def g_80(self, index):

        path = self.set_obj.lib_list[index].get("path")
        if not path or not os.path.exists(path):
            return
        dic = {}
        group_preset = {"ratio": 1.0, "level": "Default", "node": "H_Env"}
        groups = {"All itmes": group_preset, "Ignore itmes": group_preset}
        other = {
            "DUST_big_01": "DUST_hard_01_preview.png",
            "FINGERPRINT_hard_01": "FINGERPRINT_hard_01_preview1.png",
            "DUST_small_001": "DUST_small_01_preview.png",
            "SCRATCHES_big_03": "SCRATCHES_big_03_preview.jpg",
            "DIRT_big_02": "DIRT_big_02_preview.jpg",
            "RUST_03": "RUST_03_soft_preview.png",
            "RUST_04": "RUST_04_soft_preview.png",
            "DIRT_big_01": "DIRT_01_big_base_preview.png",
        }
        nothumb = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file).replace("\\", "/")

                file_path_list = file_path.split("/")
                group = file_path_list[-2]
                if group not in groups:
                    groups[group] = group_preset

                name = file.split(".")[0]
                ext = file.split(".")[-1]
                if ext != "tif":
                    continue
                name_basic = re.findall(r"(\D+\d+)", file)[0]
                if name_basic == "TEAR_01":
                    continue
                if name_basic not in dic:
                    if name_basic in other:
                        thumbnail_name = other[name_basic]
                        thumb_path = file_path.replace(file, thumbnail_name)
                    else:
                        thumbnail_name1 = name_basic + "_preview.png"
                        thumbnail_name2 = name_basic + "_base_preview.png"
                        thumbnail_name3 = name_basic + "_hard_preview.png"
                        thumb_path1 = file_path.replace(file, thumbnail_name1)
                        thumb_path2 = file_path.replace(file, thumbnail_name2)
                        thumb_path3 = file_path.replace(file, thumbnail_name3)
                        if os.path.exists(thumb_path1):
                            thumb_path = thumb_path1
                        elif os.path.exists(thumb_path2):
                            thumb_path = thumb_path2
                        elif os.path.exists(thumb_path3):
                            thumb_path = thumb_path3
                        else:
                            thumb_path = ""
                            nothumb.append(name_basic)
                    one = {}
                    one["file_name"] = name_basic
                    one["group"] = group
                    one["path"] = file_path.replace(path, "SnailBox_asset_path")
                    one["thumbnail"] = thumb_path.replace(path, "SnailBox_asset_path")
                    one["ignore"] = 0
                    one["fav"] = 0
                    one["option"] = {}
                    one["o_len"] = 100
                    one["file_path"] = file_path
                    dic[name_basic] = one
                if name_basic != name:
                    option = name.replace(name_basic + "_", "")
                    if len(option) < one["o_len"]:
                        one["o_len"] = len(option)
                        one["path"] = file_path.replace(path, "SnailBox_asset_path")
                    dic[name_basic]["option"][option] = file_path.replace(
                        path, "SnailBox_asset_path"
                    )
        new_dic = {}
        for key, value in dic.items():
            file_path = value["file_path"]
            value.pop("o_len")
            value.pop("file_path")
            id = get_file_id2(file_path)
            if id:
                new_dic[id] = value
        return new_dic, groups

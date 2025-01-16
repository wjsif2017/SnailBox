import json
import os
from utils import *


class Setting:
    def __init__(self):
        self.script_pth = ""
        self.conf_file = ""
        self.localSet = "$HIP"
        self.jsonSet = ""
        self.formatDir = {}
        self.custom_node = {"Lop/reference::2.0": "filepath1"}
        self.cacheDisk = True
        self.lockedNode = True
        self.bypass = True
        self.packThumb = True

        self.init_data()

    def init_data(self):
        self.script_pth = ALLSET.sbox_path + "/scripts/python/projectPack"
        self.conf_file = ALLSET.conf_path + "/projectPack.json"
        self.jsonSet = self.readJson()
        if self.jsonSet:
            setList = ["formatDir", "bypass", "cacheDisk", "lockedNode", "packThumb"]
            for one in setList:
                try:
                    oneSet = self.jsonSet.get(one)
                    if oneSet != None:
                        setattr(self, one, oneSet)
                except Exception as e:
                    display_status(f"Snail_error_pp3: init_data _ {e}")
        else:
            self.set_default_conf()

    def readJson(self):
        try:
            if not os.path.exists(self.conf_file):
                return None
            with open(self.conf_file, "r", encoding="utf-8") as f:
                jsonSet = json.load(f)
                return jsonSet
        except Exception as e:
            display_status(f"Snail_error_pp3: readJson _ {e}")
            return None

    @property
    def formatList(self):
        try:
            fdir = self.formatDir
            flist = []
            for val in fdir.values():
                flist += val
            return flist
        except Exception as e:
            display_status(f"Snail_error_pp3: formatList _ {e}")

    @property
    def formatKeys(self):
        try:
            return list(self.formatDir.keys())
        except Exception as e:
            display_status(f"Snail_error_pp3: formatKeys _ {e}")

    def saveJson(self):
        try:
            setting = {
                "formatDir": self.formatDir,
                "cacheDisk": self.cacheDisk,
                "bypass": self.bypass,
                "lockedNode": self.lockedNode,
                "packThumb": self.packThumb,
            }
            if not os.path.exists(ALLSET.conf_path):
                os.makedirs(ALLSET.sbox_path + "/conf")
            with open(self.conf_file, "w", encoding="utf-8") as f:
                json.dump(setting, f)
        except Exception as e:
            display_status(f"Snail_error_pp3: saveJson _ {e}")

    def set_default_conf(self):
        self.formatDir = {
            "geo": [
                "obj",
                "bgeo",
                "geo",
                "rib",
                "dxf",
                "ply",
                "vdb",
                "stl",
                "lwo",
                "xyz",
                "fbx",
                "orbx",
                "rs",
                "mdd",
                "abc",
                "gltf",
                "glb",
            ],
            "usd": ["usd", "usdz", "usda", "usdc"],
            "tex": [
                "exr",
                "hdr",
                "png",
                "jpg",
                "jpeg",
                "pic",
                "psd",
                "tx",
                "tga",
                "tif",
                "tiff",
                "rat",
            ],
            "cache": ["bgeo.sc", "sc"],
            "hda": ["hda", "hdanc", "hdalc", "otl"],
            "misc": [
                "txt",
                "cube",
                "orbx",
                "proxy",
                "rs",
                "ies",
                "mp3",
                "wav",
                "aiff",
                "osl",
                "ai",
                "vrmesh",
                "vrscene",
                "eps",
                "pdf",
                "rstexbin",
            ],
        }


PPSET = Setting()

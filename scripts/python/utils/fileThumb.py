import glob
import hashlib
import json
import os
import re
from PIL import Image
import subprocess

import sn_callback
from .thumbScene import SC_VIEWER
from .allSetting import ALLSET
from .snailFun import *
import hou

MODEL_FORMATS = [
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
    "usd",
    "usdz",
    "usda",
    "fbx",
    "orbx",
    "rs",
    "mdd",
    "gltf",
    "glb",
    "abc",
    "sc",
]
SHOWVISIBLE = False  # 被隐藏的文件参数是否监控,显示背景


class FileThumb:  # 预览图对象
    def __init__(self, parm=None, node=None, needParm=0):
        self.unloadFromdisk = 0  # 缓存节点是否为未加载文件
        self.file_num = 0
        self.info_dict = {}
        self.img_ratio = 1
        self.parm = parm
        self.node = node
        self.needParm = needParm
        self.filePath = ""
        self.expandPath = ""
        self.thumb_path = ""

        self.initData()

    def initData(self):
        if self.parm:
            self.node = self.parm.node()  # 节点对象
        elif self.node:
            self.parm = self.find_file_parm() if self.needParm else None
        # if not self.parm or not self.node:
        #     sn_callback   node_changed_callback 清除thumb需要空节点
        #     raise Exception("FileThumb initData initNode failed")
        self.filePath = self.get_ref_value()  # 参数值字符串
        self.expandPath = self.get_expand_path()  # 绝对路径带序列参数
        self.thumb_path = self.get_thumb_id_path()

    @property
    def parm_path(self):
        if not self.parm:
            return
        else:
            return self.parm.path()

    @property
    def nodePath(self):
        return self.node.path()

    @property
    def parmName(self):
        if not self.parm:
            return
        else:
            return self.parm.name()

    @property
    def extension(self):
        return self.getExtension()

    @property
    def file_name(self):
        return self.get_file_name()

    @property
    def seq(self):
        return self.isSeq()

    @property
    def udim(self):
        return self.isUdim()

    @property
    def abs_path(self):
        return self.get_abs_path()

    @property
    def file_id(self):
        return self.get_file_id()

    @property
    def isCacheNode(self):
        return self.isFilecache()

    def find_file_parm(self):  # 先找是否有文件ref,没有再找是否有文件类型的参数
        parms = []
        parms = self.find_reference_parm()
        if not parms:  # 如果已有文件引用
            parms = self.get_other_parm()
            if not parms:
                parms = self.get_fileType_parm()
        if not parms:
            if ALLSET.language:
                msg = "没有找到文件或文件参数,可以添加一个文件后重试"
            else:
                msg = "Not found file or file parameter,you can add a file and try again"
            display_status(msg)
            return None
        elif len(parms) == 1:
            return parms[0]
        else:
            thumbParm_userData = self.get_thumbParm_userData()
            if thumbParm_userData:  # 如果有userData
                return self.node.parm(thumbParm_userData)
            else:
                parm_names = [parm.name() for parm in parms]
                if ALLSET.language:
                    msg = "检测到多个文件参数,请只选择一个文件参数"
                else:
                    msg = "Detected multiple file parameters, please choose only one file parameter"
                res = hou.ui.selectFromList(parm_names, message=msg)
                if res:
                    index = res[0]
                    self.node.setUserData("fileThumb_parm", parm_names[index])
                    return parms[index]
                else:
                    msg2 = (
                        "没有选择一个文件参数" if ALLSET.language else "No file parameter selected"
                    )
                    display_status(msg2)
                    return None

    def get_thumbParm_userData(self):
        return self.node.userData("fileThumb_parm")

    def get_node_refs(self):
        all_references = []
        try:
            all_references = self.node.fileReferences(recurse=False)
        except:
            # 20.0以前的版本vop节点没有node.filefreferences方法
            references = hou.fileReferences()
            for ref in references:
                if not ref[0]:
                    continue
                node = ref[0].node()
                if self.node == node:  # 如果是当前节点
                    all_references.append(ref)
        return all_references

    def find_reference_parm(self):  # 找到引用文件
        all_references = self.get_node_refs()
        refs = []
        for reference in all_references:
            try:
                if not reference[0] or reference[0] != reference[0].getReferencedParm():
                    continue
                node = reference[0].node()  # 节点对象
                if self.node != node:  # 如果是当前节点
                    continue
                if node.isInsideLockedHDA():  # 如果节点在锁定HDA里面
                    continue
                if self.getExtension(reference[1]) in ALLSET.img_formats:
                    refs.append(reference)
                elif self.getExtension(reference[1]) in MODEL_FORMATS:
                    refs.append(reference)
            except Exception as e:
                display_status(f"Snail_error_uft: find_reference_parm {reference[0]} _ {e}")
        if refs:  # 后面改为让用户选择
            ref_parms = [reference[0] for reference in refs]
            return ref_parms

    def get_fileType_parm(self):  # 找到fileType参数
        node = self.node
        parms = node.parms()
        file_parms = []
        for oneparm in parms:
            try:
                isVisible = oneparm.isVisible()  # 是否隐藏不可见参数
                if not SHOWVISIBLE and not isVisible:
                    continue
                tem = oneparm.parmTemplate()
                if tem.fileType().name() == "Image":
                    file_parms.append(oneparm)
            except Exception as e:
                display_status(f"Snail_error_uft: get_fileType_parm {oneparm} {e}")
        return file_parms

    def get_other_parm(self):  # 定义一些其它检测不到的参数
        node_type = self.node.type().name()
        if node_type == "reference::2.0":
            parm = self.node.parm("filepath1")
            return [parm]

    def get_other_value(self):  # 获取其它参数的值
        node_type = self.node.type().name()
        if node_type == "reference::2.0":
            other_value = self.parm.evalAsString()
            return other_value

    def get_fileCache_value(self, value):  # 缓存文件节点转换
        s = value
        if not s:
            return
        nodename = self.node.name()  # expandString不能解析$OS
        s = s.replace("$OS", nodename).replace("\\", "/")
        if self.isCacheNode == 2:
            enableversion = self.node.parm("enableversion").eval()  # 获取enableversion参数的值
            versionstr = self.node.parm("versionstr").eval()  # 获取versionstr参数的值
            basename = self.node.parm("basename").unexpandedString()
            cachedir = self.node.parm("basedir").unexpandedString()
            if enableversion:
                dir = cachedir + "/" + basename + "/" + versionstr + "/"
            else:
                dir = cachedir + "/" + basename + "/"
            s = dir + s
        return s

    def get_ref_value(self):  # 过滤refrence列表,没有节点会报错
        if not self.parm:
            return
        other_value = self.get_other_value()
        if other_value:
            return other_value
        all_references = self.get_node_refs()
        new_value = None
        for reference in all_references:
            if self.parm == reference[0]:
                new_value = reference[1]
                # 缓存文件节点转换
                new_value = self.get_fileCache_value(new_value)
        return new_value

    def get_thumb_ratio(self):
        thumb_path_abs = hou.text.expandString(self.thumb_path)  # 前面必须认证预览图存在
        if not os.path.exists(thumb_path_abs):  # 预览图存在
            return 1
        image = Image.open(thumb_path_abs)
        width, height = image.size
        ratio = width / height
        return round(ratio, 2)

    def get_file_id(self):  # 文件id,文件hash值
        md5_hash = hashlib.md5()
        if self.abs_path:
            # 读取文件并更新哈希对象
            with open(self.abs_path, "rb") as file:
                # 读取文件块，避免内存过于消耗
                for chunk in iter(lambda: file.read(4096), b""):
                    md5_hash.update(chunk)
        else:
            uni_text = self.filePath + self.nodePath
            md5_hash.update(uni_text.encode("utf-8"))
        return md5_hash.hexdigest()

    def getExtension(self, filePath=None):  # 获取文件后缀
        if not filePath:  # 如果没有传入文件路径
            filePath = self.filePath
        return os.path.splitext(filePath)[1].replace(".", "").lower()

    def get_thumb_path2(self):  # 先查看节点上是否有CachedUserData,查看update值需要自动更新
        node_thumb = self.node.cachedUserData("sn_thumb")  # cached
        thumb_update = self.node.userData("sn_thumb_update")  # update
        if not node_thumb and not thumb_update:  # 0 没有cached,且没有update
            self.node.removeAllEventCallbacks()
            return None
        elif node_thumb:  # 1 有cached
            self.clear_thumb_userData()  # 清除旧的cachedUserData
            node_thumb_excited = os.path.exists(hou.text.expandString(node_thumb))
            if node_thumb_excited:  # 判断是否存在
                self.thumb_path = node_thumb
                return node_thumb
            else:
                return None
        elif thumb_update:  # updateq 且为vuser
            self.reset_bg_event()
            return self.thumbnail
        else:
            return None

    def clear_thumb_userData(self):  # 清空CacheduserData,每次生成预览图,就会清空
        try:
            self.node.destroyCachedUserData("sn_thumb")  # 19.5以前的版本不支持第三个参数
        except:
            pass

    def update_node_bg(self):  # 0,生成背景图,1清除预览图
        # if not self.parm:
        #     return
        node = self.node
        image = {}
        thumbnail = self.get_thumb_path2()
        if thumbnail:  # 不存在预览图,就会删除已经有的预览图
            category = node.type().category().name()
            image["path"] = thumbnail
            h_node_type = ["Object", "Lop", "Sop", "Top"]  # 横向节点
            thumb_ratio = self.get_thumb_ratio()
            h = round(1 / thumb_ratio, 1)
            if category in h_node_type:
                image["rect"] = [1.1, 0.1, 2.1, 0.1 + h]
            else:
                image["rect"] = [0.3, 0.3, 1.3, 0.3 + h]
            image["relativetopath"] = self.nodePath
        self.update_bg_userData(image)

    def auto_update_node_bg(self):  # 自动更新节点背景
        if ALLSET.is_vuser:
            self.node.setUserData("sn_thumb_update", self.parmName)
            self.destroyUserData("fileThumb_parm")
            self.update_node_bg()
        else:
            self.destroyUserData("sn_thumb_update")

    def destroyUserData(self, name):
        try:
            # self.node.destroyUserData(name,0)
            self.node.destroyUserData(name)  # 19.5以前的版本不支持第三个参数
        except:
            pass

    def clear_node_bg(self):  # 关闭自动预览图并清除
        self.destroyUserData("sn_thumb_update")
        self.destroyUserData("fileThumb_parm")
        self.node.removeAllEventCallbacks()
        self.update_bg_userData()

    def change_node_bg(self, old_node_path=None):  # 改名或删除节点时更新背景
        self.update_bg_userData(old_node_path=old_node_path)

    def update_bg_userData(self, image=None, old_node_path=None):  # 更新节点背景UserData
        node = self.node
        parent_node = node.parent()
        user_data_json = parent_node.userData("backgroundimages")
        if not user_data_json:  # 如果本身没有userData
            user_data = []
        else:
            user_data = json.loads(user_data_json)
            for one in user_data:  # 删除已有的预览图
                if not one:  # 空字典
                    user_data.remove(one)
                elif "relativetopath" not in one:  # 如果没有path,跳过
                    continue
                elif old_node_path and one["relativetopath"] == old_node_path:  # 更换bg
                    one["relativetopath"] = self.nodePath
                elif one["relativetopath"] == self.nodePath:  # 删除bg,只保留一个
                    user_data.remove(one)
        if image:
            user_data.append(image)
        if user_data:
            new_json = json.dumps(user_data)
            parent_node.setUserData("backgroundimages", new_json)
        else:
            try:
                parent_node.destroyUserData("backgroundimages")
            except:
                pass

    @property
    def thumbnail(self):  # 返回预览图
        if not self.abs_path:
            display_status(f"Snail_error_uft: thumbnail {self.parm} _ Path_error")
            return None
        thumb_path_abs = hou.text.expandString(self.thumb_path)
        if os.path.exists(thumb_path_abs):
            return self.thumb_path
        else:
            res = self.create_thumbnail()
            if res:
                return self.thumb_path
            else:
                return None

    def create_thumbnail(self):  # 生成预览图(图片和节点)
        node_category = self.node.type().category().name()
        if self.extension in ALLSET.img_formats:
            res = self.create_img_thumbnail()
            return res
        elif node_category in ["Object", "Sop", "Lop", "Dop"]:
            res = self.create_node_thumbnail()
            return res
        else:
            return False

    def get_thumb_id_path(self):  # thumb_id 预览图路径
        if not self.parm or not self.abs_path:
            return None
        thumb_folder = "$HIP/thumbnail"
        thumb_folder_abs = hou.text.expandString(thumb_folder)
        if not os.path.exists(thumb_folder_abs):  # 创建预览图文件夹
            os.makedirs(thumb_folder_abs)
        thumb_path = f"$HIP/thumbnail/spp_{self.file_id}.jpg"
        return thumb_path

    def create_img_thumbnail(self):  # 生成图片预览图
        try:
            thumb_file_abs = hou.text.expandString(self.thumb_path)
            folder = os.path.dirname(thumb_file_abs)
            if not os.path.exists(folder):
                os.makedirs(folder)
            if not self.info_dict:
                self.info_dict = self.file_info  # 得到尺寸
            thumb_width = 512
            thumb_height = int(512 / self.img_ratio)
            res2 = subprocess.Popen(
                [
                    "icp",
                    "-r",
                    str(thumb_width),
                    str(thumb_height),
                    "-g",
                    "auto",
                    self.abs_path,
                    thumb_file_abs,
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            stdout_data, stderr_data = res2.communicate()
            info = stdout_data.decode("utf-8")
            error = stderr_data.decode("utf-8")
            if error:
                display_status(f"Snail_info_uft: create_img_thumbnail {self.parm} _ {error}")
            return True
        except Exception as e:
            display_status(f"Snail_error_uft: create_img_thumbnail {self.parm} _ {e}")
            return False

    def solo_node(self, show=0):  # 跳转并独显当前节点 0 不显示win, 1显示 2 默认不改变
        try:
            sc_tab = SC_VIEWER.get_sc_tab(show)
            if not sc_tab:
                return
            node_cat = self.node.type().category().name()
            node = hou.node("/obj/SnailBox_thumb")
            dis_node = hou.node("/obj/SnailBox_thumb/SnailBox_view/output0")
            if not dis_node:
                return
            if node_cat not in ["Object", "Sop", "Lop", "Dop"] or not self.abs_path:
                if ALLSET.language:
                    msg = "此资产不支持查看"
                else:
                    msg = "This asset does not support viewing"
                hou.ui.displayMessage(msg)
                return
            elif node_cat == "Lop":
                node.parm("input").set(2)
                node.parm("objpath1").set(self.nodePath)
            else:
                node.parm("input").set(1)
                node.parm("objpath1").set(self.nodePath)
            # 跳转到当前节点,放前面不能很好的刷新 # 此函数很容易引起界面崩溃
            sc_tab.setCurrentNode(dis_node)
            sc_view = sc_tab.curViewport()  # 获取当前视口
            sc_view.frameSelected()  # 居中
            return sc_tab
        except Exception as e:
            display_status(f"Snail_error_uft: solo_node {self.parm} _ {e}")

    def create_node_thumbnail(self):  # 生成节点预览图
        sc_tab = self.solo_node()
        if not sc_tab:
            return
        sc_flip_set = sc_tab.flipbookSettings()
        sc_flip_set.output(self.thumb_path)
        sc_flip_set.frameRange((1, 1))
        sc_flip_set.resolution((512, 512))
        sc_flip_set.outputToMPlay(0)
        sc_tab.flipbook()
        self.node.setCurrent(1, 1)
        sc_tab.close()
        thumb_node = hou.node("/obj/SnailBox_thumb")
        thumb_node.parm("input").set(0)
        return True

    def get_img_info(self):  # 获取图片信息
        file = self.abs_path
        if not file or not os.path.exists(file):
            return
        res2 = subprocess.Popen(
            ["iinfo", "-b", file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        stdout_data, stderr_data = res2.communicate()
        info = stdout_data.decode("utf-8")
        error = stderr_data.decode("utf-8")
        if error:
            hou.ui.displayMessage(str(error))
        pattern = r"\s\((\w+)\sformat\)\nResolution:\s+(.+?)\n.*?Data:\s+(.+?)\n.*?Color\sModel:\s+(.+?)\n"
        s_res = re.search(pattern, info, flags=re.DOTALL)
        if not s_res:
            return
        format, resolution, channel_depth, color_model = s_res.groups()
        if "A:\n" in info:
            color_model = "RGBA"
        return {
            "format": format,
            "resolution": resolution,
            "channel_depth": channel_depth,
            "color_model": color_model,
        }

    def get_file_size(self):  # 获取文件大小
        file = self.abs_path
        if not file or not os.path.exists(file):
            return
        size = os.path.getsize(file) / 1024
        if size < 1024:
            size_str = str(round(size, 2)) + "KB"
        else:
            size_str = str(round(size / 1024, 2)) + "MB"
        return size_str

    @property
    def file_info(self):  # 获取文件信息
        if self.info_dict:
            return self.info_dict
        info_dict = {}
        try:
            info_dict["Name"] = (
                self.file_name if self.file_num < 2 else f"{self.file_name} ( {self.file_num} )"
            )
            info_dict["Node"] = self.nodePath
            file_size = self.get_file_size()
            info_dict["Size"] = file_size if file_size else "Not Found"
            if self.extension in ALLSET.img_formats:
                img_info = self.get_img_info()
                if img_info:
                    resolution = img_info["resolution"]
                    info_dict["Res"] = resolution
                    res_width = int(resolution.split(" x ")[0])
                    res_height = int(resolution.split(" x ")[1])
                    self.img_ratio = round(res_width / res_height, 2)
                    info_dict["Depth"] = img_info["color_model"] + "  " + img_info["channel_depth"]
        except Exception as e:
            display_status(f"Snail_error_uft: get_file_info {self.parm} _ {e}")
        finally:
            self.info_dict = info_dict
            return info_dict

    def isFilecache(self):  # 是否为缓存节点
        nodeTypeName = self.node.type().name()

        if "filecache" in nodeTypeName:
            if not self.node.parm("loadfromdisk").eval():
                self.unloadFromdisk = 1
            if self.node.parm("filemethod").eval():
                return 1
            else:
                return 2
        else:
            return 0

    def get_expand_path(self):  # 绝对化路径 两种fileCache $F 和 UDIM
        s = self.filePath
        if not s:
            return
        g = re.match(r"(.*)(\$F\d*)(.*)", s)
        if g:
            s2 = hou.text.expandString(g.group(1)) + g.group(2) + hou.text.expandString(g.group(3))
        else:
            s2 = hou.text.expandString(s)
        return s2

    def get_file_name(self):  # 文件名 xx.jpg
        return os.path.basename(self.expandPath)

    def isSeq(self):  # 是否序列文件
        if not self.expandPath:
            return
        match = re.search(r"(\$F\d*)", self.expandPath)
        if match:  # 检测是否含有$F
            s = re.sub(r"(\$F\d*)", "*", self.expandPath)
            return s
        else:
            return False

    def isUdim(self):  # 判断材质文件是否UDIM
        if not self.expandPath:
            return
        match = re.search(r"(%\(UDIM\)d)|(<UDIM>)", self.expandPath)
        if match:  # 检测是否含有$F
            s = re.sub(r"(%\(UDIM\)d)|(<UDIM>)", "*", self.expandPath)
            return s
        else:
            return False

    def get_abs_path(self):  # 判断是否为excited文件
        if not self.expandPath:
            return
        if self.seq:  # 含有$F序列处理,先判断是否为序列文件
            files = glob.glob(self.seq)  # 根据文件路径中的*来匹配文件序列
            if not len(files):
                return False
            else:
                self.file_num = len(files)
                return files[0].replace("\\", "/")
        elif self.udim:  # 含有$F序列处理,先判断是否为序列文件
            files = glob.glob(self.udim)  # 根据文件路径中的*来匹配文件序列
            if not len(files):
                return False
            else:
                self.file_num = len(files)
                return files[0].replace("\\", "/")
        else:  # 非序列文件判断是否存在
            # 测试expandString展开OS并不准确,新filecache节点并不合并两个参数
            if not os.path.exists(self.expandPath):
                return False
            else:
                self.file_num = 1
                return self.expandPath

    def get_auto_parm(self):
        try:
            parm_name = self.node.userData("sn_thumb_update")
            return parm_name
        except:
            return

    def reset_bg_event(self):
        parm_name = self.get_auto_parm()
        sn_callback.update_callback(node=self.node, parm_name=parm_name)


class ImgThumb:  # 预览图对象
    def __init__(self):
        self.path = ""
        self.ex_path = ""
        self.thumbnail = ""
        self.ex_thumb = ""
        self.thumb_width = 512
        self.thumb_height = 512
        self.img_ratio = 1
        self.is_seq = False
        self.file_num = 1
        self.info_dict = {}

    def init_data(self, path, thumb, width=None, height=None):
        self.path = path
        self.get_ex_path()
        if thumb:
            self.thumbnail = thumb
        else:
            thumb_id = get_file_id2(self.abs_path)
            thumb_path = f"$HIP/thumbnail/{thumb_id}.jpg"
            self.thumbnail = thumb_path
        if width:
            self.thumb_width = int(width)
        else:
            self.thumb_width = ALLSET.thumb_width
        if height:
            self.thumb_height = int(height)
        else:
            try:
                self.get_file_info()
                self.thumb_height = int(self.thumb_width / self.img_ratio)
            except:
                self.thumb_height = ALLSET.thumb_width

    @property
    def file_dict_p(self):
        if not self.info_dict:
            self.info_dict = self.get_file_info()
        return self.info_dict

    @property
    def file_id(self):
        return get_file_id2(self.abs_path)

    @property
    def abs_path(self):
        return self.get_abs_path()

    @property
    def abs_thumb(self):
        self.get_ex_thumb()
        return self.get_abs_thumb()

    @property
    def ext(self):
        return self.get_ext()

    @property
    def file_name(self):
        return self.get_file_name()

    def get_thumb_ratio(self):  # 前面必须认证预览图存在
        if not self.abs_thumb:
            return 1
        try:
            with Image.open(self.abs_thumb) as image:
                width, height = image.size
                return round(width / height, 2)
        except Exception as e:
            display_status(f"Snail_error_ht2: get_thumb_ratio {self.abs_thumb} - {e}")
            return 1

    def get_ext(self):  # 获取文件后缀
        if not self.path:
            return
        ext = os.path.splitext(self.path)[-1].lstrip(".").lower()
        return ext

    def get_thumb(self):  # 生成图片预览图
        abs_path = self.abs_path
        ex_thumb = self.get_ex_thumb()
        width = self.thumb_width
        height = self.thumb_height
        if not abs_path or not ex_thumb:
            return "", self.info_dict
        res = self.create_img_thumb(abs_path, ex_thumb, width, height)
        if res:
            return ex_thumb, self.info_dict

    def create_img_thumb(self, abs_path, ex_thumb, width=512, height=512):
        if not abs_path or not ex_thumb or not width or not height:
            return False
        try:
            folder = os.path.dirname(ex_thumb)
            if not os.path.exists(folder):
                os.makedirs(folder)
            res2 = subprocess.Popen(
                [
                    "icp",
                    "-r",
                    str(width),
                    str(height),
                    "-g",
                    "auto",
                    abs_path,
                    ex_thumb,
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            stdout_data, stderr_data = res2.communicate()
            info = stdout_data.decode("utf-8")
            error = stderr_data.decode("utf-8")
            if error:
                display_status(f"Snail_error_uft2: create_img_thumbnail {abs_path} _ {error}", 1)
            return True
        except Exception as e:
            display_status(f"Snail_error_uft2: create_img_thumbnail {abs_path} _ {e}", 1)
            return False

    def get_img_info(self):  # 获取图片信息
        file = self.abs_path
        if not file:
            return
        res2 = subprocess.Popen(
            ["iinfo", "-b", file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        stdout_data, stderr_data = res2.communicate()
        info = stdout_data.decode("utf-8")
        error = stderr_data.decode("utf-8")
        if error:
            display_status(f"Snail_error_ht2: get_img_info {self.path} _ {error}", 1)
            return
        pattern = r"\s\((\w+)\sformat\)\nResolution:\s+(.+?)\n.*?Data:\s+(.+?)\n.*?Color\sModel:\s+(.+?)\n"
        s_res = re.search(pattern, info, flags=re.DOTALL)
        if not s_res:
            return
        format, resolution, channel_depth, color_model = s_res.groups()
        if "A:\n" in info:
            color_model = "RGBA"
        return {
            "format": format,
            "resolution": resolution,
            "channel_depth": channel_depth,
            "color_model": color_model,
        }

    def get_file_size(self):  # 获取文件大小
        file = self.abs_path
        if not file:
            return
        size = os.path.getsize(file) / 1024
        if size < 1024:
            size_str = str(round(size, 2)) + "KB"
        else:
            size_str = str(round(size / 1024, 2)) + "MB"
        return size_str

    def get_file_info(self):  # 获取文件信息
        info_dict = {}
        try:
            name = self.get_file_name()
            info_dict["Name"] = name if self.file_num < 2 else f"{name} ( {self.file_num} )"
            file_size = self.get_file_size()
            info_dict["Size"] = file_size if file_size else "Not Found"
            if self.ext and self.ext in ALLSET.img_formats:
                img_info = self.get_img_info()
                if not img_info:
                    return
                resolution = img_info["resolution"]
                info_dict["Resolution"] = resolution
                res_width = int(resolution.split(" x ")[0])
                res_height = int(resolution.split(" x ")[1])
                self.img_ratio = round(res_width / res_height, 2)
                info_dict["Depth"] = img_info["color_model"] + "  " + img_info["channel_depth"]
        except Exception as e:
            display_status(f"Snail_error_uft2: get_file_info {self.path} _ {e}", 1)
        finally:
            self.info_dict = info_dict
            return info_dict

    def get_file_info2(self, path):  # 获取文件信息
        self.path = path
        self.get_ex_path()
        info_dict = self.get_file_info()
        return info_dict

    def get_file_name(self):  # 文件名 xx.jpg
        return os.path.basename(self.ex_path)

    def get_ex_path(self):  # 每个库重新定义
        if self.path:
            self.ex_path = hou.text.expandString(self.path)
        else:
            self.ex_path = ""
        return self.ex_path

    def get_ex_thumb(self):  # 每个库重新定义
        if self.thumbnail:
            self.ex_thumb = hou.text.expandString(self.thumbnail)
        else:
            self.ex_thumb = ""
        return self.ex_thumb

    def get_abs_path(self):  # 判断是否为excited文件
        ex_path = self.ex_path
        if not ex_path:
            return
        if self.is_seq:  # 含有$F序列处理,先判断是否为序列文件
            files = glob.glob(ex_path)  # 根据文件路径中的*来匹配文件序列
            if not len(files):
                return
            else:
                self.file_num = len(files)
                abs_path = files[0].replace("\\", "/")
                return abs_path
        else:
            if os.path.exists(ex_path):
                return ex_path

    def get_abs_thumb(self):  # 判断是否为excited文件
        if not self.ex_thumb:
            return
        if os.path.exists(self.ex_thumb):
            return self.ex_thumb

    def update_thumb(self, thumb):  # 更新缩略图
        self.thumbnail = thumb
        self.ex_thumb = self.get_ex_thumb()

    def open_file_explorer(self):
        hou.ui.showInFileBrowser(self.abs_path)

    def del_item(self, thumb=0):  # 删除文件
        try:
            if self.abs_path:
                os.remove(self.abs_path)
            if thumb and self.abs_thumb:
                os.remove(self.abs_thumb)
        except Exception as e:
            display_status(f"Snail_error_ht2: del_item {self.abs_path} _ {e}", 1)
            return

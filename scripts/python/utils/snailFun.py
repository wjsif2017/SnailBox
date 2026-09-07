"""
SnailBox 公共工具函数模块

本模块提供各种通用的工具函数，供其他模块使用。

功能分类:
    - 状态消息: display_status
    - 文件操作: get_file_id, get_file_size, get_file_ext, copy_file, read_file, save_file, save_fileB
    - JSON 操作: read_json, save_json
    - 图片转换: convert_imga, convert_imgb
    - 节点数据: get_node_userData, set_node_userData
    - 路径检查: check_path, _increment_path
    - ID 生成: id_check
"""

import json
import os
import shutil
import subprocess
import threading
import hashlib
import hou
from PIL import Image

# 调试模式开关: 开发目录(SnailBox_dev)或设置环境变量 SNAILBOX_DEBUG=1 时打印到控制台;
# 发布版默认 False, display_status 走 Houdini 状态栏而不是只输出到控制台
_DEV_RUN = os.environ.get("SNAILBOX_DEBUG", "") == "1" or "SnailBox_dev" in __file__.replace("\\", "/")
SNAIL_DBUG = _DEV_RUN


# ============================================================================
# 状态消息
# ============================================================================


def display_status(message, display=0, severity_level=1):
    """显示状态栏消息

    Args:
        message: 消息文本
        display: 0=正常显示, 1=强制打印到控制台
        severity_level: 严重程度 (0=Message, 1=Important, 2=Warning, 3=Error, 4=Fatal)
    """
    if SNAIL_DBUG or display:
        print(message)
        return

    severity_dict = {
        0: hou.severityType.Message,
        1: hou.severityType.ImportantMessage,
        2: hou.severityType.Warning,
        3: hou.severityType.Error,
        4: hou.severityType.Fatal,
    }
    severity = severity_dict[severity_level]
    hou.ui.setStatusMessage(message, severity=severity)

    def clear_status_message():
        hou.ui.setStatusMessage("")

    threading.Timer(10, clear_status_message).start()


# ============================================================================
# ID 生成
# ============================================================================


def id_check(id, all_item):
    """检查 ID 是否重复，如有重复则生成唯一 ID

    Args:
        id: 原始 ID
        all_item: 现有 ID 列表

    Returns:
        str: 唯一的 ID，重复则添加后缀 (如 id_0001)
    """
    if id in all_item:
        for i in range(1, 1000):
            new_id = id + "_%04d" % i
            if new_id not in all_item:
                break
        return new_id
    else:
        return id


# ============================================================================
# 文件操作
# ============================================================================


def get_file_id(abs_path):
    """获取文件的 MD5 哈希值 (完整文件)

    Args:
        abs_path: 文件绝对路径

    Returns:
        str: MD5 十六进制字符串，失败返回 None
    """
    if not abs_path or not os.path.exists(abs_path):
        return None
    try:
        md5_hash = hashlib.md5()
        with open(abs_path, "rb") as file:
            # 读取文件块，避免内存过于消耗
            for chunk in iter(lambda: file.read(4096), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except Exception as e:
        display_status(f"Snail_error_usf: get_file_id {abs_path} _ {e}")
        return None


def get_file_id2(abs_path):
    """获取文件的 MD5 哈希值 (前后 4KB)

    Args:
        abs_path: 文件绝对路径

    Returns:
        str: MD5 十六进制字符串，失败返回 None
    """
    if not abs_path or not os.path.exists(abs_path):
        return None
    try:
        md5_hash = hashlib.md5()
        with open(abs_path, "rb") as file:
            head = file.read(4096)
            md5_hash.update(head)
            file.seek(-4096, 2)
            tail = file.read(4096)
            md5_hash.update(tail)
        return md5_hash.hexdigest()
    except Exception as e:
        display_status(f"Snail_error_usf: get_file_id {abs_path} _ {e}")
        return None


def get_file_size(abs_path):
    """获取文件大小 (KB)

    Args:
        abs_path: 文件绝对路径

    Returns:
        int: 文件大小 (KB)，失败返回 None
    """
    if not abs_path or not os.path.exists(abs_path):
        return None
    try:
        size = int(os.path.getsize(abs_path) / 1024)
        return size
    except Exception as e:
        display_status(f"Snail_error_usf: get_file_size {abs_path} _ {e}")
        return None


def get_file_ext(abs_path, point=False):
    """获取文件扩展名

    Args:
        abs_path: 文件路径
        point: True=包含点号, False=不包含点号

    Returns:
        str: 小写的扩展名，失败返回 None
    """
    if not abs_path:
        return None
    try:
        ext = os.path.splitext(abs_path)[-1]
        if not point:
            ext = ext.strip(".")
        ext = ext.lower()
        return ext
    except Exception as e:
        display_status(f"Snail_error_usf: get_file_ext {abs_path} _ {e}", 1)
        return None


def copy_file(src_file, dst_file):
    """复制文件

    Args:
        src_file: 源文件路径
        dst_file: 目标文件路径

    Returns:
        bool: 成功返回 True，失败返回 False
    """
    if not src_file or not dst_file:
        return False

    try:
        if not os.path.isfile(src_file):
            return False
        dst_path = os.path.dirname(dst_file)
        if not os.path.isdir(dst_path):
            os.makedirs(dst_path)
        shutil.copyfile(src_file, dst_file)
        return True
    except Exception as e:
        display_status(f"Snail_error_usf: copy_file {src_file} _ {e}", 1)
        return False


def read_file(abs_path):
    """读取文本文件

    Args:
        abs_path: 文件绝对路径

    Returns:
        str: 文件内容，失败返回 None
    """
    if not abs_path:
        return None
    try:
        if not os.path.isfile(abs_path):
            return None
        with open(abs_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        display_status(f"Snail_error_usf: read_file {abs_path} _ {e}", 1)
        return None


def save_file(data, abs_path):
    """保存文本文件

    Args:
        data: 文本内容
        abs_path: 文件绝对路径

    Returns:
        bool: 成功返回 True，失败返回 None
    """
    if not data or not abs_path:
        return None
    try:
        dir = os.path.dirname(abs_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(data)
        return True
    except Exception as e:
        display_status(f"Snail_error_usf: save_file {abs_path} _ {e}", 1)
        return None

def read_fileB(abs_path):
    """读取二进制文件

    Args:
        abs_path: 文件绝对路径

    Returns:
        bytes: 文件内容，失败返回 None
    """
    if not abs_path:
        return None
    try:
        if not os.path.isfile(abs_path):
            return None
        with open(abs_path, "rb") as f:
            return f.read()
    except Exception as e:
        display_status(f"Snail_error_usf: read_fileB {abs_path} _ {e}", 1)
        return None


def save_fileB(data, abs_path):
    """保存二进制文件

    Args:
        data: 二进制内容
        abs_path: 文件绝对路径

    Returns:
        bool: 成功返回 True，失败返回 None
    """
    if not data or not abs_path:
        return None
    try:
        dir = os.path.dirname(abs_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(abs_path, "wb") as f:
            f.write(data)
        return True
    except Exception as e:
        display_status(f"Snail_error_usf: save_fileB {abs_path} _ {e}", 1)
        return None


# ============================================================================
# JSON 操作
# ============================================================================


def read_json(abs_path):
    """读取 JSON 文件

    Args:
        abs_path: 文件绝对路径

    Returns:
        dict/list: 解析后的数据，失败返回 None
    """
    if not abs_path:
        return None
    try:
        if not os.path.isfile(abs_path):
            return None
        with open(abs_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        display_status(f"Snail_error_usf: read_json {abs_path} _ {e}", 1)
        return None


def save_json(data, abs_path):
    """保存 JSON 文件

    Args:
        data: 要保存的数据 (可 JSON 序列化)
        abs_path: 文件绝对路径

    Returns:
        bool: 成功返回 True，失败返回 None
    """
    if not data or not abs_path:
        return None
    try:
        dir = os.path.dirname(abs_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(abs_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        return True
    except Exception as e:
        display_status(f"Snail_error_usf: save_json {abs_path} _ {e}", 1)
        return None


# ============================================================================
# 图片转换
# ============================================================================


def convert_imga(src_img, dst_img, width=512, height=512):
    """使用 PIL 转换图片

    Args:
        src_img: 源图片路径
        dst_img: 目标图片路径
        width: 目标宽度
        height: 目标高度

    Returns:
        bool: 成功返回 True，失败返回 None
    """
    support_exts = [
        "bmp", "dib", "gif", "tif", "tiff", "jfif", "jpe", "jpg", "jpeg",
        "pbm", "pgm", "ppm", "pnm", "png", "apng",
    ]
    if not src_img or not dst_img:
        return None
    try:
        ext = get_file_ext(src_img)
        if not ext or ext not in support_exts:
            return None
        img = Image.open(src_img)
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(dst_img)
        return True
    except Exception as e:
        display_status(f"Snail_error_usf: convert_imga {src_img} _ {e}", 1)
        return False


def convert_imgb(src_img, dst_img, width=512, height=512):
    """使用 icp 工具转换图片

    Args:
        src_img: 源图片路径
        dst_img: 目标图片路径
        width: 目标宽度
        height: 目标高度

    Returns:
        bool: 成功返回 True，失败返回 False
    """
    support_exts = [
        "jpg", "jpeg", "png", "tif", "tiff", "exr", "hdr", "psd", "tx",
        "tga", "rat", "xbm", "xpm", "ppm", "svg", "pbm", "pdf",
        "bmp", "cur", "gif", "icns", "ico",
    ]
    if not src_img or not dst_img or not width or not height:
        return False
    try:
        ext = get_file_ext(src_img)
        if not ext:
            return False
        if ext not in support_exts:
            msg = f"thumbnail don't supports {ext} format"
            hou.ui.displayMessage(msg)
            return False
        folder = os.path.dirname(dst_img)
        if not os.path.exists(folder):
            os.makedirs(folder)
        res2 = subprocess.Popen(
            ["icp", "-r", str(width), str(height), "-g", "auto", src_img, dst_img],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        stdout_data, stderr_data = res2.communicate()
        if stderr_data:
            display_status(f"Snail_error_usf: convert_imgb {src_img} _ {stderr_data.decode()}", 1)
        return True
    except Exception as e:
        display_status(f"Snail_error_usf: convert_imgb {src_img} _ {e}", 1)
        return False


# ============================================================================
# 节点数据操作
# ============================================================================


def get_node_userData(node_path, name, option=0):
    """读取节点用户自定义数据

    Args:
        node_path: 节点路径 (如 "/obj/geo1")
        name: 数据键名
        option: 0=UserData (保存到 hip), 1=CachedUserData (临时)

    Returns:
        dict: 解析后的数据字典，无数据或失败返回空字典
    """
    if not node_path:
        return {}
    node = hou.node(node_path)
    if not node:
        return {}

    try:
        if option == 0:
            data_str = node.userData(name)
        else:
            data_str = node.cachedUserData(name)

        if not data_str:
            return {}
        return json.loads(data_str)
    except Exception as e:
        display_status(f"Snail_error_usf: get_node_userData {node_path} _ {e}", 1)
        return {}


def set_node_userData(node_path, name, value, option=0):
    """设置节点用户自定义数据

    Args:
        node_path: 节点路径 (如 "/obj/geo1")
        name: 数据键名
        value: 要存储的数据 (可 JSON 序列化)
        option: 0=UserData (保存到 hip), 1=CachedUserData (临时)

    Returns:
        bool: 成功返回 True，失败返回 False
    """
    if not node_path:
        return False
    node = hou.node(node_path)
    if not node:
        return False

    try:
        data_str = json.dumps(value, ensure_ascii=False)
        if option == 0:
            node.setUserData(name, data_str)
        else:
            node.setCachedUserData(name, data_str)
        return True
    except Exception as e:
        display_status(f"Snail_error_usf: set_node_userData {node_path} _ {e}", 1)
        return False


# ============================================================================
# 路径检查
# ============================================================================


def check_path(file_path, option=0, expanded=True):
    """检查文件/文件夹是否存在并处理冲突

    Args:
        file_path: 文件路径（可包含环境变量如 $HIP）
        option: 0=默认覆盖, 1=弹框询问（覆盖/增量保存/取消）
        expanded: True=返回展开后的路径, False=返回原始路径

    Returns:
        str: 最终路径（增量保存返回新路径），取消返回 None
    """
    if not file_path:
        return file_path

    # 展开环境变量
    expanded_path = hou.text.expandString(file_path)

    # 路径不存在，创建后返回
    if not os.path.exists(expanded_path):
        # 判断是文件还是文件夹
        if os.path.splitext(os.path.basename(expanded_path))[1]:
            # 是文件：创建父目录
            dir_path = os.path.dirname(expanded_path)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
        else:
            # 是文件夹：直接创建
            os.makedirs(expanded_path, exist_ok=True)
        return expanded_path if expanded else file_path

    # 路径存在
    if option == 0:
        return expanded_path if expanded else file_path

    # option=1: 弹框询问
    if option == 1:
        res = hou.ui.displayMessage(
            f"File already exists:\n{file_path}\n\nWhat would you like to do?",
            buttons=("Overwrite", "Increment Save", "Cancel"),
            default_choice=2,
            close_choice=2
        )

        if res == 0:  # Overwrite
            return expanded_path if expanded else file_path
        elif res == 1:  # Increment Save
            new_path = _increment_path(file_path)
            return new_path
        else:  # Cancel
            return None

    return expanded_path if expanded else file_path


def _increment_path(path):
    """为路径添加增量后缀 _v1, _v2, ...

    Args:
        path: 原始路径（可包含环境变量如 $HIP）

    Returns:
        str: 带增量后缀的新路径
    """
    # 分离目录、文件名和扩展名
    dir_path = os.path.dirname(path)
    basename = os.path.basename(path)
    name, ext = os.path.splitext(basename)

    # 查找可用的版本号
    version = 1
    while True:
        new_basename = f"{name}_v{version}{ext}"
        new_path = f"{dir_path}/{new_basename}"

        # 需要展开来检查是否存在
        expanded_path = hou.text.expandString(new_path)
        if not os.path.exists(expanded_path):
            break
        version += 1

    return new_path

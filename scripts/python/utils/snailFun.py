import json
import os
import shutil
import subprocess
import threading
import hashlib
import hou
from PIL import Image

# from .allSetting import ALLSET # 循环引入错误

SNAIL_DBUG = True


def display_status(message, display=0, severity_level=1):  # 显示状态栏消息
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
    # message = "*" * 10 + message + "*" * 10
    severity = severity_dict[severity_level]
    hou.ui.setStatusMessage(message, severity=severity)

    def clear_status_message():
        hou.ui.setStatusMessage("")

    threading.Timer(10, clear_status_message).start()


def id_check(id, all_item):
    if id in all_item:
        for i in range(1, 1000):
            new_id = id + "_%04d" % i
            if new_id not in all_item:
                break
        return new_id
    else:
        return id


def get_file_id(abs_path):  # 文件id,完整文件hash值
    if not abs_path or not os.path.exists(abs_path):
        return
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


def get_file_id2(abs_path):  # 文件id,前后4k文件hash值
    if not abs_path or not os.path.exists(abs_path):
        return
    try:
        md5_hash = hashlib.md5()
        with open(abs_path, "rb") as file:
            head = file.read(4096)  # 读取文件前4KB
            md5_hash.update(head)
            file.seek(-4096, 2)  # 移动到文件末尾前4KB的位置
            tail = file.read(4096)
            md5_hash.update(tail)
        return md5_hash.hexdigest()
    except Exception as e:
        display_status(f"Snail_error_usf: get_file_id {abs_path} _ {e}")
        return None


def get_file_size(abs_path):  # 获取文件大小
    if not abs_path or not os.path.exists(abs_path):
        return
    size = int(os.path.getsize(abs_path) / 1024)
    return size


def get_file_ext(abs_path, point=False):
    if not abs_path:
        return
    try:
        ext = os.path.splitext(abs_path)[-1]
        if not point:
            ext = ext.strip(".")
        ext = ext.lower()
        return ext
    except Exception as e:
        display_status(f"Snail_error_usf: get_file_ext {abs_path} _ {e}", 1)


def save_json(data, abs_path):
    if not data or not abs_path:
        return
    try:
        dir = os.path.dirname(abs_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(abs_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            return True
    except Exception as e:
        display_status(f"Snail_error_usf: save_json _ {e}", 1)


def read_json(abs_path):
    if not abs_path:
        return
    try:
        if not os.path.isfile(abs_path):
            return
        with open(abs_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception as e:
        display_status(f"Snail_error_usf: save_json _ {e}", 1)


def copy_file(src_file, dst_file):
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
    except:
        display_status("Snail_error_usf: copy_file {src_path}", 1)
        return False


def read_file(abs_path):
    if not abs_path:
        return
    try:
        if not os.path.isfile(abs_path):
            return
        with open(abs_path, "r", encoding="utf-8") as f:
            cont = f.read()
            return cont
    except Exception as e:
        display_status(f"Snail_error_usf: read_file _ {e}", 1)


def save_file(data, abs_path):
    if not data or not abs_path:
        return
    try:
        dir = os.path.dirname(abs_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(data)
            return True
    except Exception as e:
        display_status(f"Snail_error_usf: save_file _ {e}", 1)


def save_fileB(data, abs_path):
    if not data or not abs_path:
        return
    try:
        dir = os.path.dirname(abs_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(abs_path, "wb") as f:
            f.write(data)
            return True
    except Exception as e:
        display_status(f"Snail_error_usf: save_file _ {e}", 1)


def convert_imga(src_img, dst_img, width=512, height=512):  # Image 转换图片
    support_exts = [
        "bmp",
        "dib",
        "gif",
        "tif",
        "tiff",
        "jfif",
        "jpe",
        "jpg",
        "jpeg",
        "pbm",
        "pgm",
        "ppm",
        "pnm",
        "png",
        "apng",
    ]
    if not src_img or not dst_img:
        return
    try:
        ext = get_file_ext(src_img)
        if not ext or ext not in support_exts:
            return
        img = Image.open(src_img)
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(dst_img)
        return True
    except Exception as e:
        display_status(f"Snail_error_usf: convert_imga _ {e}", 1)
        return False


def convert_imgb(src_img, dst_img, width=512, height=512):  # icp 转换图片
    support_exts = [
        "jpg",
        "jpeg",
        "png",
        "tif",
        "tiff",
        "exr",
        "hdr",
        "psd",
        "tx",
        "tga",
        "rat",
        "xbm",
        "xpm",
        "ppm",
        "svg",
        "pbm",
        "pdf",
        "bmp",
        "cur",
        "gif",
        "icns",
        "ico",
    ]
    if not src_img or not dst_img or not width or not height:
        return False
    try:
        ext = get_file_ext(src_img)
        if not ext:
            return
        if ext not in support_exts:
            msg = f"thumbnail don't supports {ext} format"
            hou.ui.displayMessage(msg)
            return
        folder = os.path.dirname(dst_img)
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
                src_img,
                dst_img,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        stdout_data, stderr_data = res2.communicate()
        info = stdout_data.decode("utf-8")
        error = stderr_data.decode("utf-8")
        if error:
            display_status(f"Snail_error_usf: create_img_thumbnail {src_img} _ {error}", 1)
        return True
    except Exception as e:
        display_status(f"Snail_error_usf: create_img_thumbnail {src_img} _ {e}", 1)
        return False

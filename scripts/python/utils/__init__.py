# 屏蔽 "OpenSSL 3's legacy provider failed to load" 警告。
# 该警告由 CPython 的 _hashlib 在首次初始化时发出：OpenSSL 3 环境下 CPython
# 会尝试加载 legacy provider，而 Houdini 自带的 Python 的 OpenSSL 配置通常
# 未启用它，于是第一次打开 SnailBox 插件（import requests/hashlib 等）时弹窗。
# 此警告无害：SnailBox 用到的 MD5 等算法仍在 OpenSSL 3 的 default provider 中。
# 先注册过滤器、再主动导入 hashlib，让警告在首次触发时就被静默掉。
import warnings

warnings.filterwarnings("ignore", message=".*legacy provider failed to load.*")
import hashlib  # noqa: F401  提前初始化 _hashlib，此时过滤器已生效

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import *
from .allSetting import ALLSET
from .snailFun import (
    display_status,
    get_file_ext,
    get_file_id,
    get_file_id2,
    get_file_size,
    id_check,
    save_file,
    save_fileB,
    save_json,
    read_file,
    read_json,
    copy_file,
    convert_imgb,
    convert_imga,
    get_node_userData,
    set_node_userData,
    check_path,
)
from .snailWidget import (
    Snail_List2,
    Snail_Btn,
    Snail_Btn2,
    Snail_ColorBtn,
    Snail_ComboBox,
    Snail_CheckBox,
    Snail_DropLabel,
    Snail_DropLabel2,
    Snail_Menu,
    Snail_icon,
    Snail_IconBtn,
    Snail_IconBtn2,
    Snail_IconBtn_data,
    Snail_IconBtn_toggle,
    Snail_IconBtn_bz,
    Snail_IconBtn_help,
    Snail_Label,
    Snail_LabelB,
    Snail_LabelA,
    Snail_line,
    Snail_LineEdit,
    Snail_LineEdit2,
    Snail_IntLine,
    Snail_DropLine,
    Snail_List,
    Snail_RadioButton,
    Snail_SpinBox,
    Snail_Table,
    Snail_TextBrowser,
    Snail_ImgButton,
    Snail_thumbViewer,
    Snail_assetsViewer,
)

import random
import os
import webbrowser
import hou
from hutil.Qt import QtCore, QtGui
from hutil.Qt.QtWidgets import *
from .snailFun import display_status, get_file_id2
from .fileThumb import ImgThumb
from .allSetting import ALLSET

ICON_DATAS = {}


def get_icon_path(icon_name):
    icon_path = hou.getenv("SnailBox") + "/icons/" + icon_name + ".svg"
    if os.path.isfile(icon_path):
        return icon_path
    else:
        return None


def get_icon_data(icon_name):
    if icon_name in ICON_DATAS:
        return ICON_DATAS[icon_name]
    else:
        icon_path = get_icon_path(icon_name)
        if icon_path:
            with open(icon_path, "rb") as f:
                icon_data = f.read()  # 讀取為二進制數據
                ICON_DATAS[icon_name] = icon_data
                return icon_data
        else:
            return None


class Snail_icon(hou.qt.Icon):  # hou.Icon
    def __init__(self, icon_name, width=30, height=30):
        super().__init__(icon_name, width, height)

    def __new__(cls, *args, **kwargs):
        try:
            hou.qt.Icon(*args)
        except:
            icon_name = args[0]

            icon_path = get_icon_path(icon_name)
            if icon_path:
                icon_name = icon_path
            else:
                icon_name = "MISC_python"
            if not isinstance(args, str):
                args = (icon_name,) + args[1:]
            else:
                args = icon_name
            super().__init__(*args)
        return super().__new__(cls, *args, **kwargs)


class Snail_Btn(QPushButton):  # 按钮
    def __init__(self, text, tip=None):
        super().__init__(text)
        self.setToolTip(tip)
        self.setStyleSheet(
            "QPushButton {background-color: rgb(75,75,75);border-radius: 5px;  padding: 4px;margin:2px;}"
            "QPushButton:hover {color: rgb(255,163,32); border-radius: 5px; border: 2px solid rgb(255,163,32);}"
            "QPushButton {font-family: Microsoft YaHei UI; font-size: 14px;} "
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )


class Snail_CheckBox(QCheckBox):  # 勾选框
    def __init__(self, name, tip=None):
        super().__init__(name)
        self.setToolTip(tip)
        self.setProperty("radius", "all")  # 默认
        self.setStyleSheet(
            "QCheckBox {background-color: rgb(50,50,50); padding: 4px;}"
            "QCheckBox:hover {border: 2px solid rgb(125,80,16);}"
            "QCheckBox {font-family: Microsoft YaHei UI; font-size: 14px;} "
            "QCheckBox[radius='all'] {border-radius: 5px;}"
            "QCheckBox[radius='left'] {border-top-left-radius: 5px; border-bottom-left-radius: 5px; border-top-right-radius: 0px; border-bottom-right-radius: 0px }"
            "QCheckBox[radius='right'] {border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-top-right-radius: 5px; border-bottom-right-radius: 5px }"
            "QCheckBox[radius='none'] {border-radius: 0px;}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )
        self.setFixedHeight(25)

    def set_radius(self, mode="none"):
        self.setProperty("radius", mode)
        self.style().polish(self)
        self.update()


class Snail_ComboBox(QComboBox):  # 下拉框
    def __init__(self, items=[], tip=None, pa=None):
        super().__init__(pa)
        self.setToolTip(tip)
        self.setFixedHeight(25)
        for one in items:
            if isinstance(one, str):
                self.addItem(one)
            else:
                icon = Snail_icon(one[0])
                self.addItem(icon, one[1])
        down_arrow_path = get_icon_path("snail_arrow3")
        self.setStyleSheet(
            f"""
            QComboBox {{padding: 1px 3px 1px 3px;background-color: rgb(27,27,27); }}
            QComboBox {{font-family: Microsoft YaHei UI; font-size: 13px; }}
            QComboBox:hover {{border: 2px solid rgb(125,80,16);}}"
            QComboBox::drop-down {{background-color: rgb(40,40,40); width: 25px; border-top-right-radius: 5px; border-bottom-right-radius: 5px;}}
            QComboBox::down-arrow {{image: url('{down_arrow_path}'); width: 12px; height: 12px;}}
            QComboBox QAbstractItemView {{border: 1px solid rgb(100, 100, 100);selection-background-color: rgb(125,80,16);selection-color: rgb(255, 191, 0);}}
            QToolTip {{ background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }}
            QComboBox[radius='all'] {{border-radius: 5px;}}
            QComboBox[radius='left'] {{border-top-right-radius: 0px; border-bottom-right-radius: 0px;}}
            QComboBox[radius='right'] {{border-top-left-radius: 0px; border-bottom-left-radius: 0px;}}
            QComboBox[radius='none'] {{border-radius: 0px;}}
        """
        )
        self.setProperty("radius", "all")  # 默认圆角

    def set_radius(self, mode="all"):
        """设置圆角模式"""
        self.setProperty("radius", mode)
        self.style().polish(self)
        self.update()


class Snail_RadioButton(QRadioButton):  # 单选按钮
    def __init__(self, name, tip=None):
        super().__init__(name)
        self.setToolTip(tip)
        self.setStyleSheet(
            "QRadioButton {border-radius: 5px; padding: 2px;margin-left: 2px;margin-right: 2px;}"
            "QRadioButton:hover {color: rgb(125,80,16); border-radius: 5px;}"
            "QRadioButton {font-family: Microsoft YaHei UI; font-size: 14px;} "
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )


class Snail_Label(QLabel):
    def __init__(
        self,
        text,
        pa=None,
        tip=None,
    ):
        super().__init__(text, pa)

        self.setToolTip(tip)
        self.setProperty("radius", "all")  # 默认
        self.setStyleSheet(
            "QLabel {background-color: rgb(50,50,50); padding-left: 4px;font-family: Microsoft YaHei UI;font-size: 13px;}"
            "QLabel[radius='all'] {border-radius: 5px;}"
            "QLabel[radius='left'] {border-top-left-radius: 5px; border-bottom-left-radius: 5px; border-top-right-radius: 0px; border-bottom-right-radius: 0px }"
            "QLabel[radius='right'] {border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-top-right-radius: 5px; border-bottom-right-radius: 5px }"
            "QLabel[radius='none'] {border-radius: 0px;}"
            "QToolTip { background-color: rgb(40,40,40); color: rgb(170,170,170); font-size: 13px; font-family: Microsoft YaHei UI; }"
        )

    def set_radius(self, mode="none"):
        self.setProperty("radius", mode)
        self.style().polish(self)
        self.update()


class Snail_LabelA(Snail_Label):  # 左侧标题Label
    def __init__(self, text, pa=None, tip=None, width=80, height=25):
        super().__init__(text, pa, tip)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.set_radius("left")


class Snail_LabelB(QLabel):  # Snail_Label
    def __init__(self, text, size=14, pa=None):
        super().__init__(text, pa)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")  # 设置字体为Arial
        font.setPointSize(size)  # 设置字体大小为24点
        self.setFont(font)


class Snail_LabelTip(QLabel):  # Snail_Label
    def __init__(self, text, size=10, pa=None):
        super().__init__(text, pa)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")  # 设置字体为Arial
        font.setPointSize(size)  # 设置字体大小为24点
        self.setFont(font)
        self.setStyleSheet("QLabel {color: rgb(125,125,125);}")


class Snail_DropLabel(Snail_Label):  # 拖拽添加Label
    def __init__(self, text, pa=None, tip=None, fun=None):
        super().__init__(text, pa, tip)
        self.fun = fun
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):  # 当前widget是否接受数据
        event.acceptProposedAction()

    def dropEvent(self, event):  # 当前拖拽数据释放后的操作
        mime_data = event.mimeData()
        # 提取拖拽数据的类型.
        parm_path_data = mime_data.data(hou.qt.mimeType.parmPath)
        parm_path = str(parm_path_data, "utf-8")
        node_path_data = mime_data.data(hou.qt.mimeType.nodePath)
        node_path = str(node_path_data, "utf-8")
        if self.fun:
            self.fun(parm_path, node_path)


class Snail_LineEdit(QLineEdit):  # line输入
    def __init__(self, text=None, tip=None, pa=None):
        super().__init__(text, pa)
        self.setPlaceholderText(tip)
        self.setFixedHeight(25)
        self.setStyleSheet(
            "QLineEdit {font-family: Microsoft YaHei UI; font-size: 13px;text_align: left; background-color: rgb(27,27,27); padding-left: 4px;}"
            "QLineEdit[radius='all'] {border-radius: 5px;}"
            "QLineEdit[radius='left'] {border-top-left-radius: 5px; border-bottom-left-radius: 5px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;}"
            "QLineEdit[radius='right'] {border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-top-right-radius: 5px; border-bottom-right-radius: 5px;}"
            "QLineEdit[radius='none'] {border-radius: 0px;}"
            "QLineEdit:hover {border: 2px solid rgb(125,80,16);}"
            "QLineEdit:focus {border: 1px solid rgb(255,163,32);}"
            "QLineEdit:read-only {background-color: rgb(40, 40, 40);}"
            "QToolTip { background-color: rgb(40,40,40); color: rgb(170,170,170); font-size: 13px; font-family: Microsoft YaHei UI; }"
        )

    def set_radius(self, mode="none"):
        self.setProperty("radius", mode)
        self.style().polish(self)
        self.update()


class Snail_LineEdit2(QWidget):  # line加入title
    def __init__(self, key="", value="", readOnly=False, tip=None, parent=None):
        super().__init__(parent)

        self.label = Snail_LabelA(key)
        self.edit = Snail_LineEdit(value, tip, self)
        self.edit.set_radius("right")

        self.edit.setReadOnly(readOnly)

        self.label.setFixedWidth(80)  # 统一 key 宽度（很重要）

        layout = QHBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)  # 上下留 1px 边距
        layout.setSpacing(0)

        layout.addWidget(self.label)
        layout.addWidget(self.edit, 1)


class Snail_IntLine(Snail_LineEdit):
    def __init__(self, text=None, tip=None, pa=None, bottom=0, top=None):
        super().__init__(text, pa, tip)
        int_validator = QtGui.QIntValidator(self)
        if bottom != None:
            int_validator.setBottom(bottom)
        if top != None:
            int_validator.setTop(top)
        self.setValidator(int_validator)


class Snail_DropLine(Snail_LineEdit):  # 拖拽line输入
    def __init__(self, text=None, tip=None, pa=None, fun=None):
        super().__init__(text, tip, pa)
        self.fun = fun

    def dragEnterEvent(self, event):  # 当前widget是否接受数据
        event.acceptProposedAction()

    def dropEvent(self, event):  # 当前拖拽数据释放后的操作
        mime_data = event.mimeData()
        # 提取拖拽数据的类型.
        parm_path_data = mime_data.data(hou.qt.mimeType.parmPath)
        parm_path = str(parm_path_data, "utf-8")
        node_path_data = mime_data.data(hou.qt.mimeType.nodePath)
        node_path = str(node_path_data, "utf-8")
        if self.fun:
            self.fun(parm_path, node_path)


class Snail_IconBtn(QToolButton):  # ICON小按钮
    def __init__(self, icon_name, tip=None, bg=1, pa=None):
        super().__init__(pa)
        icon = Snail_icon(icon_name)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(20, 20))
        if tip:
            self.setToolTip(tip)
        bg_list = [
            "rgba(45,45,45,0)",
            "rgb(45,45,45)",
            "rgba(45,45,45,150)",
        ]
        bg_color = bg_list[bg]
        self.setStyleSheet(
            f"""
            QToolButton {{
                background-color: {bg_color};
                border-radius: 5px;
            }}

            QToolButton:hover {{
                background-color: rgb(20,20,20);
                border: 2px solid rgb(100,100,100);
            }}

            QToolTip {{
                background-color: rgb(45,45,45);
                color: rgb(170,170,170);
                font-size: 14px;
                font-family: Microsoft YaHei UI;
            }}
            """
        )
        self.setProperty("transparent", True)
        self.resize(24, 24)


class Snail_IconBtn_checked(Snail_IconBtn):  # ICON小按钮,checked状态有不同
    def __init__(self, icon_name, tip=None, bg=1, pa=None):
        super().__init__(icon_name, tip, bg, pa)
        self.setCheckable(True)
        self.setStyleSheet(
            "QToolButton:checked{background-color:rgb(20,20,20); border:2px solid rgb(100,100,100);}"
        )


class Snail_IconBtn_data(QToolButton):  # 预览图上的ICON小按钮
    def __init__(self, icon_name, tip=None, pa=None):
        super().__init__(pa)
        icon_data = get_icon_data(icon_name)
        if not icon_data:
            return
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(icon_data)
        icon = QtGui.QIcon(pixmap)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(20, 20))
        if tip:
            self.setToolTip(tip)
        self.setStyleSheet(
            "QToolButton{background-color:rgba(255,255,255,0); padding-top: 0px;}"
            "QToolButton:hover{background-color:rgba(255,255,255,150); border:2px solid rgb(200,200,200);}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )
        self.setProperty("transparent", True)
        self.resize(24, 24)


class Snail_IconBtn2(QToolButton):  # 切换ICON小按钮(图标尺寸不对,准备废弃)
    def __init__(self, icon_name1, icon_name2, tip=None, pa=None):
        super().__init__(pa)
        icon = QtGui.QIcon()
        icon_path1 = get_icon_path(icon_name1)
        icon_path2 = get_icon_path(icon_name2)
        if icon_path1:
            pixmap = QtGui.QPixmap(icon_path1)
            icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if icon_path2:
            pixmap2 = QtGui.QPixmap(icon_path2)
            icon.addPixmap(pixmap2, QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(22, 22))
        if tip:
            self.setToolTip(tip)
        self.setStyleSheet(
            "QToolButton{ background-color:rgb(45,45,45); border-radius: 5px;}"
            "QToolButton:hover{background-color:rgb(20,20,20); border:2px solid rgb(100,100,100);}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )
        self.setProperty("transparent", True)
        self.resize(24, 24)
        self.setCheckable(True)


class Snail_IconBtn_toggle(QToolButton):  # 切换ICON小按钮
    def __init__(self, icon_name1, icon_name2, tip=None, bg=1, pa=None):
        super().__init__(pa)
        icon_path1 = get_icon_path(icon_name1)
        icon_path2 = get_icon_path(icon_name2)
        self.icon_off = QtGui.QIcon(icon_path1)
        self.icon_on = QtGui.QIcon(icon_path2)

        self.setIcon(self.icon_off)
        self.setIconSize(QtCore.QSize(20, 20))
        self.setCheckable(True)

        self.toggled.connect(self._on_toggled)

        if tip:
            self.setToolTip(tip)
        bg_list = [
            "rgba(45,45,45,0)",
            "rgb(45,45,45)",
            "rgba(45,45,45,100)",
        ]
        bg_color = bg_list[bg]
        self.setStyleSheet(
            f"""
            QToolButton {{
                background-color: {bg_color};
                border-radius: 5px;
            }}

            QToolButton:hover {{
                background-color: rgb(20,20,20);
                border: 2px solid rgb(100,100,100);
            }}

            QToolTip {{
                background-color: rgb(45,45,45);
                color: rgb(170,170,170);
                font-size: 14px;
                font-family: Microsoft YaHei UI;
            }}
            """
        )
        self.setProperty("transparent", True)
        self.setFixedSize(24, 24)

    def _on_toggled(self, checked):
        self.setIcon(self.icon_on if checked else self.icon_off)


class Snail_IconBtn3(Snail_IconBtn):  # 预览图ICON小按钮
    def __init__(self, icon_name, tip=None, pa=None):
        super().__init__(icon_name, tip, pa)
        self.setStyleSheet(
            "QToolButton{background-color:rgba(255,255,255,0); padding-top: 0px;}"
            "QToolButton:hover{background-color:rgba(255,255,255,150); border:2px solid rgb(200,200,200);}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )


class Snail_SpinBox(QSpinBox):  # 数字输入框
    def __init__(self, pre=None, suf=None, min=0, max=100, width=80):
        super().__init__()
        if pre:
            self.setPrefix(pre)
        if suf:
            self.setSuffix(suf)
        self.setMaximum(max)
        self.setMinimum(min)
        self.setMaximumWidth(width)

        self.setStyleSheet(
            "QSpinBox {font-family: Microsoft YaHei UI; font-size: 13px;text_align: left; background-color: rgb(27,27,27); padding-left: 4px;}"
            "QSpinBox[radius='all'] {border-radius: 5px;}"
            "QSpinBox[radius='left'] {border-top-left-radius: 5px; border-bottom-left-radius: 5px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;}"
            "QSpinBox[radius='right'] {border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-top-right-radius: 5px; border-bottom-right-radius: 5px;}"
            "QSpinBox[radius='none'] {border-radius: 0px;}"
            "QSpinBox:hover {border: 2px solid rgb(125,80,16);}"
            "QSpinBox:focus {border: 1px solid rgb(255,163,32);}"
            "QToolTip { background-color: rgb(40,40,40); color: rgb(170,170,170); font-size: 13px; font-family: Microsoft YaHei UI; }"
        )
        self.setProperty("transparent", True)
        self.setProperty("radius", "all")
        self.setFixedHeight(25)

    def set_radius(self, mode="all"):
        """设置圆角模式"""
        self.setProperty("radius", mode)
        self.style().polish(self)
        self.update()


class Snail_ColorBtn(QPushButton):  # 颜色按钮
    def __init__(self, pa, width=50):
        super().__init__()
        self.pa = pa
        self.setToolTip("Click to set color")
        self.setProperty("radius", "all")  # 默认圆角
        self.setStyleSheet(
            "QPushButton {background-color:rgb(15,100,200);}"
            "QPushButton[radius='all'] {border-radius: 5px;}"
            "QPushButton[radius='left'] {border-top-right-radius: 0px; border-bottom-right-radius: 0px;}"
            "QPushButton[radius='right'] {border-top-left-radius: 0px; border-bottom-left-radius: 0px;}"
            "QPushButton[radius='none'] {border-radius: 0px;}"
            "QPushButton:hover {border: 2px solid rgb(125,80,16);}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI;}"
        )
        self.setFixedWidth(width)

    def set_radius(self, mode="none"):
        """设置圆角模式"""
        self.setProperty("radius", mode)
        self.style().polish(self)
        self.update()

    def changeColor(self, color=None):
        if color:
            r = color[0]
            g = color[1]
            b = color[2]
        else:
            color = hou.ui.selectColor()
            if color == None:
                return
            r, g, b = color.rgb()
        r = round(r, 6)
        g = round(g, 6)
        b = round(b, 6)
        # 更新父对象的颜色（支持两种方式：直接 color 属性或 item.color）
        self.pa.color = [r, g, b]
        # 使用 getattr 避免 property 访问问题
        item = getattr(self.pa, "item", None)
        if item is not None:
            item.color = [r, g, b]
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        # 获取当前圆角模式并重建样式
        radius_mode = self.property("radius")
        style = f"QPushButton{{ background-color:rgb({r},{g},{b});}}"
        style += f"QPushButton[radius='all'] {{border-radius: 5px;}}"
        style += f"QPushButton[radius='left'] {{border-top-right-radius: 0px; border-bottom-right-radius: 0px;}}"
        style += f"QPushButton[radius='right'] {{border-top-left-radius: 0px; border-bottom-left-radius: 0px;}}"
        style += f"QPushButton[radius='none'] {{border-radius: 0px;}}"
        style += "QPushButton:hover {border: 2px solid rgb(125,80,16);}"
        style += "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI;}"
        self.setStyleSheet(style)

    def getColor(self):
        """获取当前颜色"""
        if hasattr(self.pa, "item"):
            return self.pa.item.color
        elif hasattr(self.pa, "color"):
            return self.pa.color
        return [1, 0, 0]  # 默认红色

    def set_randomColor(self):
        r = random.random()
        g = random.random()
        b = random.random()
        r = round(r, 6)
        g = round(g, 6)
        b = round(b, 6)
        color = [r, g, b]
        self.changeColor(color)


##################
class Snail_IconBtn_bz(Snail_IconBtn):  # 视频链接
    def __init__(self):
        super().__init__("snail_bz", "Bilibli")
        self.clicked.connect(self.go_b_web)
        self.url = "https://space.bilibili.com/319628481"

    def go_b_web(self):
        webbrowser.open(self.url, new=0, autoraise=True)

    def toggle_language(self, language):
        if language:
            self.url = "https://space.bilibili.com/319628481"
            icon = Snail_icon("snail_bz")
            self.setIcon(icon)
            self.setToolTip("Bilibli")
        else:
            self.url = "https://www.youtube.com/@SnailBox_Houdini"
            icon = Snail_icon("snail_video")
            self.setIcon(icon)
            self.setToolTip("YouTube")


class Snail_IconBtn_help(Snail_IconBtn):  # 在线帮助
    def __init__(self):
        super().__init__("snail_help", "Online documents")
        self.clicked.connect(self.go_help)

    def go_help(self):
        url = "http://snailbox.online/hsb/doc"
        webbrowser.open(url, new=0, autoraise=True)


class Snail_line(QFrame):
    def __init__(self, or_option=0):
        super().__init__()
        if or_option:
            self.setFrameShape(QFrame.VLine)
        else:
            self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(1)
        self.setMidLineWidth(0)


class Snail_TextBrowser(QTextBrowser):
    def __init__(self, pa):
        super().__init__(pa)
        self.setStyleSheet(
            "QTextBrowser {color: rgb(125,125,125); background-color: rgb(27,27,27);}"
            "QTextBrowser {font-family: Microsoft YaHei UI; font-size: 9pt;}"
        )

    def update_tips(self, tips=[]):
        self.clear()
        if not tips:
            return
        for i in tips:
            self.append(i)


class Snail_Table(QTableWidget):
    def __init__(self, pa=None):
        super().__init__(pa)
        self.setStyle(QStyleFactory.create("fusion"))
        self.setStyleSheet(
            "QTableWidget{font-family: Microsoft YaHei UI; font-size: 13px;}"
            "QTableWidget::item:hover{color: rgb(125,80,16);}"
            "QTableWidget::item:selected{color: rgb(255,163,32); background-color: rgb(125,80,16);}"
            "QTableWidget::item:focus{color: rgb(255,163,32);background-color: rgb(125,80,16);}"
        )
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setVisible(False)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().setFixedWidth(25)
        self.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.setGridStyle(QtCore.Qt.NoPen)
        self.setAlternatingRowColors(True)
        palette = self.palette()
        palette.setColor(
            QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor(29, 29, 29)
        )  # 偶数行背景色
        self.setPalette(palette)


class Snail_List(QListWidget):
    def __init__(self, pa=None):
        super().__init__(pa)
        # self.setAlternatingRowColors(True)
        # palette = self.palette()
        # palette.setColor(palette.AlternateBase, QtGui.QColor(29, 29, 29))  # 偶数行背景色
        # self.setPalette(palette)
        # self.setContentsMargins(2)
        self.setGridSize(QtCore.QSize(0, 27))
        self.setTextElideMode(QtCore.Qt.ElideMiddle)  # 中间显示省略号
        self.setStyleSheet(
            "QListWidget{background: transparent; padding: 2px;}"
            "QListWidget::item{height: 25px; background-color: rgba(45,45,45,200); border-radius: 5px;}"
            "QListWidget{font-family: Microsoft YaHei UI; font-size: 13px;}"
            "QListWidget::item:hover{color: rgb(125,80,16);background-color: rgb(100,100,100);}"
            "QListWidget::item:selected{color: rgb(255,163,32); background-color: rgb(125,80,16);}"
            # "QListWidget::item:focus{color: rgb(255,163,32); background-color: rgb(125,80,16);}"
        )


class Snail_List2(QListWidget):  # info栏
    """
    支持嵌入 QLineEdit 的列表类
    用于显示键值对列表，支持通过参数控制是否可编辑。
    """

    def __init__(self, pa=None):
        super().__init__(pa)
        self.setGridSize(QtCore.QSize(0, 27))
        self.setStyleSheet(
            "QListWidget{background: transparent; padding: 2px;}")

    def add_item(self, key, value, readOnly=False):
        """
        添加一个列表项

        Args:
            key: 键名（用于识别字段类型）
            value: 显示值
            readOnly: 是否只读

        Returns:
            Snail_LineEdit2: 嵌入的行编辑器
        """
        # 创建列表项
        list_item = QListWidgetItem()
        list_item.setSizeHint(QtCore.QSize(0, 27))
        list_item.setData(QtCore.Qt.UserRole, key)

        # 创建嵌入的 QLineEdit
        line_edit = Snail_LineEdit2(key, value, readOnly)

        # 添加到列表
        self.addItem(list_item)
        self.setItemWidget(list_item, line_edit)

        return line_edit


class Snail_Menu(QMenu):
    def __init__(self, pa=None):
        super().__init__(pa)
        menu_style = """
            QMenu {
                text-align: center;
                font-family: Microsoft YaHei UI;
                font-size: 13px;
                background-color: rgb(27,27,27);
                border: 2px solid rgb(100, 100, 100);
            }
            QMenu::item:selected {
                font-family: Microsoft YaHei UI;
                font-size: 14px;
                color: rgb(255,163,32);
                background-color: rgb(50,50,50);
            }"""
        self.setStyleSheet(menu_style)


class Snail_ImgButton(QToolButton):  # 主按钮
    def __init__(self, parent, thumbsize, name):
        super().__init__(parent)
        self.name = name
        self.btn_size = thumbsize
        self.setFixedSize(self.btn_size)
        self.icon_size = QtCore.QSize(
            self.btn_size.width(), self.btn_size.height() - 25)
        self.setIconSize(self.icon_size)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setMouseTracking(True)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.setStyleSheet(
            "QToolButton{ background-color:rgb(29,29,29);padding: 0px; padding-top: -2px; border:none;}"
            "QToolButton:hover{color: rgb(255,163,32); background-color:rgb(100,100,100);}"
        )
        self.init_date()

    def init_date(self):
        self.setText(self.name)

    def set_img(self, img):
        if not img:
            return
        try:
            if type(img) == str:
                img = QtGui.QPixmap(img)
                img_size = self.icon_size
                img = img.scaled(
                    img_size, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation
                )
            else:
                img = QtGui.QPixmap().loadFromData(img)
            self.setIcon(QtGui.QIcon(img))
        except Exception as e:
            display_status(f"Snail_error_usw: set_img _ {e}")

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        event.ignore()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(event)
        event.ignore()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(event)
        event.ignore()


class Snail_thumbViewer(QWidget):
    """
    通用图片查看组件

    特性:
        - 自动居中显示
        - 等比缩放
        - 随窗口大小自适应
        - 支持从文件路径加载或直接设置 QPixmap
    """

    def __init__(self, parent=None):
        """
        初始化图片查看器

        Args:
            parent: 父窗口
        """
        super().__init__(parent)
        self.default_image = ALLSET.sbox_path + "/file/tex/asset_miss.jpg"

        # 保存原始 pixmap
        self._origin_pixmap = None

        # 初始化 UI
        self._init_ui()

    def _init_ui(self):
        """初始化 UI 组件"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self._label = QLabel(self)
        self._label.setAlignment(QtCore.Qt.AlignCenter)

        # 关键：设置 SizePolicy 为 Ignored，允许自由缩放
        self._label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self._label.setMinimumSize(0, 0)

        self._label.setStyleSheet("QLabel {background-color: #1e1e1e;}")

        layout.addWidget(self._label)

        self.set_image(self.default_image)

    # ==================== 公共接口 ====================

    def set_image(self, path=None):
        """
        从文件路径加载并显示图片

        Args:
            path: 图片文件路径，None 则显示默认图片
        """
        # 如果路径为 None 或不是有效文件，使用默认图片
        if not path or not os.path.isfile(path):
            path = self.default_image
        pixmap = QtGui.QPixmap(path)
        if pixmap.isNull():
            self.clear()
            return
        self.set_pixmap(pixmap)

    def set_pixmap(self, pixmap):
        """
        直接设置并显示 QPixmap

        Args:
            pixmap: 要显示的 QPixmap 对象
        """
        self._origin_pixmap = pixmap
        self._update_pixmap()

    def clear(self):
        """清空显示"""
        self._origin_pixmap = None
        self._label.clear()

    def has_image(self):
        """是否正在显示图片"""
        return self._origin_pixmap is not None

    # ==================== 内部方法 ====================

    def resizeEvent(self, event):
        """窗口大小改变时重新缩放图片"""
        super().resizeEvent(event)
        self._update_pixmap()

    def _update_pixmap(self):
        """根据当前窗口大小更新显示的 pixmap"""
        if not self._origin_pixmap:
            return

        scaled = self._origin_pixmap.scaled(
            self._label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation
        )
        self._label.setPixmap(scaled)


class Snail_assetsViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.assets = []
        self.thumb_dir = ""
        self.setObjectName("Snail_assetsViewer")
        self.lb = QLabel(self)
        self.lb.setScaledContents(True)
        self.current_miss = False
        self.inter = False
        self.img_ratio = 1
        self.current_index = 0
        self.current_thumb = ""
        self.current_info = {}
        self.lw_assets = Snail_List(self)
        self.lw_assets.itemClicked.connect(self.click_item)
        self.tb_folder = self.sub_btn_folder()
        self.tb_bigView = self.sub_btn_bigView()

    def update(self, assets=[], thumbPath=""):
        self.thumb_dir = thumbPath
        self.assets = list(assets)
        self.current_index = 0
        self.current_thumb = ""
        self.file_info = {}
        self.refresh_list()
        self.refresh_img()

    @property
    def current_ex_path(self):
        index = self.current_index
        if index >= len(self.assets):
            return
        path = self.assets[index]
        ex_path = hou.text.expandString(path)
        return ex_path

    def click_item(self, item):
        self.current_thumb = ""
        self.file_info = {}
        index = self.lw_assets.row(item)
        self.current_index = index
        self.refresh_img()

    def refresh_img(self):
        index = self.current_index
        self.lb.clear()
        if not self.assets:
            return
        if index > len(self.assets):
            return
        self.get_thumb()
        if self.current_thumb:
            img = QtGui.QPixmap(self.current_thumb)
            img_size = img.size()
            self.img_ratio = img_size.width() / img_size.height()
            self.lb.setPixmap(img)
            self.resizeEvent(None)

    def refresh_list(self):
        self.lw_assets.clear()
        for one in self.assets:
            try:
                name = os.path.basename(one)
                name2 = os.path.splitext(name)[0]
                self.lw_assets.addItem(name2)
            except:
                pass

    def get_thumb_path(self, ex_path):
        self.current_miss = False
        if not ex_path:
            return
        if not os.path.isfile(ex_path):
            miss_file = f"{ALLSET.sbox_path}/file/tex/asset_miss.jpg"
            self.current_miss = True
            return miss_file
        if self.thumb_dir:
            thumb_dir = self.thumb_dir
        else:
            dir = os.path.dirname(ex_path)
            thumb_dir = f"{dir}/thumbnail"
        file_id = get_file_id2(ex_path)
        if file_id:
            thumb_path = f"{thumb_dir}/{file_id}.jpg"
            return thumb_path

    def get_thumb(self):
        ex_path = self.current_ex_path
        if not ex_path:
            return
        thumb_path = self.get_thumb_path(ex_path)
        if thumb_path and os.path.isfile(thumb_path):
            self.current_thumb = thumb_path
            return
        img_thumb = ImgThumb()
        img_thumb.init_data(ex_path, thumb_path)
        current_thumb, current_info = img_thumb.get_thumb()
        self.current_thumb = current_thumb
        self.file_info = current_info

    def get_current_info(self):
        ex_path = self.current_ex_path
        if not ex_path:
            return
        img_thumb = ImgThumb()
        file_info = img_thumb.get_file_info2(ex_path)
        if file_info:
            self.file_info = file_info
            return file_info

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        if not width or not height:
            return
        ratio = width / height
        if ratio > self.img_ratio:  # 以高度为限制
            self.lb.move(0, 0)
            w = height * self.img_ratio
            self.lb.resize(w, height)
            self.lw_assets.setHidden(False)
            self.lb.move(0, 0)
            if width - w > 30:
                self.lw_assets.resize(width - w, height)
                self.lw_assets.move(height * self.img_ratio, 0)
            else:
                self.lw_assets.resize(30, height)
                self.lw_assets.move(width - 30, 0)
        else:  # 以宽度为限制
            h = width / self.img_ratio
            self.lb.resize(width, h)
            self.lw_assets.setHidden(False)
            self.lb.move(0, 0)
            if height - h > 54:
                self.lw_assets.resize(width, height - h)
                self.lw_assets.move(0, h)
            else:
                self.lw_assets.resize(30, height)
                self.lw_assets.move(width - 30, 0)
        return super().resizeEvent(event)

    def sub_btn_folder(self):  # 跳到材质节点
        tb_folder = Snail_IconBtn("BUTTONS_folder", "Asset folder", pa=self.lb)
        tb_folder.move(2, 2)
        tb_folder.clicked.connect(lambda: self.open_file_explorer())
        tb_folder.setHidden(not self.inter)
        return tb_folder

    def sub_btn_bigView(self):  # 跳到材质节点
        tb_bigView = Snail_IconBtn("snail_big_viewer", "Zoom view", pa=self.lb)
        tb_bigView.move(2, 28)
        tb_bigView.setHidden(not self.inter)
        return tb_bigView

    def open_file_explorer(self):
        ex_path = self.current_ex_path
        if ex_path:
            hou.ui.showInFileBrowser(ex_path)

    def enterEvent(self, event):
        self.inter = True
        self.toggle_showIcon()

    def leaveEvent(self, event):
        self.inter = False
        self.toggle_showIcon()

    def toggle_showIcon(self):
        if self.current_miss or not self.assets:
            return
        self.tb_folder.setVisible(self.inter)
        self.tb_bigView.setVisible(self.inter)

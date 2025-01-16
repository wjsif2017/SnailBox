import random
import os
import webbrowser
import hou
from PySide2 import QtCore, QtGui, QtUiTools
from PySide2.QtWidgets import *


def get_icon_path(icon_name):
    icon_path = hou.getenv("SnailBox") + "/icons/" + icon_name + ".svg"
    if os.path.isfile(icon_path):
        return icon_path
    else:
        return None


class Snail_icon(hou.qt.Icon):
    def __init__(self, icon_name, width=32, height=32):
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


class Snail_Btn(QPushButton):
    def __init__(self, text, tip=None):
        super().__init__(text)
        self.setToolTip(tip)
        self.setStyleSheet(
            "QPushButton {background-color: rgb(75,75,75);border-radius: 5px;  padding: 4px;margin:2px;}"
            "QPushButton:hover {color: rgb(255,163,32); border-radius: 5px; border: 2px solid rgb(255,163,32);}"
            "QPushButton {font-family: Microsoft YaHei UI; font-size: 14px;} "
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )


class Snail_CheckBox(QCheckBox):
    def __init__(self, name, tip=None):
        super().__init__(name)
        self.setToolTip(tip)
        self.setStyleSheet(
            "QCheckBox {border-radius: 5px; padding: 2px;}"
            "QCheckBox:hover {color: rgb(255,163,32); border-radius: 5px; }"
            "QCheckBox {font-family: Microsoft YaHei UI; font-size: 14px;} "
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )


class Snail_ComboBox(QComboBox):
    def __init__(self, items=[], tip=None):
        super().__init__()
        self.setToolTip(tip)
        for one in items:
            if isinstance(one, str):
                self.addItem(one)
            else:
                icon = Snail_icon(one[0])
                self.addItem(icon, one[1])
        self.setStyleSheet(
            "QComboBox {border-radius: 5px; padding: 1px 3px 1px 3px;background-color: rgb(27,27,27); }"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )


class Snail_RadioButton(QRadioButton):
    def __init__(self, name, tip=None):
        super().__init__(name)
        self.setToolTip(tip)
        self.setStyleSheet(
            "QRadioButton {border-radius: 5px; padding: 2px;margin-left: 2px;margin-right: 2px;}"
            "QRadioButton:hover {color: rgb(255,163,32); border-radius: 5px;}"
            "QRadioButton {font-family: Microsoft YaHei UI; font-size: 14px;} "
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )


class Snail_Label(QLabel):
    def __init__(self, text, pa=None, tip=None):
        super().__init__(text, pa)
        self.setToolTip(tip)
        self.setStyleSheet(
            "QLabel {background-color: rgb(45,45,45); border-radius: 5px; padding-left: 4px;}"
            "QLabel:hover {color: rgb(255,163,32); border-radius: 5px; border: 2px solid rgb(255,163,32);}"
            "QLabel {font-family: Microsoft YaHei UI; font-size: 14px;} "
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )


class Snail_LabelA(Snail_Label):
    def __init__(self, text, pa=None, tip=None, width=80, height=25):
        super().__init__(text, pa, tip)
        self.setFixedWidth(width)
        self.setFixedHeight(height)


class Snail_DropLabel(Snail_Label):
    def __init__(self, text, pa=None, tip=None, fun=None):
        super().__init__(text, pa, tip)
        self.fun = fun
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        mime_data = event.mimeData()

        parm_path_data = mime_data.data(hou.qt.mimeType.parmPath)
        parm_path = str(parm_path_data, "utf-8")
        node_path_data = mime_data.data(hou.qt.mimeType.nodePath)
        node_path = str(node_path_data, "utf-8")
        if self.fun:
            self.fun(parm_path, node_path)


class Snail_LineEdit(QLineEdit):
    def __init__(self, text=None, pa=None, tip=None):
        super().__init__(text, pa)
        self.setToolTip(tip)
        self.setStyleSheet(
            "QLineEdit {text_align: left; background-color: rgb(27,27,27); border-radius: 5px;  padding-left: 4px;}"
            "QLineEdit:hover {color: rgb(255,163,32); border-radius: 5px; border: 2px solid rgb(255,163,32);}"
            "QLineEdit:focus {background-color: rgb(20,20,20);}"
            "QLineEdit {font-family: Microsoft YaHei UI; font-size: 14px;} "
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )
        self.setFixedHeight(25)


class Snail_IntLine(Snail_LineEdit):
    def __init__(self, text=None, pa=None, tip=None, bottom=0, top=None):
        super().__init__(text, pa, tip)
        int_validator = QtGui.QIntValidator(self)
        if bottom != None:
            int_validator.setBottom(bottom)
        if top != None:
            int_validator.setTop(top)
        self.setValidator(int_validator)


class Snail_DropLine(Snail_LineEdit):
    def __init__(self, text=None, pa=None, tip=None, fun=None):
        super().__init__(text, pa, tip)
        self.fun = fun

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        mime_data = event.mimeData()

        parm_path_data = mime_data.data(hou.qt.mimeType.parmPath)
        parm_path = str(parm_path_data, "utf-8")
        node_path_data = mime_data.data(hou.qt.mimeType.nodePath)
        node_path = str(node_path_data, "utf-8")
        if self.fun:
            self.fun(parm_path, node_path)


class Snail_IconBtn(QToolButton):
    def __init__(self, icon_name, tip=None):
        super().__init__()
        icon = Snail_icon(icon_name)
        self.setIcon(icon)
        if tip:
            self.setToolTip(tip)
        self.setStyleSheet(
            "QToolButton{ background-color:rgb(45,45,45); border-radius: 5px;}"
            "QToolButton:hover{background-color:rgb(61,61,61); border:2px solid rgb(255,163,32);}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )
        self.setProperty("transparent", True)
        self.resize(30, 30)


class Snail_IconBtn2(QToolButton):
    def __init__(self, icon_name1, icon_name2, tip=None):
        super().__init__()
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
        if tip:
            self.setToolTip(tip)
        self.setStyleSheet(
            "QToolButton{ background-color:rgb(45,45,45); border-radius: 5px;}"
            "QToolButton:hover{background-color:rgb(61,61,61); border:2px solid rgb(255,163,32);}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )
        self.setProperty("transparent", True)
        self.resize(30, 30)
        self.setCheckable(True)


class Snail_SpinBox(QSpinBox):
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
            "QSpinBox {background-color: rgb(27,27,27); border-radius: 5px;}"
            "QSpinBox:hover{background-color:rgb(61,61,61); border:2px solid rgb(255,163,32);}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )
        self.setProperty("transparent", True)


class Snail_ColorBtn(QPushButton):
    def __init__(self, pa, width=50):
        super().__init__()
        self.pa = pa
        self.setToolTip("Click to set color")
        style = "QPushButton{ background-color:rgb(15,100,200); border-radius: 5px;}"
        self.style2 = """QPushButton:hover{border:2px solid rgb(255,163,32);}
              QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI;}"""
        self.setStyleSheet(style + self.style2)
        self.setFixedWidth(width)

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
        self.pa.color = [r, g, b]
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        style = "QPushButton{ background-color:rgb(%d,%d,%d);border-radius: 5px;}" % (r, g, b)
        self.setStyleSheet(style + self.style2)

    def set_randomColor(self):
        r = random.random()
        g = random.random()
        b = random.random()
        r = round(r, 6)
        g = round(g, 6)
        b = round(b, 6)
        color = [r, g, b]
        self.changeColor(color)


class Snail_IconBtn_bz(Snail_IconBtn):
    def __init__(self):
        super().__init__("snail_bz", "Bilibli")
        self.setIconSize(QtCore.QSize(24, 24))
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


class Snail_IconBtn_help(Snail_IconBtn):
    def __init__(self):
        super().__init__("snail_help", "Online documents")
        self.setIconSize(QtCore.QSize(24, 24))
        self.clicked.connect(self.go_help)

    def go_help(self):
        url = "http://snailbox.online/hsb/doc"
        webbrowser.open(url, new=0, autoraise=True)


class thumbViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Snail_imgViewer2")
        img_layout = QGridLayout()
        img_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(img_layout)
        self.lb = QLabel()
        self.lb.setObjectName("l_img")
        self.lb.setScaledContents(True)
        img_layout.addWidget(self.lb)
        self.img_ratio = 1.0

    def update_img(self, path=None):
        if not path:
            self.lb.clear()
            return
        img = QtGui.QPixmap(path)
        img_size = img.size()
        self.img_ratio = img_size.width() / img_size.height()
        self.lb.setPixmap(img)
        self.resizeEvent(None)

    def resizeEvent(self, event):
        ratio = self.size().width() / self.size().height()
        if ratio > self.img_ratio:
            self.lb.setMaximumWidth(self.size().height() * self.img_ratio)
            self.lb.setMinimumWidth(self.size().height() * self.img_ratio)
            self.lb.setMaximumHeight(self.size().height())
            self.lb.setMinimumHeight(20)
        else:
            self.lb.setMaximumWidth(self.size().width())
            self.lb.setMinimumWidth(20)
            self.lb.setMaximumHeight(self.size().width() / self.img_ratio)
            self.lb.setMinimumHeight(self.size().width() / self.img_ratio)
        return super().resizeEvent(event)


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

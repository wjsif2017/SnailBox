import random
import os
import webbrowser
import hou
from PySide2 import QtCore, QtGui, QtUiTools
from PySide2.QtWidgets import *
from .snailFun import *
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
                icon_data = f.read()
                ICON_DATAS[icon_name] = icon_data
                return icon_data
        else:
            return None


class Snail_icon(hou.qt.Icon):
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
            QComboBox {{border-radius: 5px; padding: 1px 3px 1px 3px;background-color: rgb(27,27,27); }}
            QComboBox {{font-family: Microsoft YaHei UI; font-size: 13px; }}
            QComboBox::drop-down {{background-color: rgb(40,40,40); width: 25px; border-top-right-radius: 5px; border-bottom-right-radius: 5px;}}
            QComboBox::down-arrow {{image: url('{down_arrow_path}'); width: 12px; height: 12px;}}
            QComboBox QAbstractItemView {{border: 1px solid rgb(100, 100, 100);selection-background-color: rgb(100,80,40);selection-color: rgb(255, 191, 0);}}
            QToolTip {{ background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }}
        """
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
            "QLabel {font-family: Microsoft YaHei UI; font-size: 13px;} "
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 13px; font-family: Microsoft YaHei UI; }"
        )


class Snail_LabelA(Snail_Label):
    def __init__(self, text, pa=None, tip=None, width=80, height=25):
        super().__init__(text, pa, tip)
        self.setFixedWidth(width)
        self.setFixedHeight(height)


class Snail_LabelB(QLabel):
    def __init__(self, text, size=14, pa=None):
        super().__init__(text, pa)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(size)
        self.setFont(font)


class Snail_LabelTip(QLabel):
    def __init__(self, text, size=10, pa=None):
        super().__init__(text, pa)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(size)
        self.setFont(font)
        self.setStyleSheet("QLabel {color: rgb(125,125,125);}")


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
    def __init__(self, text=None, tip=None, pa=None):
        super().__init__(text, pa)
        self.setPlaceholderText(tip)
        self.setStyleSheet(
            "QLineEdit {text_align: left; background-color: rgb(27,27,27); border-radius: 5px;  padding-left: 4px;}"
            "QLineEdit:hover {color: rgb(255,163,32); border-radius: 5px; border: 2px solid rgb(255,163,32);}"
            "QLineEdit:focus {background-color: rgb(20,20,20);}"
            "QLineEdit {font-family: Microsoft YaHei UI; font-size: 13px;} "
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )
        self.setFixedHeight(25)


class Snail_IntLine(Snail_LineEdit):
    def __init__(self, text=None, tip=None, pa=None, bottom=0, top=None):
        super().__init__(text, pa, tip)
        int_validator = QtGui.QIntValidator(self)
        if bottom != None:
            int_validator.setBottom(bottom)
        if top != None:
            int_validator.setTop(top)
        self.setValidator(int_validator)


class Snail_DropLine(Snail_LineEdit):
    def __init__(self, text=None, tip=None, pa=None, fun=None):
        super().__init__(text, tip, pa)
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
    def __init__(self, icon_name, tip=None, pa=None):
        super().__init__(pa)
        icon = Snail_icon(icon_name)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(20, 20))
        if tip:
            self.setToolTip(tip)
        self.setStyleSheet(
            "QToolButton{ background-color:rgb(45,45,45); border-radius: 5px;}"
            "QToolButton:hover{background-color:rgb(20,20,20); border:2px solid rgb(100,100,100);}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )
        self.setProperty("transparent", True)
        self.resize(24, 24)


class Snail_IconBtn_data(QToolButton):
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


class Snail_IconBtn2(QToolButton):
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


class Snail_IconBtn3(Snail_IconBtn):
    def __init__(self, icon_name, tip=None, pa=None):
        super().__init__(icon_name, tip, pa)
        self.setStyleSheet(
            "QToolButton{background-color:rgba(255,255,255,0); padding-top: 0px;}"
            "QToolButton:hover{background-color:rgba(255,255,255,150); border:2px solid rgb(200,200,200);}"
            "QToolTip { background-color: rgb(45,45,45); color: rgb(170,170,170); font-size: 14px; font-family: Microsoft YaHei UI; }"
        )


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
        self.setFixedHeight(25)


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
            "QTableWidget::item:hover{color: rgb(255,163,32);}"
            "QTableWidget::item:selected{color: rgb(255,163,32); background-color: rgb(100,80,40);}"
            "QTableWidget::item:focus{color: rgb(255,163,32);background-color: rgb(100,80,40);}"
        )
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setVisible(False)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().setFixedWidth(25)
        self.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.setGridStyle(QtCore.Qt.NoPen)
        self.setAlternatingRowColors(True)
        palette = self.palette()
        palette.setColor(palette.AlternateBase, QtGui.QColor(29, 29, 29))
        self.setPalette(palette)


class Snail_List(QListWidget):
    def __init__(self, pa=None):
        super().__init__(pa)

        self.setGridSize(QtCore.QSize(0, 27))
        self.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.setStyleSheet(
            "QListWidget{background: transparent; padding: 2px;}"
            "QListWidget::item{height: 25px; background-color: rgba(45,45,45,200); border-radius: 5px;}"
            "QListWidget{font-family: Microsoft YaHei UI; font-size: 13px;}"
            "QListWidget::item:hover{color: rgb(255,163,32);background-color: rgb(100,100,100);}"
            "QListWidget::item:selected{color: rgb(255,163,32); background-color: rgb(100,80,40);}"
        )


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


class Snail_ImgButton(QToolButton):
    def __init__(self, parent, thumbsize, name):
        super().__init__(parent)
        self.name = name
        self.btn_size = thumbsize
        self.setFixedSize(self.btn_size)
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
        icon_size = QtCore.QSize(self.btn_size.width(), self.btn_size.height() - 25)
        self.setIconSize(icon_size)

    def set_img(self, img):
        if not img:
            return
        try:
            if type(img) == str:
                img = QtGui.QPixmap(img)
                img_size = QtCore.QSize(self.thumb_width, self.thumb_height - 25)
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
            self.lb.setPixmap(self.current_thumb)
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
        if ratio > self.img_ratio:
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
        else:
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

    def sub_btn_folder(self):
        tb_folder = Snail_IconBtn("BUTTONS_folder", "Asset folder", pa=self.lb)
        tb_folder.move(2, 2)
        tb_folder.clicked.connect(lambda: self.open_file_explorer())
        tb_folder.setHidden(not self.inter)
        return tb_folder

    def sub_btn_bigView(self):
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

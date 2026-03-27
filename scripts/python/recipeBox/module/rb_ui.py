import os
import hou
from pathlib import Path
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import *
from hrecipes import storage
from utils.videoViewer import VideoViewer
from utils import capture as cap
from utils.snailFun import display_status
from utils.allSetting import ALLSET
from .rb_set import MYSET
from utils.snailWidget import (
    Snail_List2,
    Snail_Btn,
    Snail_ComboBox,
    Snail_IconBtn,
    Snail_IconBtn_toggle,
    Snail_IconBtn_bz,
    Snail_IconBtn_help,
    Snail_LabelB,
    Snail_LineEdit,
    Snail_Table,
    Snail_TextBrowser,
)


class Ui_Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_main_layout()

    def _setup_main_layout(self):
        layout_main = QHBoxLayout(self)
        layout_main.setSpacing(0)
        layout_main.setContentsMargins(0, 0, 0, 0)

        layout_menu = self._create_left_menu()
        layout_main.addLayout(layout_menu)

        layout_main2 = self._create_main_content()
        layout_main.addLayout(layout_main2)

    def _create_left_menu(self):
        layout_menu = QVBoxLayout()

        self.leftmenu = self._create_leftmenu_frame()
        layout_menu.addWidget(self.leftmenu)

        return layout_menu

    def _create_leftmenu_frame(self):
        frame = QFrame(self)
        frame.setFixedWidth(70)
        frame.setStyleSheet("border:0;\n" "background-color: #2d2d2d;")
        frame.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_leftmenu = QVBoxLayout(frame)
        self.layout_leftmenu.setContentsMargins(0, 0, 0, 0)
        self.layout_leftmenu.setSpacing(2)

        self.layout_leftmenu.addItem(QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Fixed))

        self.lw_menu1 = self._create_library_menu(frame)
        self.layout_leftmenu.addWidget(self.lw_menu1)

        self.layout_leftmenu.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))

        return frame

    def _create_library_menu(self, parent):
        list_widget = QListWidget(parent)
        list_widget.setObjectName("lw_menu1")
        list_widget.setStyleSheet(
            "QListWidget::item:selected {background-color:rgb(35, 35, 39); border-left: 6px solid rgb(255,163,32);}"
        )
        list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        list_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        list_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        list_widget.setViewMode(QListView.IconMode)
        list_widget.setItemAlignment(QtCore.Qt.AlignCenter)
        list_widget.setIconSize(QtCore.QSize(40, 40))
        list_widget.setGridSize(QtCore.QSize(70, 72))
        return list_widget

    def _create_main_content(self):
        layout = QVBoxLayout()

        layout_top = self._create_top_bar()
        layout.addLayout(layout_top)

        layout_tool = self._create_tool_bar()
        layout.addLayout(layout_tool)

        splitter_v = self._create_center_splitter()
        layout.addWidget(splitter_v)

        layout_bottom = self._create_bottom_bar()
        layout.addLayout(layout_bottom)

        return layout

    def _create_top_bar(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)

        self.l_title = Snail_LabelB("Texture Browser", 14)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.cb_group = Snail_ComboBox()
        self.cb_group.setFixedWidth(200)

        layout.addWidget(self.l_title)
        layout.addItem(spacer)
        layout.addWidget(self.cb_group)

        return layout

    def _create_tool_bar(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._create_tool_buttons()

        layout.addItem(spacer)
        layout.addWidget(self.tb_zip_export)
        layout.addWidget(self.tb_zip_import)
        layout.addWidget(self.tb_md)
        layout.addWidget(self.tb_cap_img)
        layout.addWidget(self.tb_cap_video)
        layout.addWidget(self.tb_folder)
        layout.addWidget(self.tb_ignore)
        layout.addWidget(self.tb_delete)
        layout.addWidget(self.tb_fav)

        return layout

    def _create_tool_buttons(self):
        self.tb_zip_export = Snail_IconBtn("snail_zip0", "Export recipe zip")
        self.tb_zip_import = Snail_IconBtn("snail_zip1", "Import recipe zip")
        self.tb_md = Snail_IconBtn("snail_md", "View and edit MD")
        self.tb_cap_img = Snail_IconBtn("snail_matThumb2", "Capture thumb")
        self.tb_cap_video = Snail_IconBtn("snail_rec_on", "Capture video")
        self.tb_folder = Snail_IconBtn("BUTTONS_folder", "Item folder")
        self.tb_ignore = Snail_IconBtn_toggle("snail_ignore1", "snail_ignore2", "Toggle ignore")
        self.tb_delete = Snail_IconBtn("COMMON_delete", "Delete")
        self.tb_fav = Snail_IconBtn_toggle("snail_fav1", "snail_fav2", "Solo fav")

    def _create_center_splitter(self):
        splitter_v = QSplitter()
        splitter_v.setOrientation(QtCore.Qt.Vertical)

        self.list_thumb = self._create_thumb_list()
        splitter_v.addWidget(self.list_thumb)

        splitter_info = self._create_info_splitter()
        splitter_v.addWidget(splitter_info)

        splitter_v.setSizes([120, 20])

        return splitter_v

    def _create_thumb_list(self):
        list_widget = QListWidget(self)
        list_widget.setObjectName("list_thumb")
        list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        list_widget.setProperty("isWrapping", True)
        list_widget.setResizeMode(QListView.Adjust)
        list_widget.setSpacing(4)
        list_widget.setViewMode(QListView.IconMode)
        return list_widget

    def _create_info_splitter(self):
        splitter = QSplitter()
        splitter.setOrientation(QtCore.Qt.Horizontal)

        self.list_info = Snail_List2(self)
        self.list_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.video_viewer = VideoViewer()

        splitter.addWidget(self.list_info)
        splitter.addWidget(self.video_viewer)
        splitter.setSizes([100, 100])

        return splitter

    def _create_bottom_bar(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)

        self._create_bottom_buttons()

        layout.addWidget(self.tb_set)
        layout.addWidget(self.tb_bz)
        layout.addWidget(self.tb_help)
        layout.addWidget(self.btn_apply)
        layout.addWidget(self.btn_refresh)

        return layout

    def _create_bottom_buttons(self):
        self.tb_bz = Snail_IconBtn_bz()
        self.tb_help = Snail_IconBtn_help()
        self.tb_set = Snail_IconBtn("snail_set", "Settings")
        self.btn_refresh = Snail_Btn("Refresh")
        self.btn_apply = Snail_Btn("Apply")


class Ui_Setting(QDialog):
    PACKAGE_SEPARATOR = " : "
    DEFAULT_PACKAGE = "SnailBox"

    DEFAULT_RECIPE_DATA = {
        "data": {"type": "box", "parms": {"divrate": [2, 2, 2], "type": "polymesh"}},
        "info": {
            "author": "SnailBox",
            "created": "January 21, 2026 - 10:51:10",
            "houdini_version": "21.0.440",
            "data_version": "1.0",
            "comment": "",
        },
        "properties": {
            "recipe_category": "node_preset_recipe",
            "visible": True,
            "nodetype_category": "Sop",
            "nodetype_name": "box",
            "nodetype_patterns": ["Sop/box"],
        },
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pa = parent
        self._setup_window()
        self.init_ui()
        self.init_data()
        self.connect_signals()

    def _setup_window(self):
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        self.setWindowTitle("SnailBox Recipe Box Setting")
        self.setWindowFlags(
            self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint
            | QtCore.Qt.WindowCloseButtonHint
        )

    def init_ui(self):
        tab = self._create_tab_widget()
        layout_main = QVBoxLayout(self)
        layout_main.addWidget(tab)

        self.tab_library = self._create_library_tab()
        tab.addTab(self.tab_library, "Library")

        self.setLayout(layout_main)

    def _create_tab_widget(self):
        tab = QTabWidget(self)
        tab.setStyleSheet(
            "QTabBar::tab:selected {color: rgb(255,163,32);}"
            "QTabBar {font-family: Microsoft YaHei UI; font-size: 14px;}"
        )
        return tab

    def _create_library_tab(self):
        layout_tab1 = QVBoxLayout()

        self.tw_libList = self._create_library_table()
        layout_tab1.addWidget(self.tw_libList)

        layout_options = self._create_options_layout()
        layout_tab1.addLayout(layout_options)

        layout_buttons = self._create_buttons_layout()
        layout_tab1.addLayout(layout_buttons)

        self.t_tips = Snail_TextBrowser(self)
        self.t_tips.setFixedHeight(80)
        layout_tab1.addWidget(self.t_tips)

        layout_tab1.setStretch(0, 1)

        tab_widget = QWidget()
        tab_widget.setLayout(layout_tab1)
        return tab_widget

    def _create_library_table(self):
        table = Snail_Table(self)
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Name", "Package"])
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.itemClicked.connect(self.on_lib_selected)
        return table

    def _create_options_layout(self):
        layout = QHBoxLayout()

        self.cb_package = Snail_ComboBox(tip="Package : hda")
        self.cb_package.setFixedWidth(200)

        self.cb_index = Snail_ComboBox(tip="Index")
        self.cb_index.setFixedWidth(50)

        self.cb_icon = Snail_ComboBox(tip="Icon")
        self.cb_icon.setFixedWidth(100)

        self.le_name = Snail_LineEdit(tip="Library name")

        layout.addWidget(self.cb_package)
        layout.addWidget(self.cb_index)
        layout.addWidget(self.cb_icon)
        layout.addWidget(self.le_name)
        return layout

    def _create_buttons_layout(self):
        layout = QHBoxLayout()

        self.btn_del = Snail_Btn("Delete")
        self.btn_mod = Snail_Btn("Modify")
        self.btn_add = Snail_Btn("Add")

        layout.addWidget(self.btn_del)
        layout.addWidget(self.btn_mod)
        layout.addWidget(self.btn_add)
        return layout

    def init_data(self):
        self.refresh_lib_list()
        self.refresh_package_cb()
        self.refresh_index_cb()
        self.refresh_icon_cb()
        self.refresh_tips()

    def connect_signals(self):
        self.btn_add.clicked.connect(self.add_lib)
        self.btn_del.clicked.connect(self.del_lib)
        self.btn_mod.clicked.connect(self.mod_lib)
        self.cb_package.currentTextChanged.connect(self.refresh_tips)

    def refresh_lib_list(self):
        self.tw_libList.setRowCount(0)
        for lib_name in MYSET.lib_sort:
            lib_dict = MYSET.libs.get(lib_name)
            if not lib_dict:
                continue

            row = self.tw_libList.rowCount()
            self.tw_libList.insertRow(row)

            self.tw_libList.setItem(row, 0, QTableWidgetItem(lib_dict.get("name", "")))

            package_display = self._format_package_display(lib_dict)
            self.tw_libList.setItem(row, 1, QTableWidgetItem(package_display))

        self.tw_libList.resizeColumnsToContents()

    def _format_package_display(self, lib_dict):
        package = lib_dict.get("package", "")
        hda = lib_dict.get("hda", "")
        return f"{package}{self.PACKAGE_SEPARATOR}{hda}" if package and hda else package

    def refresh_package_cb(self):
        self.cb_package.clear()

        packages = self._get_available_packages()
        packages = sorted(packages)
        packages.insert(0, "Add new lib")

        for pkg in packages:
            self.cb_package.addItem(pkg)

    def _get_available_packages(self):
        store = storage.recipeStorage()
        all_refs = store.refs()
        packages = set()

        for ref in all_refs:
            location = ref.location()
            package = Path(location).parent.parent.name
            if package == "SnailBox_dev":
                package = self.DEFAULT_PACKAGE
            name = Path(location).stem
            packages.add(f"{package}{self.PACKAGE_SEPARATOR}{name}")

        return packages

    def refresh_index_cb(self):
        self.cb_index.clear()
        for i in range(len(MYSET.lib_sort) + 1):
            self.cb_index.addItem(str(i))

    def refresh_icon_cb(self):
        self.cb_icon.clear()
        icon_folder = ALLSET.sbox_path + "/file/icon02/"

        if os.path.exists(icon_folder):
            icons = os.listdir(icon_folder)
            for icon_file in sorted(icons):
                if icon_file.endswith(".svg"):
                    icon_num = icon_file.split(".")[0]
                    icon_path = os.path.join(icon_folder, icon_file)
                    icon = QtGui.QIcon(icon_path)
                    self.cb_icon.addItem(icon, icon_num)

    def refresh_tips(self):
        tips = [
            "* Add: Add a new library to the list",
            "* Delete: Select a library and click delete",
            "* Modify: Select a library and modify its properties",
            "* Package: 'package : hda_name'",
            "* Name: The name of the library",
        ]
        self.t_tips.update_tips(tips)

    def on_lib_selected(self):
        row = self.tw_libList.currentRow()
        if not self._is_valid_row(row):
            return

        lib_name = MYSET.lib_sort[row]
        lib_dict = MYSET.libs.get(lib_name)
        if not lib_dict:
            return

        self._fill_library_options(lib_name, lib_dict, row)

    def _is_valid_row(self, row):
        return row >= 0 and row < len(MYSET.lib_sort)

    def _fill_library_options(self, lib_name, lib_dict, row):
        self.le_name.setText(lib_dict.get("name", ""))

        package_hda = self._format_package_display(lib_dict)
        self.cb_package.setCurrentText(package_hda)

        self.cb_index.setCurrentText(str(row))

        self._set_current_icon(lib_dict.get("icon", ""))

    def _set_current_icon(self, icon_num):
        if icon_num:
            index = self.cb_icon.findData(icon_num)
            if index >= 0:
                self.cb_icon.setCurrentIndex(index)

    def get_selected_lib_name(self):
        row = self.tw_libList.currentRow()
        if not self._is_valid_row(row):
            hou.ui.displayMessage("Please select a library from the list")
            return None
        return MYSET.lib_sort[row]

    def add_lib(self):
        package_hda = self.cb_package.currentText()
        index = int(self.cb_index.currentText())
        icon = self.cb_icon.currentText()
        name = self.le_name.text()

        if not name:
            hou.ui.displayMessage("Please enter a library name")
            return

        if package_hda == "Add new lib":
            if not self._create_new_library(name):
                return
            package_hda = f"{self.DEFAULT_PACKAGE}{self.PACKAGE_SEPARATOR}{name}"

        parsed = self._parse_package_hda(package_hda)
        if not parsed:
            return

        package, hda = parsed

        lib_dict = {
            "name": name,
            "icon": icon,
            "package": package,
            "hda": hda,
        }

        result = MYSET.add_lib(index, lib_dict)

        if result:
            self._refresh_after_change()

    def _create_new_library(self, name):
        res = self.add_hda(name)
        return res is not None

    def _parse_package_hda(self, package_hda):
        if self.PACKAGE_SEPARATOR in package_hda:
            return package_hda.split(self.PACKAGE_SEPARATOR, 1)

        hou.ui.displayMessage(f"Invalid package format: {package_hda}")
        return None

    def _refresh_after_change(self):
        self.refresh_lib_list()
        self.refresh_index_cb()
        if hasattr(self.pa, "refresh_manager"):
            self.pa.refresh_manager()

    def del_lib(self):
        lib_name = self.get_selected_lib_name()
        if not lib_name:
            return

        confirm = hou.ui.displayMessage(
            f"Are you sure you want to delete library '{lib_name}'?",
            buttons=("Cancel", "OK"),
            close_choice=0,
        )

        if confirm == 1:
            result = MYSET.del_lib(lib_name)
            if result:
                self._refresh_after_change()

    def mod_lib(self):
        lib_name = self.get_selected_lib_name()
        if not lib_name:
            return

        package_hda = self.cb_package.currentText()
        new_index = int(self.cb_index.currentText())
        icon = self.cb_icon.currentText()
        name = self.le_name.text()

        if not name:
            hou.ui.displayMessage("Please enter a library name")
            return

        parsed = self._parse_package_hda(package_hda)
        if not parsed:
            return

        package, hda = parsed

        lib_dict = MYSET.libs.get(lib_name)
        if not lib_dict:
            hou.ui.displayMessage(f"Library '{lib_name}' not found")
            return

        if not self._validate_modifiable_fields(lib_name, lib_dict, name, package, hda):
            return

        lib_dict["icon"] = icon

        result = MYSET.update_lib(lib_name, new_index, lib_dict)

        if result:
            self.refresh_lib_list()
            if hasattr(self.pa, "refresh_manager"):
                self.pa.refresh_manager()

    def _validate_modifiable_fields(self, lib_name, lib_dict, name, package, hda):
        if lib_name != name:
            hou.ui.displayMessage("Library name cannot be modified")
            self.on_lib_selected()
            return False

        old_package = lib_dict.get("package", "")
        old_hda = lib_dict.get("hda", "")
        if old_package != package or old_hda != hda:
            hou.ui.displayMessage(
                "Package and HDA cannot be modified (read from Houdini Recipe Storage)"
            )
            self.on_lib_selected()
            return False

        return True

    def add_hda(self, name):
        if not name:
            return None

        if self._hda_exists(name):
            hou.ui.displayMessage(f"HDA '{name}' already exists")
            return None

        try:
            store = storage.recipeStorage()
            hda_path = os.path.join(ALLSET.sbox_path, "otls", f"{name}.hda")
            store.saveToHDA(
                name=f"{self.DEFAULT_PACKAGE}::{name}::test",
                label="test",
                location=hda_path,
                recipe_data=self.DEFAULT_RECIPE_DATA,
            )
            return True
        except Exception as e:
            display_status(f"Snail_error_rb: Failed to add new recipe lib: {e}")
            hou.ui.displayMessage(f"Failed to add new recipe lib: {e}")
            return None

    def _hda_exists(self, name):
        libs = MYSET.libs if MYSET.libs else {}
        for lib in libs.values():
            if lib.get("hda") == name and lib.get("package").startswith(self.DEFAULT_PACKAGE):
                return True
        return False


class Item_Widget(QToolButton):
    def __init__(self, parent, info=None):
        super().__init__(parent)
        self.parent = parent
        self._init_attributes()
        self._setup_widget()
        if info:
            self.update(info)

    def _init_attributes(self):
        self.setObjectName("item")
        self.inter = False
        self.id = ""
        self.name = "recipe_name"
        self.type = "recipe"
        self.fav = False
        self.thumb_width = 128
        self.thumb_height = 128
        self.thumb_abs = ""

    def _setup_widget(self):
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setMouseTracking(True)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._set_stylesheet()

    def _set_stylesheet(self):
        self.setStyleSheet(
            "QToolButton#item{ background-color:rgb(29,29,29);padding: 0px; padding-top: -2px; border:none;}"
            "QToolButton#item:hover{color: rgb(255,163,32); background-color:rgb(60,60,60);}"
        )

    def update(self, info):
        for k, v in info.items():
            setattr(self, k, v)
        self.update_ui()

    def update_ui(self):
        self._set_sizes()
        self._set_display_text()
        self.update_thumb()
        self._setup_buttons()

    def _set_sizes(self):
        self.widget_size = QtCore.QSize(self.thumb_width, self.thumb_height + 25)
        self.setFixedSize(self.widget_size)
        self.icon_size = QtCore.QSize(self.thumb_width, self.thumb_height)
        self.setIconSize(self.icon_size)

    def _set_display_text(self):
        display_text = getattr(self, "title", None) or self.name
        self.setText(display_text)

    def _setup_buttons(self):
        self.sub_btn_cap()
        self.sub_btn_fav()
        self.sub_btn_type()
        self.sub_btn_apply()

    def sub_btn_apply(self):
        if getattr(self, "tb_apply", True):
            self.tb_apply = Snail_IconBtn("snail_add", "Apply recipe", pa=self)
            self.tb_apply.move(self.thumb_width - 26, self.thumb_height)
            self.tb_apply.clicked.connect(self.apply_recipe)
            self.tb_apply.setVisible(self.inter)

    def sub_btn_cap(self):
        if getattr(self, "tb_cap", True):
            self.tb_cap = Snail_IconBtn("snail_matThumb2", "Capture thumb", pa=self)
            self.tb_cap.move(self.thumb_width - 52, self.thumb_height)
            self.tb_cap.clicked.connect(self.cap_thumb)
            self.tb_cap.setVisible(self.inter)

    def sub_btn_fav(self):
        if getattr(self, "tb_fav", True):
            self.tb_fav = Snail_IconBtn_toggle("snail_fav1", "snail_fav2", bg=2, pa=self)
            self.tb_fav.move(self.thumb_width - 52, 2)
            self.tb_fav.clicked.connect(self.toggle_fav)
            self._update_fav_button()
        else:
            self.tb_fav.setChecked(self.fav)
            if self.inter or self.fav:
                self.tb_fav.setVisible(True)

    def _update_fav_button(self):
        self.tb_fav.setVisible(self.fav)
        self.tb_fav.setChecked(self.fav)

    def sub_btn_type(self):
        if getattr(self, "tb_type", True):
            icon = self._get_type_icon()
            self.tb_type = Snail_IconBtn(icon, "recipe_type", bg=2, pa=self)
            self.tb_type.move(self.thumb_width - 26, 2)

    def _get_type_icon(self):
        icon_dict = {
            "nodePreset": "DATATYPES_preset_parms",
            "tool": "DATATYPES_node_path",
            "decoration": "DATATYPES_preset_nodes_central",
        }
        return icon_dict.get(self.type, "BUTTONS_recipe")

    def apply_recipe(self):
        self.parent.manager.apply_item(self.id)

    def cap_thumb(self):
        capImg = cap.CaptureImage(self.thumb_abs)
        capImg.finish_sig.connect(self.update_thumb)
        capImg.show()

    def toggle_fav(self):
        self.fav = not self.fav
        self.tb_fav.setChecked(self.fav)
        self.parent.manager.items_toggle_fav([self.id])

    def toggle_showIcon(self):
        self.tb_fav.setVisible(self.inter)
        self.tb_cap.setVisible(self.inter)
        self.tb_apply.setVisible(self.inter)
        if self.fav:
            self.tb_fav.setVisible(True)

    def update_thumb(self):
        try:
            thumb_abs = self._get_thumb_path()
            img = QtGui.QPixmap(thumb_abs)
            img = img.scaled(
                self.icon_size, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation
            )
            self.setIcon(QtGui.QIcon(img))
        except Exception as e:
            display_status(f"Snail_error_usw: set_img _ {e}")

    def _get_thumb_path(self):
        thumb_abs = self.thumb_abs
        if not Path(thumb_abs).is_file():
            thumb_abs = ALLSET.sbox_path + "/file/tex/thumb_def.jpg"
        return thumb_abs

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        event.ignore()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(event)
        event.ignore()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        event.ignore()

    def enterEvent(self, event):
        self.inter = True
        self.toggle_showIcon()

    def leaveEvent(self, event):
        self.inter = False
        self.toggle_showIcon()

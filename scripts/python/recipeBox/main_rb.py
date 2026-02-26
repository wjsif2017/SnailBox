import hou
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import *
from utils.snailWidget import Snail_Menu
from utils import mdViewer as md
from utils import capture as cap
from utils import ALLSET
from utils import display_status
from .module import *


class RB_Win(QWidget):
    def __init__(self):
        super().__init__()
        self._init_attributes()
        self.init_ui()
        self.init_data()

    def _init_attributes(self):
        self.current_lib_name = MYSET.lib_sort[0] if MYSET.lib_sort else ""
        self.manager = Recipe_Manager(self.current_lib_name) if self.current_lib_name else None
        self.md_editor = None
        self.items_widget = {}
        self.current_group = "All"
        self.current_id = None
        self.is_solo_fav = False
        self.is_show_ignore = False

    def init_ui(self):
        self._setup_window()
        self._create_layout()
        self._connect_signals()
        self.init_left_menu()
        self._setup_context_menu()

    def _setup_window(self):
        self.setObjectName("Snail_RB")
        self.setWindowTitle("SnailBox Recipe Box")
        self.resize(780, 650)
        icon_path = ALLSET.sbox_path + "/icons/SnailBox.svg"
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def _create_layout(self):
        self.ui = Ui_Main(self)
        mainlayout = QVBoxLayout(self)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.addWidget(self.ui)

    def _connect_signals(self):
        self.ui.tb_zip_export.clicked.connect(self.export_items)
        self.ui.tb_zip_import.clicked.connect(self.import_items)
        self.ui.tb_md.clicked.connect(self.view_edit_md)
        self.ui.tb_cap_img.clicked.connect(self.set_thumb_capture)
        self.ui.tb_cap_video.clicked.connect(self.set_thumb_video)
        self.ui.tb_folder.clicked.connect(self.open_item_folder)
        self.ui.tb_ignore.clicked.connect(self.show_ignore)
        self.ui.tb_delete.clicked.connect(self.del_items)
        self.ui.tb_fav.clicked.connect(self.solo_fav)
        self.ui.tb_set.clicked.connect(self.go_set)
        self.ui.btn_apply.clicked.connect(self.apply_item)
        self.ui.btn_refresh.clicked.connect(self.refresh)

        self.ui.cb_group.activated.connect(self.change_group)
        self.ui.lw_menu1.itemClicked.connect(self.menu_toggle)
        self.ui.list_thumb.itemClicked.connect(self.click_item)

    def _setup_context_menu(self):
        self.ui.list_thumb.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.list_thumb.customContextMenuRequested.connect(self.rightClickContext)

    def init_data(self):
        if not self.manager:
            return

        self.refresh()

    def refresh(self):
        self.refresh_groups()
        self.refresh_list()
        self.refresh_info()
        self.refresh_video()
        self.refresh_md()

    def on_info_edit_finished(self):
        if not self.current_id or not self.manager:
            return

        line_edit = self.sender()
        if not line_edit:
            return

        key = line_edit.property("field_key")
        if not key:
            return

        new_value = line_edit.text()
        if not new_value or new_value == "no_value":
            return

        self._update_item_field(key, new_value)

    def _update_item_field(self, key, value):
        success = self.manager.update_item(self.current_id, key, value)
        if success:
            self._refresh_item_widget(key, value)

    def _refresh_item_widget(self, key, value):
        widget = self.items_widget.get(self.current_id)
        if widget:
            if key in ("title", "pattern", "comment"):
                setattr(widget, key, value)
            widget.update_ui()

    def refresh_groups(self):
        self.ui.cb_group.clear()
        groups = self.manager.groups
        self.ui.cb_group.addItems(groups)
        if self.current_group and self.current_group in groups:
            self.ui.cb_group.setCurrentText(self.current_group)
        else:
            self.ui.cb_group.setCurrentIndex(0)
            self.current_group = groups[0]

    def init_left_menu(self):
        self.ui.lw_menu1.clear()

        if not MYSET.libs:
            self._handle_empty_library()
            return

        self._create_library_menu_items()
        self._update_selected_library()
        self.update_title()

    def _handle_empty_library(self):
        icon_path = f"{ALLSET.sbox_path}/file/icon02/10042.svg"
        icon = QtGui.QIcon(icon_path)
        item = QListWidgetItem(icon, "Add Lib")
        item.setSizeHint(QtCore.QSize(70, 60))
        item.setData(QtCore.Qt.UserRole, "")
        self.ui.lw_menu1.addItem(item)

    def _create_library_menu_items(self):
        for lib_name in MYSET.lib_sort:
            lib_dict = MYSET.libs.get(lib_name)
            if not lib_dict:
                continue

            item = self._create_lib_menu_item(lib_name, lib_dict)
            self.ui.lw_menu1.addItem(item)

    def _create_lib_menu_item(self, lib_name, lib_dict):
        icon_num = lib_dict.get("icon", "10001")
        icon_path = f"{ALLSET.sbox_path}/file/icon02/{icon_num}.svg"
        icon = QtGui.QIcon(icon_path)

        item = QListWidgetItem(icon, lib_name)
        item.setSizeHint(QtCore.QSize(70, 60))
        item.setData(QtCore.Qt.UserRole, lib_name)
        item.setToolTip(lib_name)

        return item

    def _update_selected_library(self):
        if self.current_lib_name in MYSET.libs and self.current_lib_name in MYSET.lib_sort:
            index = MYSET.lib_sort.index(self.current_lib_name)
            self.ui.lw_menu1.setCurrentRow(index)
        elif MYSET.lib_sort:
            self.current_lib_name = MYSET.lib_sort[0]
            self.ui.lw_menu1.setCurrentRow(0)

    def update_title(self):
        if self.current_lib_name and self.current_lib_name in MYSET.libs:
            self.ui.l_title.setText(self.current_lib_name)
        else:
            self.ui.l_title.setText("Recipe Box")

    def menu_toggle(self, item):
        lib_name = item.data(QtCore.Qt.UserRole)
        self.switch_library(lib_name)

    def switch_library(self, lib_name):
        if not lib_name:
            self.go_set()
            return

        if lib_name == self.current_lib_name:
            return

        if lib_name not in MYSET.libs:
            display_status(f"Snail_error_rb_main: Library '{lib_name}' not found")
            return

        self.current_lib_name = lib_name
        self.manager = Recipe_Manager(lib_name)
        self.refresh()
        self.update_title()

    def refresh_list(self):
        self.ui.list_thumb.clear()
        self.items_widget = {}

        items_dict = self.manager.get_items_dict(self.current_group)
        if not items_dict:
            return

        filtered_items = self._filter_items(items_dict)
        if not filtered_items:
            return

        self._update_current_id(filtered_items)
        self._create_item_widgets(filtered_items)

    def _filter_items(self, items_dict):
        filtered = {}
        for item_id, item_widget_dict in items_dict.items():
            if not item_widget_dict.get("fav") and self.is_solo_fav:
                continue
            if (
                item_widget_dict.get("ignore")
                and not self.is_show_ignore
                and self.current_group != "Ignore"
            ):
                continue
            filtered[item_id] = item_widget_dict
        return filtered

    def _update_current_id(self, items_dict):
        if self.current_id not in items_dict and items_dict:
            self.current_id = list(items_dict.keys())[0]

    def _create_item_widgets(self, items_dict):
        for item_id, item_widget_dict in items_dict.items():
            item_widget = Item_Widget(self, item_widget_dict)
            self.items_widget[item_id] = item_widget

            list_item = QListWidgetItem()
            list_item.setData(QtCore.Qt.UserRole, item_id)
            list_item.setSizeHint(item_widget.size())

            self.ui.list_thumb.addItem(list_item)
            self.ui.list_thumb.setItemWidget(list_item, item_widget)

    def change_group(self):
        self.group_index = self.ui.cb_group.currentIndex()
        group = self.ui.cb_group.currentText()
        self.current_group = group
        self.refresh()

    def click_item(self, item):
        item_id = item.data(QtCore.Qt.UserRole)
        if item_id != self.current_id:
            self.current_id = item_id
            self.refresh_info()
            self.refresh_video()
            self.refresh_md()

    def refresh_md(self):
        if not self.md_editor or not self.md_editor.isVisible():
            return
        md_file = self.manager.get_item_md(self.current_id)
        if md_file:
            self.md_editor.update_md_path(md_file)

    def refresh_info(self):
        self.ui.list_info.clear()

        if not self.current_id or not self.manager:
            return

        info_dict = self.manager.get_item_dict(self.current_id)
        if not info_dict:
            return

        for key in ["title", "name", "pattern", "author", "type", "comment"]:
            self._add_info_field(key, info_dict)

    def _is_editable_field(self, key):
        return key in {"title", "pattern", "comment"}

    def _add_info_field(self, key, info_dict):
        value = info_dict.get(key, "")
        if not value:
            value = "no_value"

        is_edit = self._is_editable_field(key)
        line_edit = self.ui.list_info.add_item(key, value, readOnly=not is_edit)

        if is_edit:
            line_edit.edit.setProperty("field_key", key)
            line_edit.edit.editingFinished.connect(self.on_info_edit_finished)

    def refresh_video(self):
        if not self.current_id or not self.manager:
            return

        info_dict = self.manager.get_item_dict(self.current_id)

        if not info_dict:
            return
        video_path = info_dict.get("video_abs", "")
        self.ui.video_viewer.update_video(video_path)

    def current_items(func):
        def wrapper(self, *args, **kwargs):
            sel_items = self.ui.list_thumb.selectedItems()
            if not sel_items:
                msg = "Please select one item"
                hou.ui.displayMessage(msg)
                return
            ids = [btnItem.data(QtCore.Qt.UserRole) for btnItem in sel_items]
            return func(self, ids, *args, **kwargs)

        return wrapper

    @current_items
    def set_Tex(self, ids):
        id = ids[-1]
        item = self.manager.items.get(id)
        if item and hasattr(item, "set_tex"):
            item.set_tex()

    @current_items
    def set_thumb_capture(self, ids):
        id = ids[-1]
        item_thumb_dict = self.manager.get_item_dict(id)
        if not item_thumb_dict:
            return
        thumb_abs = item_thumb_dict.get("thumb_abs")
        capImg = cap.CaptureImage(thumb_abs)
        capImg.finish_sig.connect(lambda: self.on_item_updated(id))
        capImg.show()

    @current_items
    def set_thumb_video(self, ids):
        id = ids[-1]
        item_thumb_dict = self.manager.get_item_dict(id)
        if not item_thumb_dict:
            return
        video_abs = item_thumb_dict.get("video_abs")

        self.ui.video_viewer.release()

        self._capture_window = cap.CaptureVideo(video_abs)
        self._capture_window.finish_sig.connect(self.refresh_video)
        self._capture_window.show()

    @current_items
    def open_item_folder(self, ids):
        id = ids[-1]
        self.manager.open_item_folder(id)

    def on_item_updated(self, id):
        item_widget = self.items_widget.get(id)
        if not item_widget:
            return
        item_widget_dict = self.manager.get_item_dict(id)
        item_widget.update(item_widget_dict)

    @current_items
    def items_add_group(self, ids):
        result = hou.ui.readInput("新组名:", buttons=("OK", "Cancel"))
        if not result:
            return
        group = result[1]
        self.items_modify_group(group)

    @current_items
    def items_modify_group(self, ids, group, *args, **kwargs):
        self.manager.items_modify_group(ids, group)
        self.refresh()

    @current_items
    def toggle_fav(self, ids):
        self.manager.items_toggle_fav(ids)
        for id in ids:
            self.on_item_updated(id)

    @current_items
    def toggle_ignore(self, ids):
        self.manager.items_toggle_ignore(ids)
        self.refresh()

    @current_items
    def apply_item(self, ids):
        id = ids[-1]
        self.manager.apply_item(id)

    def apply_item2(self, id):
        self.manager.apply_item(id)

    @current_items
    def del_items(self, ids):
        count = len(ids)
        msg = f"Are you sure you want to delete {count} Recipe(s)?"
        confirm = hou.ui.displayMessage(msg, buttons=("Cancel", "OK"), close_choice=0)
        if confirm != 1:
            return
        self.ui.video_viewer.release()
        self.manager.del_items(ids)
        self.refresh()

    @current_items
    def edit_item(self, ids):
        id = ids[-1]
        self.manager.edit_item(id)

    @current_items
    def view_edit_md(self, ids):
        id = ids[-1]
        self.current_id = id

        if not self.md_editor:
            self._create_md_editor()
        elif not self.md_editor.isVisible():
            self.md_editor.show()

        self.refresh_md()

    def _create_md_editor(self):
        self.md_editor = md.MdViewer()
        self._position_md_editor()
        self.md_editor.show()

    def _position_md_editor(self):
        rb_frame_geo = self.frameGeometry()
        rb_geo = self.geometry()
        md_width = 460

        self.md_editor.resize(md_width, rb_geo.height())
        self.md_editor.move(rb_frame_geo.right() + 4, rb_frame_geo.top())

    @current_items
    def export_items(self, ids):
        base_dir = self._select_export_directory()
        if not base_dir:
            return

        base_dir = self._clean_directory_path(base_dir)
        self.manager.export_items(ids, base_dir)

    def _select_export_directory(self):
        return hou.ui.selectFile(
            title="Export Recipes (Select Directory)",
            file_type=hou.fileType.Directory,
            collapse_sequences=False,
        )

    def _clean_directory_path(self, path):
        if path.endswith("/"):
            path = path[:-1]
        return path

    def import_items(self):
        if not self.manager:
            hou.ui.displayMessage("No library available")
            return

        zip_paths = self._select_import_files()
        if not zip_paths:
            return

        zip_paths = self._process_import_paths(zip_paths)
        self.manager.import_items(zip_paths)
        self.refresh()

    def _select_import_files(self):
        return hou.ui.selectFile(
            title="Import Recipe(s) from ZIP",
            file_type=hou.fileType.Any,
            pattern="recipe_*.zip",
            collapse_sequences=False,
            multiple_select=True,
        )

    def _process_import_paths(self, zip_paths):
        if isinstance(zip_paths, str):
            zip_paths = [p.strip() for p in zip_paths.split(";") if p.strip()]

        return [hou.text.expandString(path) for path in zip_paths]

    def solo_fav(self):
        self.is_solo_fav = self.ui.tb_fav.isChecked()
        self.refresh()

    def show_ignore(self):
        self.is_show_ignore = self.ui.tb_ignore.isChecked()
        self.refresh()

    def go_set(self):
        ui_set = Ui_Setting(self)
        ui_set.show()

    def refresh_manager(self):
        self._reset_library()
        if not self.current_lib_name:
            return
        self._refresh_after_library_change()

    def _reset_library(self):
        self.current_lib_name = MYSET.lib_sort[0] if MYSET.lib_sort else ""
        if self.current_lib_name:
            self.manager = Recipe_Manager(self.current_lib_name)
        else:
            self.manager = None

    def _refresh_after_library_change(self):
        self.init_left_menu()
        self.ui.cb_group.clear()
        self.ui.cb_group.addItems(self.manager.groups)
        self.ui.cb_group.setCurrentText("All")
        self.current_group = "All"
        self.refresh_list()

    def create_submenu_group(self):
        submenu = Snail_Menu("Change group")
        submenu.addAction("Add group", self.items_add_group)
        submenu.addAction("Remove group", lambda: self.items_modify_group(""))

        items_group = self.manager.get_items_group()
        if not items_group:
            return submenu

        self._add_group_menu_items(submenu, items_group)
        return submenu

    def _add_group_menu_items(self, submenu, items_group):
        for group in items_group:
            submenu.addAction(group, lambda g=group: self.items_modify_group(g))

    def rightClickContext(self, position=None):
        menu = Snail_Menu()
        selected_items = self.ui.list_thumb.selectedItems()

        if selected_items:
            self._create_context_menu_items(menu)
        else:
            menu.addAction("刷新", self.refresh_list)

        menu.exec_(self.ui.list_thumb.viewport().mapToGlobal(position))

    def _create_context_menu_items(self, menu):
        submenu_group = self.create_submenu_group()
        menu.addAction("Apply", self.apply_item)
        menu.addAction("Edit", self.edit_item)
        menu.addAction("View MD", self.view_edit_md)
        menu.addAction("Capture Thumb", self.set_thumb_capture)
        menu.addAction("Capture Video", self.set_thumb_video)
        menu.addMenu(submenu_group)
        menu.addAction("Export / Share", self.export_items)
        menu.addAction("Toggle Favorite", self.toggle_fav)
        menu.addAction("Toggle Ignore", self.toggle_ignore)
        menu.addAction("Delete", self.del_items)
        menu.addAction("Open Folder", self.open_item_folder)

    def closeEvent(self, event):
        if self.md_editor:
            self.md_editor.close()
        event.accept()


def main_show():
    try:
        houMainWindow = hou.qt.mainWindow()
        getChildWin = houMainWindow.findChild(QWidget, "Snail_RB")
        getChildWin.close()
        getChildWin.deleteLater()
    except:
        pass
    if not ALLSET.verify_sig("rb"):
        return
    mywin2 = RB_Win()
    mywin2.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    mywin2.show()

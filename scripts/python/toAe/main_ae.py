import hou
import traceback
from utils import QtCore, QtGui, QWidget, QVBoxLayout
from utils import ALLSET, display_status
from .module import ae_item
from .module import ae_ui

import importlib
importlib.reload(ae_ui)
importlib.reload(ae_item)


class Ae_win(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.manager = ae_item.Ae_Manager()

        self.ui = ae_ui.Ui_Main(self, self.manager)

        self._setup_window()

    def _setup_window(self):
        self.setObjectName("SnailBox_AeBridger")
        self.setWindowTitle("SnailBox Ae Bridger")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)
        main_layout.addWidget(self.ui)
        self.resize(650, 650)

    def on_refresh_clicked(self):
        self.manager.update_from_houdini()

        self.ui.refresh()

        self.manager.refresh_items()

        self._update_item_list()

    def on_node_dropped(self, parm_paths, node_paths):
        if parm_paths or not node_paths:
            return

        path_list = node_paths.split()
        self.add_items(path_list)

    def add_items(self, path_list):
        added_count = 0
        for path in path_list:
            try:
                node = hou.node(path)
                if not node:
                    raise ValueError(f"Invalid node path: {path}")
                node_id = node.sessionId()
                item = self.manager.add_item(node_id)
                if item:
                    added_count += 1
            except ValueError as e:
                display_status(f"Snail_error_ae: {e}")
            except Exception as e:
                display_status(f"Snail_error_ae: {e}\n{traceback.format_exc()}")

        if added_count > 0:
            self._update_item_list()

    def _update_item_list(self):
        self.ui.clear_item_list()

        items = self.manager.get_all_items()
        if not items:
            return
        for item in items.values():
            try:
                self._add_item_widget(item)
            except Exception as e:
                display_status(f"Snail_error_ae: {e}\n{traceback.format_exc()}")

    def _add_item_widget(self, item):
        if item.type == ae_item.NodeType.OBJ_CAMERA:
            widget = ae_ui.ObjCamItemWidget(item, self)
        elif item.type == ae_item.NodeType.OBJ_LIGHT:
            widget = ae_ui.ObjLightItemWidget(item, self)
        elif item.type == ae_item.NodeType.SOP_NULL:
            widget = ae_ui.SopNullItemWidget(item, self)
        else:
            widget = ae_ui.ObjNullItemWidget(item, self)

        self.ui.add_item_widget(widget)

    def delete_item(self, item_id):
        self.manager.remove_item(item_id)
        self._update_item_list()


def main_show():
    houMainWindow = hou.qt.mainWindow()
    get_child_win = houMainWindow.findChild(QWidget, "SnailBox_AeBridger")
    if get_child_win:
        get_child_win.close()
        get_child_win.deleteLater()
    if not ALLSET.verify_sig("ae"):
        return
    win = Ae_win()
    win.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    win.show()

"""
RecipeBox - Houdini Recipe 管理插件

提供 Recipe 的浏览、管理和应用功能。

TODO:
    1. 在线库功能: 支持从 API 从服务器获取 recipe list 和详情
    2. 搜索功能: 支持本地和在线搜索
    3. Assets 保存: 支持通过 add recipe 时保存节点中的 assets
    4. comment 多行文字
"""

import hou
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import *
from utils import mdViewer as md
from utils import ALLSET
from .module import MYSET, rb_item, rb_ui

import importlib
importlib.reload(rb_ui)
importlib.reload(rb_item)


class RB_Win(QWidget):
    """
    RecipeBox 主窗口类（协调者角色）

    只负责：manager 创建、跨组件协调、MD 编辑器管理
    所有 UI 操作（包括文件对话框）都在 Ui_Main 中完成
    """

    def __init__(self):
        """初始化主窗口"""
        super().__init__()
        self._init_attributes()
        self._setup_window()
        self.ui.refresh()

    def _init_attributes(self):
        """初始化属性"""
        MYSET.init_data()
        self.current_lib_name = MYSET.lib_sort[0] if MYSET.lib_sort else ""
        self.manager = rb_item.Recipe_Manager(self.current_lib_name)
        self.md_editor = None

    def _setup_window(self):
        """设置窗口属性和 UI"""
        self.setObjectName("Snail_RB")
        self.setWindowTitle("SnailBox Recipe Box")
        self.resize(780, 650)
        icon_path = ALLSET.sbox_path + "/icons/SnailBox.svg"
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui = rb_ui.Ui_Main(self, self.manager)
        mainlayout = QVBoxLayout(self)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.addWidget(self.ui)

    def switch_library(self, lib_name):
        """切换到指定库

        Args:
            lib_name: 库名称
        """
        if lib_name == self.current_lib_name:
            return
        if lib_name not in MYSET.libs:
            print(f"Library '{lib_name}' not found")
            return
        self.current_lib_name = lib_name
        self.manager = rb_item.Recipe_Manager(lib_name)
        self.ui.refresh()

    def refresh_manager(self):
        """刷新 Recipe 管理器（在库列表变化后由 Ui_Setting 调用）"""
        if not self.current_lib_name:
            self.current_lib_name = MYSET.lib_sort[0] if MYSET.lib_sort else ""
        if self.current_lib_name:
            self.manager = rb_item.Recipe_Manager(self.current_lib_name)
            self.ui.refresh_after_lib_change()
        else:
            self.manager = None
        
    # ========================================================================
    # MD 编辑器管理
    # ========================================================================

    def view_edit_md(self, ids):
        """
        查看/编辑选中 Recipe 的 Markdown 文档

        Args:
            ids: 选中的 Recipe ID 列表
        """
        if not ids:
            hou.ui.displayMessage("Please select one item")
            return
        id = ids[-1]
        if not self.md_editor:
            self.md_editor = md.MdViewer()
            rb_frame_geo = self.frameGeometry()
            rb_geo = self.geometry()
            self.md_editor.resize(460, rb_geo.height())
            self.md_editor.move(rb_frame_geo.right() + 4, rb_frame_geo.top())
        self.md_editor.show()
        if self.md_editor.isMinimized():
            self.md_editor.showNormal()
        md_file = self.manager.get_item_md(id)
        if md_file:
            self.md_editor.update_md_path(md_file)

    # ========================================================================
    # 其他
    # ========================================================================

    def go_set(self):
        """打开设置界面"""
        ui_set = rb_ui.Ui_Setting(self)
        ui_set.show()

    def closeEvent(self, event):
        """
        窗口关闭事件：关闭 Markdown 编辑器和视频播放器

        Args:
            event: 关闭事件
        """
        if self.md_editor:
            self.md_editor.close()
        self.ui.video_viewer.release()
        MYSET.save_user_json()
        event.accept()


def main_show():
    """
    主入口函数：显示 RecipeBox 主窗口

    关闭已存在的窗口，验证签名，创建并显示新窗口。
    """
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

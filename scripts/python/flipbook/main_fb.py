"""
Flipbook 主窗口模块 (重构版)

本模块实现前后端分离后的主窗口类。

架构:
    Fb_win (主窗口)
    ├── Fb_Manager (后端 - 数据管理)
    └── Ui_Main (前端 - UI 组件)

职责:
    - 连接前后端
    - 管理 ItemTextWidget 生命周期
    - 处理 UI 回调事件
"""

import hou
from utils import QtCore, QtGui, QWidget, QVBoxLayout
from utils import ALLSET, display_status
from .module import fb_item, fb_ui

import importlib
importlib.reload(fb_ui)
importlib.reload(fb_item)

# ============================================================================
# Fb_win - 主窗口类
# ============================================================================


class Fb_win(QWidget):
    """
    Flipbook 主窗口

    薄协调层，连接前端 UI (Ui_Main) 和后端管理器 (Fb_Manager)。

    职责:
        - 创建和管理 UI 组件
        - 处理来自 UI 的回调事件
        - 协调前后端数据同步

    Args:
        parent: 父窗口，通常为 Houdini 主窗口
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # 后端管理器
        self.manager = fb_item.Fb_Manager()
        # 前端 UI
        self.ui = fb_ui.Ui_Main(self)

        self._setup_window()
        self._init_data()

    def _setup_window(self):
        """设置窗口属性"""
        self.setObjectName("Snail_fb")
        self.setWindowTitle("SnailBox Flipbook")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)
        main_layout.addWidget(self.ui)
        self.resize(650, 650)

    def _init_data(self):
        """初始化数据

        加载 Last Input 预设并更新文字项列表。
        """
        self.ui.refresh()
        self._update_text_item_list()

    # =========================================================================
    # 回调方法 - 供 Ui_Main 和 ItemTextWidget 调用
    # =========================================================================

    def on_add_text_clicked(self):
        """添加文字项回调

        由 Ui_Main._on_add_text_clicked() 调用。
        """
        item_id = self.manager.add_text()
        if item_id:
            self._update_text_item_list()

    def on_delete_text(self, item_id):
        """删除文字项回调

        由 ItemTextWidget._on_close_clicked() 调用。

        Args:
            item_id: 要删除的文字项 ID
        """
        self.manager.remove_text(item_id)
        self._update_text_item_list()

    def on_text_item_changed(self):
        """文字项属性变更回调

        由 ItemTextWidget 的各个属性变更方法调用。
        触发 viewport 更新以显示最新文字。
        """
        self.manager.show_text()

    def _update_text_item_list(self):
        """更新文字项列表

        从 Fb_Manager 同步文字项到 UI。
        """
        self.ui.clear_item_list()
        for item_id, item in self.manager.text_items.items():
            try:
                widget = fb_ui.ItemTextWidget(item_id, self)
                self.ui.add_item_widget(widget)
            except Exception as e:
                display_status(f"Snail_error_fb: Failed to create text widget for item {item_id}: {e}")
        self.manager.show_text()

    # =========================================================================
    # 刷新和关闭
    # =========================================================================

    def refresh(self):
        """刷新数据

        由 callInterface() 面板重入时调用。
        """
        self.ui.refresh()

    def closeEvent(self, event):
        """关闭事件

        保存 Last Input 到 Houdini 节点后关闭窗口。

        Args:
            event: QCloseEvent
        """
        self.manager.save_preset_close()
        super().closeEvent(event)


# ============================================================================
# 入口函数
# ============================================================================


def main_show():
    """调用主界面 (独立窗口)"""
    try:
        houMainWindow = hou.qt.mainWindow()
        getChildWin = houMainWindow.findChild(QWidget, "Snail_fb")
        if getChildWin:
            getChildWin.close()
            getChildWin.deleteLater()
    except:
        pass

    if not ALLSET.verify_sig("fb"):
        return
    mywin = Fb_win()
    mywin.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    mywin.show()


def callInterface():
    """调用界面 (Python Panel)"""
    panel = None
    pane_name = "SnailBox_Fb"
    if not ALLSET.verify_sig("fb"):
        return
    for pane in hou.ui.floatingPaneTabs():
        fp = pane.floatingPanel()
        if fp and fp.name() == pane_name:
            fb_win = pane.activeInterfaceRootWidget()
            fb_win.refresh()
            panel = pane
    if not panel:
        panel = hou.ui.curDesktop().createFloatingPaneTab(
            hou.paneTabType.PythonPanel, (500, 500), (500, 650), pane_name
        )
    if panel:
        panel.showToolbar(0)
        panel.expandToolbar(0)
    fp = panel.floatingPanel()
    if fp:
        fp.setName(pane_name)
        try:
            fp.qtParentWindow().showNormal()
        except:
            pass

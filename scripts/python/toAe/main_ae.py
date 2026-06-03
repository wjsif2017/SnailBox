"""
toAe 主窗口模块 (重构版)

本模块实现前后端分离后的主窗口类。

架构:
    Ae_win (主窗口)
    ├── Ae_Manager (后端 - 数据管理)
    └── Ui_Main (前端 - UI 组件)

职责:
    - 连接前后端
    - 管理 Item Widgets
    - 处理拖放节点
    - 同步 Houdini 数据

刷新逻辑:
    1. Manager 从 Houdini 更新配置（fps、帧范围等）
    2. 更新设置区域 UI
    3. 刷新所有现有 Item 的属性（自动清理不存在的节点）
    4. 重建 Item 列表 UI
"""

import hou
import traceback
from utils import QtCore, QtGui, QWidget, QVBoxLayout
from utils import ALLSET, display_status
from .module import ae_item
from .module import ae_ui

# 开发模式：重新加载模块（仅用于开发调试）
import importlib
importlib.reload(ae_ui)
importlib.reload(ae_item)

# ============================================================================
# Ae_win - 主窗口类
# ============================================================================


class Ae_win(QWidget):
    """
    toAe 主窗口

    连接前端 UI 和后端 Manager，处理所有用户交互。
    """

    def __init__(self, parent=None):
        """初始化主窗口"""
        super().__init__(parent)

        # 创建后端管理器（已包含 Houdini 数据）
        self.manager = ae_item.Ae_Manager()

        # 创建前端 UI（传入 manager）
        self.ui = ae_ui.Ui_Main(self, self.manager)

        # 设置窗口
        self._setup_window()

    def _setup_window(self):
        """设置窗口属性"""
        self.setObjectName("SnailBox_AeBridger")
        self.setWindowTitle("SnailBox Ae Bridger")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)
        main_layout.addWidget(self.ui)
        self.resize(650, 650)

    # =========================================================================
    # 事件处理
    # =========================================================================

    def on_refresh_clicked(self):
        """刷新按钮点击 - 重新同步所有 Item 数据（供 Ui_Main 调用）

        流程:
            1. Manager 从 Houdini 更新配置（fps、帧范围等）
            2. 更新设置区域 UI
            3. 刷新所有现有 Item 的属性
            4. 重建 Item 列表 UI（自动清理不存在的节点）
        """
        # 1. 从 Houdini 更新配置
        self.manager.update_from_houdini()

        # 2. 更新设置区域 UI
        self.ui.refresh()

        # 3. 刷新所有现有 Item 的属性（自动清理不存在的节点）
        self.manager.refresh_items()

        # 4. 重建 Item 列表 UI
        self._update_item_list()

    # =========================================================================
    # 拖放节点处理
    # =========================================================================

    def on_node_dropped(self, parm_paths, node_paths):
        """处理拖放节点（供 Ui_Main 调用）"""
        if parm_paths or not node_paths:
            return

        # 解析节点路径
        path_list = node_paths.split()
        self.add_items(path_list)

    def add_items(self, path_list):
        """
        添加节点列表（通过路径）

        Args:
            path_list: 节点路径列表
        """
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
                # 已知的业务错误，显示状态消息
                display_status(f"Snail_error_ae: {e}")
            except Exception as e:
                # 未知异常，打印完整调试信息
                display_status(f"Snail_error_ae: {e}\n{traceback.format_exc()}")

        # 如果有节点被添加，刷新 UI
        if added_count > 0:
            self._update_item_list()

    # =========================================================================
    # UI 同步方法
    # =========================================================================

    def _update_item_list(self):
        """从 Manager 同步 Items 到 UI"""
        # 清空当前列表
        self.ui.clear_item_list()

        # 添加所有 items（get_all_items 返回字典，使用 .values()）
        items = self.manager.get_all_items()
        if not items:
            return
        for item in items.values():
            try:
                self._add_item_widget(item)
            except Exception as e:
                # 未知异常，打印完整调试信息
                display_status(f"Snail_error_ae: {e}\n{traceback.format_exc()}")

    def _add_item_widget(self, item):
        """添加单个 Item Widget"""
        # 根据类型创建对应的 Widget
        if item.type == ae_item.NodeType.OBJ_CAMERA:
            widget = ae_ui.ObjCamItemWidget(item, self)
        elif item.type == ae_item.NodeType.OBJ_LIGHT:
            widget = ae_ui.ObjLightItemWidget(item, self)
        elif item.type == ae_item.NodeType.SOP_NULL:
            widget = ae_ui.SopNullItemWidget(item, self)
        else:  # OBJ_NULL (默认)
            widget = ae_ui.ObjNullItemWidget(item, self)

        # 添加到列表
        self.ui.add_item_widget(widget)

    def delete_item(self, item_id):
        """
        删除指定的 Item（供 widget 内部调用）

        Args:
            item_id: Item 的唯一标识
        """
        self.manager.remove_item(item_id)
        self._update_item_list()


# ============================================================================
# 入口函数
# ============================================================================


def main_show():
    """调用主界面"""
    # 查找已存在的窗口
    houMainWindow = hou.qt.mainWindow()
    get_child_win = houMainWindow.findChild(QWidget, "SnailBox_AeBridger")
    if get_child_win:
        get_child_win.close()
        get_child_win.deleteLater()
    if not ALLSET.verify_sig("ae"):
        return
    # 创建新窗口
    win = Ae_win()
    win.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    win.show()

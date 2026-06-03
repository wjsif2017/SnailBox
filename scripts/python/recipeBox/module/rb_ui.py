import os
import hou
from pathlib import Path
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import *
from hrecipes import storage
from hrecipes.ui.nodepresetdialog import NodePresetDialog
from utils import *
from utils.videoViewer import VideoViewer
from utils import capture as cap
from .rb_set import MYSET


class Ui_Main(QWidget):
    """
    主界面布局类

    职责：
        - 创建和管理所有 UI 控件和布局
        - 所有信号槽处理都在内部完成
        - 所有 UI 刷新逻辑都在内部完成
        - 库菜单、列表交互、信息面板、右键菜单全部自主管理
        - 通过回调函数调用父窗口方法处理跨组件操作（文件对话框、MD 编辑器）

    设计原则：
        - 拥有完整 UI 自主权，不依赖父窗口操作任何 UI 控件
        - 所有 UI 状态（_current_id, _current_group 等）内部管理
    """

    def __init__(self, parent, manager):
        """初始化主界面

        Args:
            parent: 父窗口 (RB_Win)
            manager: Recipe_Manager 实例
        """
        super().__init__(parent)
        self.pa = parent
        self._manager = manager

        # UI 状态
        self._current_id = None
        self._current_group = "All"
        self._is_solo_fav = False
        self._is_show_ignore = False
        self.items_widget = {}

        self._setup_main_layout()
        self._connect_internal_signals()

    # ========================================================================
    # 布局创建
    # ========================================================================

    def _setup_main_layout(self):
        """设置主布局"""
        layout_main = QHBoxLayout(self)
        layout_main.setSpacing(0)
        layout_main.setContentsMargins(0, 0, 0, 0)

        # 左侧菜单区域
        layout_menu = self._create_left_menu()
        layout_main.addLayout(layout_menu)

        # 右侧主内容区域
        layout_main2 = self._create_main_content()
        layout_main.addLayout(layout_main2)

    def _create_left_menu(self):
        """
        创建左侧菜单区域

        Returns:
            QVBoxLayout: 左侧菜单布局
        """
        layout_menu = QVBoxLayout()

        # 创建左侧菜单框架
        self.leftmenu = self._create_leftmenu_frame()
        layout_menu.addWidget(self.leftmenu)

        return layout_menu

    def _create_leftmenu_frame(self):
        """
        创建左侧菜单框架

        Returns:
            QFrame: 左侧菜单框架
        """
        frame = QFrame(self)
        frame.setFixedWidth(70)
        frame.setStyleSheet("border:0;\n" "background-color: #2d2d2d;")
        frame.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)

        # 设置布局
        self.layout_leftmenu = QVBoxLayout(frame)
        self.layout_leftmenu.setContentsMargins(0, 0, 0, 0)
        self.layout_leftmenu.setSpacing(2)

        # 添加顶部间隔
        self.layout_leftmenu.addItem(QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # 创建库菜单列表（传入 frame 作为父控件）
        self.lw_menu1 = self._create_library_menu(frame)
        self.layout_leftmenu.addWidget(self.lw_menu1)

        # 添加底部间隔
        self.layout_leftmenu.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))

        return frame

    def _create_library_menu(self, parent):
        """
        创建库菜单列表

        Args:
            parent: 父控件

        Returns:
            QListWidget: 库菜单列表控件
        """
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
        """
        创建右侧主内容区域

        Returns:
            QVBoxLayout: 主内容布局
        """
        layout = QVBoxLayout()

        # 顶部标题栏
        layout_top = self._create_top_bar()
        layout.addLayout(layout_top)

        # 工具栏
        layout_tool = self._create_tool_bar()
        layout.addLayout(layout_tool)

        # 中间内容区（预览图列表 + 信息面板）
        splitter_v = self._create_center_splitter()
        layout.addWidget(splitter_v)

        # 底部按钮栏
        layout_bottom = self._create_bottom_bar()
        layout.addLayout(layout_bottom)

        return layout

    def _create_top_bar(self):
        """
        创建顶部标题栏

        Returns:
            QHBoxLayout: 顶部栏布局
        """
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
        """
        创建工具栏

        Returns:
            QHBoxLayout: 工具栏布局
        """
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # 创建工具按钮
        self._create_tool_buttons()

        layout.addItem(spacer)
        layout.addWidget(self.tb_zip_export)
        layout.addWidget(self.tb_zip_import)
        layout.addWidget(self.tb_cap_img)
        layout.addWidget(self.tb_cap_video)
        layout.addWidget(self.tb_md)
        layout.addWidget(self.tb_folder)
        layout.addWidget(self.tb_ignore)
        layout.addWidget(self.tb_delete)
        layout.addWidget(self.tb_fav)

        return layout

    def _create_tool_buttons(self):
        """创建工具栏按钮"""
        self.tb_zip_export = Snail_IconBtn("snail_zip0", "Export recipe zip")
        self.tb_zip_import = Snail_IconBtn("snail_zip1", "Import recipe zip")
        self.tb_cap_img = Snail_IconBtn("snail_matThumb2", "Capture thumb")
        self.tb_cap_video = Snail_IconBtn("snail_rec_on", "Capture video")
        self.tb_md = Snail_IconBtn("snail_md", "View and edit MD")
        self.tb_folder = Snail_IconBtn("BUTTONS_folder", "Item folder")
        self.tb_ignore = Snail_IconBtn_toggle("snail_ignore1", "snail_ignore2", "Toggle ignore")
        self.tb_delete = Snail_IconBtn("COMMON_delete", "Delete")
        self.tb_fav = Snail_IconBtn_toggle("snail_fav1", "snail_fav2", "Solo fav")

    def _create_center_splitter(self):
        """
        创建中间内容分割器（包含预览图列表和信息面板）

        Returns:
            QSplitter: 垂直分割器
        """
        splitter_v = QSplitter()
        splitter_v.setOrientation(QtCore.Qt.Vertical)

        # 预览图列表
        self.list_thumb = self._create_thumb_list()
        splitter_v.addWidget(self.list_thumb)

        # 信息面板
        info_widget = self._create_info_splitter()
        splitter_v.addWidget(info_widget)

        splitter_v.setSizes([120, 20])

        return splitter_v

    def _create_thumb_list(self):
        """
        创建预览图列表

        Returns:
            QListWidget: 预览图列表控件
        """
        list_widget = QListWidget(self)
        list_widget.setObjectName("list_thumb")
        list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        list_widget.setProperty("isWrapping", True)
        list_widget.setResizeMode(QListView.Adjust)
        list_widget.setSpacing(4)
        list_widget.setViewMode(QListView.IconMode)
        return list_widget

    def _create_info_splitter(self):
        """
        创建信息面板分割器（列表信息 + 视频预览）

        Returns:
            QSplitter: 水平分割器
        """
        splitter = QSplitter()
        splitter.setOrientation(QtCore.Qt.Horizontal)

        # 列表信息
        self.list_info = Snail_List2(self)
        self.list_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # 视频预览
        self.video_viewer = VideoViewer()

        splitter.addWidget(self.list_info)
        splitter.addWidget(self.video_viewer)
        splitter.setSizes([100, 100])

        return splitter

    def _create_bottom_bar(self):
        """
        创建底部按钮栏

        Returns:
            QHBoxLayout: 底部栏布局
        """
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)

        # 创建底部按钮
        self._create_bottom_buttons()

        layout.addWidget(self.tb_set)
        layout.addWidget(self.tb_bz)
        layout.addWidget(self.tb_help)
        layout.addWidget(self.btn_add_recipe)
        layout.addWidget(self.btn_apply)
        layout.addWidget(self.btn_refresh)

        return layout

    def _create_bottom_buttons(self):
        """创建底部按钮"""
        self.tb_bz = Snail_IconBtn_bz()
        self.tb_help = Snail_IconBtn_help()
        self.tb_set = Snail_IconBtn("snail_set", "Settings")
        self.btn_refresh = Snail_Btn("Refresh")
        self.btn_apply = Snail_Btn("Apply")
        self.btn_add_recipe = Snail_Btn("Add Recipe")

    # ========================================================================
    # 信号连接
    # ========================================================================

    def _connect_internal_signals(self):
        """连接所有内部信号槽"""
        # 工具栏按钮
        self.tb_zip_export.clicked.connect(self._on_export_clicked)
        self.tb_zip_import.clicked.connect(self._on_import_clicked)
        self.tb_cap_img.clicked.connect(self._on_cap_img_clicked)
        self.tb_cap_video.clicked.connect(self._on_cap_video_clicked)
        self.tb_md.clicked.connect(self._on_md_clicked)
        self.tb_folder.clicked.connect(self._on_folder_clicked)
        self.tb_ignore.clicked.connect(self._on_ignore_toggled)
        self.tb_delete.clicked.connect(self._on_delete_clicked)
        self.tb_fav.clicked.connect(self._on_fav_toggled)
        self.tb_set.clicked.connect(self._on_set_clicked)
        self.btn_apply.clicked.connect(self._on_apply_clicked)
        self.btn_refresh.clicked.connect(self._on_refresh_clicked)
        self.btn_add_recipe.clicked.connect(self._on_add_recipe_clicked)

        # 下拉框和列表
        self.cb_group.activated.connect(self._on_group_changed)
        self.lw_menu1.itemClicked.connect(self._on_library_clicked)
        self.list_thumb.itemClicked.connect(self._on_item_clicked)

        # 右键菜单
        self.list_thumb.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.list_thumb.customContextMenuRequested.connect(self._on_right_click)

    # ========================================================================
    # 工具栏按钮处理
    # ========================================================================

    def _on_export_clicked(self):
        """导出按钮点击"""
        ids = self._get_selected_ids()
        if ids:
            self._export_items(ids)

    def _on_import_clicked(self):
        """导入按钮点击"""
        self._import_items()

    def _on_cap_img_clicked(self):
        """截图按钮点击"""
        ids = self._get_selected_ids()
        if ids:
            self._capture_thumb(ids)

    def _on_cap_video_clicked(self):
        """截视频按钮点击"""
        ids = self._get_selected_ids()
        if ids:
            self._capture_video(ids)

    def _on_md_clicked(self):
        """MD 文档按钮点击"""
        ids = self._get_selected_ids()
        if ids:
            self.pa.view_edit_md(ids)

    def _on_folder_clicked(self):
        """打开文件夹按钮点击"""
        ids = self._get_selected_ids()
        if ids:
            self.pa.manager.open_item_folder(ids[-1])

    def _on_ignore_toggled(self):
        """忽略过滤按钮切换"""
        self._is_show_ignore = self.tb_ignore.isChecked()
        self._refresh_list()

    def _on_delete_clicked(self):
        """删除按钮点击"""
        ids = self._get_selected_ids()
        self._delete_items(ids)

    def _on_fav_toggled(self):
        """收藏过滤按钮切换"""
        self._is_solo_fav = self.tb_fav.isChecked()
        self._refresh_list()

    def _on_set_clicked(self):
        """设置按钮点击"""
        self.pa.go_set()

    def _on_apply_clicked(self):
        """应用按钮点击"""
        ids = self._get_selected_ids()
        if ids:
            self.pa.manager.apply_item(ids[-1])

    def _on_refresh_clicked(self):
        """刷新按钮点击"""
        if hasattr(self.pa, "refresh_manager"):
            self.pa.refresh_manager()
        self.refresh()

    def _on_add_recipe_clicked(self):
        """Add Recipe 按钮点击"""
        self.pa.manager.add_recipe(on_accept=self.refresh)

    # ========================================================================
    # 文件导入导出
    # ========================================================================

    def _export_items(self, ids):
        """
        导出 Recipe 为 zip 文件

        Args:
            ids: 选中的 Recipe ID 列表
        """
        if not ids:
            hou.ui.displayMessage("Please select one item")
            return
        base_dir = hou.ui.selectFile(
            title="Export Recipes (Select Directory)",
            file_type=hou.fileType.Directory,
            collapse_sequences=False,
        )
        if not base_dir:
            return
        if base_dir.endswith("/"):
            base_dir = base_dir[:-1]
        self.pa.manager.export_items(ids, base_dir)

    def _import_items(self):
        """从 zip 文件导入 Recipe"""
        manager = self.pa.manager
        if not manager:
            hou.ui.displayMessage("No library available")
            return
        zip_paths = hou.ui.selectFile(
            title="Import Recipe(s) from ZIP",
            file_type=hou.fileType.Any,
            pattern="recipe_*.zip",
            collapse_sequences=False,
            multiple_select=True,
        )
        if not zip_paths:
            return
        if isinstance(zip_paths, str):
            zip_paths = [p.strip() for p in zip_paths.split(";") if p.strip()]
        zip_paths = [hou.text.expandString(path) for path in zip_paths]
        manager.import_items(zip_paths)
        self.refresh()

    def _capture_thumb(self, ids):
        """截图设置预览图"""
        if not ids:
            return
        id = ids[-1]
        info_dict = self.pa.manager.get_item_dict(id)
        if not info_dict:
            return
        thumb_abs = info_dict.get("thumb_abs")
        cap_img = cap.CaptureImage(thumb_abs)
        cap_img.finish_sig.connect(lambda: self.on_item_updated(id))
        cap_img.show()

    def _capture_video(self, ids):
        """截视频设置预览"""
        if not ids:
            return
        id = ids[-1]
        info_dict = self.pa.manager.get_item_dict(id)
        if not info_dict:
            return
        video_abs = info_dict.get("video_abs")

        # 释放视频播放器资源
        self.video_viewer.release()

        self._capture_window = cap.CaptureVideo(video_abs)
        self._capture_window.finish_sig.connect(self._refresh_video)
        self._capture_window.show()

    # ========================================================================
    # 下拉框和列表处理
    # ========================================================================

    def _on_group_changed(self):
        """组下拉框改变"""
        self._current_group = self.cb_group.currentText()
        self._refresh_list()
        self._refresh_info()
        self._refresh_md()

    def _on_library_clicked(self, item):
        """库菜单点击 - 内部处理"""
        lib_name = item.data(QtCore.Qt.UserRole)
        if not lib_name:
            self.pa.go_set()
            return
        if lib_name != self.pa.current_lib_name:
            self.pa.switch_library(lib_name)

    def _on_item_clicked(self, item):
        """Recipe 列表项点击"""
        item_id = item.data(QtCore.Qt.UserRole)
        if item_id != self._current_id:
            self._current_id = item_id
            self._refresh_info()
            self._refresh_md()
            self._refresh_video()

    # ========================================================================
    # 辅助方法
    # ========================================================================

    def _get_selected_ids(self):
        """获取选中的 Recipe IDs

        Returns:
            list: Recipe ID 列表
        """
        sel_items = self.list_thumb.selectedItems()
        return [item.data(QtCore.Qt.UserRole) for item in sel_items]

    # ========================================================================
    # 刷新方法
    # ========================================================================

    def refresh(self):
        """UI 自主刷新所有区域"""
        self.init_left_menu()
        self._update_title()
        self._refresh_groups()
        self._refresh_list()
        self._refresh_info()
        self._refresh_md()
        self._refresh_video()

    def refresh_after_lib_change(self):
        """库列表变更后刷新界面（由 Ui_Setting 通过 RB_Win 回调）"""
        self._current_group = "All"
        self._current_id = None
        self.refresh()

    def _refresh_groups(self):
        """刷新组下拉框"""
        self.cb_group.clear()
        groups = self.pa.manager.groups
        self.cb_group.addItems(groups)
        if self._current_group and self._current_group in groups:
            self.cb_group.setCurrentText(self._current_group)
        else:
            self.cb_group.setCurrentIndex(0)
            self._current_group = groups[0] if groups else "All"

    def _refresh_list(self):
        """刷新 Recipe 预览图列表"""
        self.list_thumb.clear()
        self.items_widget = {}

        manager = self.pa.manager
        if not manager:
            return

        items_dict = manager.get_items_dict(self._current_group)
        if not items_dict:
            return

        filtered_items = self._filter_items(items_dict)
        if not filtered_items:
            return

        self._update_current_id(filtered_items)
        self._create_item_widgets(filtered_items)

    def _refresh_info(self):
        """刷新 Recipe 信息显示"""
        self.list_info.clear()
        manager = self.pa.manager
        if not self._current_id or not manager:
            return

        info_dict = manager.get_item_dict(self._current_id)
        if not info_dict:
            return

        for key in ["title", "name", "pattern","type", "author","comment"]:
            self._add_info_field(key, info_dict)

    def _refresh_md(self):
        """刷新 Markdown 编辑器内容"""
        md_editor = self.pa.md_editor
        if not md_editor or not md_editor.isVisible():
            return
        manager = self.pa.manager
        if not self._current_id or not manager:
            return
        md_file = manager.get_item_md(self._current_id)
        if md_file:
            md_editor.update_md_path(md_file)

    def _refresh_video(self):
        """刷新 Recipe 预览视频"""
        manager = self.pa.manager
        if not self._current_id or not manager:
            return
        info_dict = manager.get_item_dict(self._current_id)
        if not info_dict:
            return
        video_path = info_dict.get("video_abs", "")
        self.video_viewer.update_video(video_path)

    def _filter_items(self, items_dict):
        """
        过滤 Recipe 列表（收藏和忽略）

        Args:
            items_dict: 原始 Recipe 字典

        Returns:
            dict: 过滤后的 Recipe 字典
        """
        filtered = {}
        for item_id, item_widget_dict in items_dict.items():
            if not item_widget_dict.get("fav") and self._is_solo_fav:
                continue
            if (
                item_widget_dict.get("ignore")
                and not self._is_show_ignore
                and self._current_group != "Ignore"
            ):
                continue
            filtered[item_id] = item_widget_dict
        return filtered

    def _update_current_id(self, items_dict):
        """
        更新当前选中的 Recipe ID

        Args:
            items_dict: Recipe 字典
        """
        if self._current_id not in items_dict and items_dict:
            self._current_id = list(items_dict.keys())[0]

    def _create_item_widgets(self, items_dict):
        """
        创建 Recipe 组件并添加到列表

        Args:
            items_dict: Recipe ID 字典
        """
        for item_id in items_dict.keys():
            item_widget = Item_Widget(self.pa, item_id)
            self.items_widget[item_id] = item_widget

            list_item = QListWidgetItem()
            list_item.setData(QtCore.Qt.UserRole, item_id)
            list_item.setSizeHint(item_widget.size())

            self.list_thumb.addItem(list_item)
            self.list_thumb.setItemWidget(list_item, item_widget)

    # ========================================================================
    # 库菜单管理
    # ========================================================================

    def init_left_menu(self):
        """初始化左侧库菜单：为每个库创建列表项"""
        self.lw_menu1.clear()

        if not MYSET.libs:
            self._handle_empty_library()
            return

        self._create_library_menu_items()
        self._update_selected_library()

    def _handle_empty_library(self):
        """处理空库情况：显示设置图标"""
        icon_path = f"{ALLSET.sbox_path}/file/icon02/10042.svg"
        icon = QtGui.QIcon(icon_path)
        item = QListWidgetItem(icon, "Add Lib")
        item.setSizeHint(QtCore.QSize(70, 60))
        item.setData(QtCore.Qt.UserRole, "")
        self.lw_menu1.addItem(item)

    def _create_library_menu_items(self):
        """创建库菜单列表项"""
        for lib_name in MYSET.lib_sort:
            lib_dict = MYSET.libs.get(lib_name)
            if not lib_dict:
                continue

            item = self._create_lib_menu_item(lib_name, lib_dict)
            self.lw_menu1.addItem(item)

    def _create_lib_menu_item(self, lib_name, lib_dict):
        """
        创建单个库菜单项

        Args:
            lib_name: 库名称
            lib_dict: 库配置字典

        Returns:
            QListWidgetItem: 库菜单项
        """
        icon_num = lib_dict.get("icon", "10001")
        icon_path = f"{ALLSET.sbox_path}/file/icon02/{icon_num}.svg"
        icon = QtGui.QIcon(icon_path)

        item = QListWidgetItem(icon, lib_name)
        item.setSizeHint(QtCore.QSize(70, 60))
        item.setData(QtCore.Qt.UserRole, lib_name)
        item.setToolTip(lib_name)

        return item

    def _update_selected_library(self):
        """更新当前选中的库"""
        current_lib = self.pa.current_lib_name
        if current_lib in MYSET.libs and current_lib in MYSET.lib_sort:
            index = MYSET.lib_sort.index(current_lib)
            self.lw_menu1.setCurrentRow(index)
        elif MYSET.lib_sort:
            self.lw_menu1.setCurrentRow(0)

    def _update_title(self):
        """更新窗口标题显示当前库名称"""
        current_lib = self.pa.current_lib_name
        if current_lib and current_lib in MYSET.libs:
            self.l_title.setText(current_lib)
        else:
            self.l_title.setText("Recipe Box")

    # ========================================================================
    # 信息面板
    # ========================================================================

    def _is_editable_field(self, key):
        """
        判断字段是否可编辑

        Args:
            key: 字段名

        Returns:
            bool: 可编辑返回 True
        """
        return key in {"title", "pattern", "comment"}

    def _add_info_field(self, key, info_dict):
        """
        添加信息字段到列表

        Args:
            key: 字段名
            info_dict: Recipe 信息字典
        """
        value = info_dict.get(key, "")

        if key =="type":
            value = f"{value} _ {info_dict.get('houdiniVersion', '')}"
        if not value:
            value = "no_value"
        is_edit = self._is_editable_field(key)
        line_edit = self.list_info.add_item(key, value, readOnly=not is_edit)

        if is_edit:
            line_edit.edit.setProperty("field_key", key)
            line_edit.edit.editingFinished.connect(self._on_info_edit_finished)

    def _on_info_edit_finished(self):
        """信息字段编辑完成"""
        if not self._current_id or not self.pa.manager:
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

        self.pa.manager.update_item(self._current_id, key, new_value)

        # 刷新对应的 Item_Widget
        widget = self.items_widget.get(self._current_id)
        if widget:
            widget.refresh_ui()

    # ========================================================================
    # 右键菜单
    # ========================================================================

    def _on_right_click(self, position):
        """
        显示右键菜单

        Args:
            position: 鼠标位置
        """
        menu = Snail_Menu()
        selected_items = self.list_thumb.selectedItems()

        if not selected_items:
            return

        ids = self._get_selected_ids()
        self._create_context_menu(menu, ids)
        menu.exec_(self.list_thumb.viewport().mapToGlobal(position))

    def _create_context_menu(self, menu, ids):
        """
        创建右键菜单项

        Args:
            menu: 菜单对象
            ids: 选中的 Recipe ID 列表
        """
        submenu = self._create_group_submenu()
        menu.addAction("Apply", lambda: self._apply_context(ids))
        menu.addAction("Edit", lambda: self._edit_context(ids))
        menu.addAction("View MD", lambda: self.pa.view_edit_md(ids))
        menu.addAction("Capture Thumb", lambda: self._capture_thumb(ids))
        menu.addAction("Capture Video", lambda: self._capture_video(ids))
        menu.addMenu(submenu)
        menu.addAction("Export / Share", lambda: self._export_items(ids))
        menu.addAction("Toggle Favorite", lambda: self._toggle_fav_context(ids))
        menu.addAction("Toggle Ignore", lambda: self._toggle_ignore_context(ids))
        menu.addAction("Delete", lambda: self._delete_items(ids))
        menu.addAction("Open Folder", lambda: self._open_folder_context(ids))

    def _create_group_submenu(self):
        """
        获取右键菜单的分组子菜单

        Returns:
            Snail_Menu: 分组子菜单
        """
        submenu = Snail_Menu("Change group")
        submenu.addAction("Add group", self._submenu_add_group)
        submenu.addAction("Remove group", self._submenu_remove_group)

        manager = self.pa.manager
        if not manager:
            return submenu

        items_group = manager.get_items_group()
        if items_group:
            for group in items_group:
                submenu.addAction(group, lambda g=group: self._submenu_modify_group(g))

        return submenu

    def _submenu_add_group(self):
        """添加组菜单项点击"""
        ids = self._get_selected_ids()
        if not ids:
            hou.ui.displayMessage("Please select one item")
            return
        result = hou.ui.readInput("新组名:", buttons=("OK", "Cancel"))
        if not result:
            return
        group = result[1]
        self.pa.manager.items_modify_group(ids, group)
        self.refresh()

    def _submenu_remove_group(self):
        """移除组菜单项点击"""
        ids = self._get_selected_ids()
        if not ids:
            hou.ui.displayMessage("Please select one item")
            return
        self.pa.manager.items_modify_group(ids, "")
        self.refresh()

    def _submenu_modify_group(self, group):
        """修改组菜单项点击"""
        ids = self._get_selected_ids()
        if not ids:
            hou.ui.displayMessage("Please select one item")
            return
        self.pa.manager.items_modify_group(ids, group)
        self.refresh()

    # ========================================================================
    # 右键菜单操作处理
    # ========================================================================

    def _apply_context(self, ids):
        """右键菜单应用"""
        if ids:
            self.pa.manager.apply_item(ids[-1])

    def _edit_context(self, ids):
        """右键菜单编辑"""
        if ids:
            self.pa.manager.edit_item(ids[-1])

    def _toggle_fav_context(self, ids):
        """右键菜单切换收藏"""
        if not ids:
            return
        self.pa.manager.items_toggle_fav(ids)
        for id in ids:
            self.on_item_updated(id)

    def _toggle_ignore_context(self, ids):
        """右键菜单切换忽略"""
        if not ids:
            return
        self.pa.manager.items_toggle_ignore(ids)
        self.refresh()

    def _delete_items(self, ids):
        """
        删除选中的 Recipe

        Args:
            ids: 选中的 Recipe ID 列表
        """
        if not ids:
            hou.ui.displayMessage("Please select one item")
            return
        count = len(ids)
        msg = f"Are you sure you want to delete {count} Recipe(s)?"
        confirm = hou.ui.displayMessage(msg, buttons=("Cancel", "OK"), close_choice=0)
        if confirm != 1:
            return
        self.pa.manager.del_items(ids)
        self.refresh()

    def _open_folder_context(self, ids):
        """右键菜单打开文件夹"""
        if ids:
            self.pa.manager.open_item_folder(ids[-1])

    # ========================================================================
    # Recipe 更新回调
    # ========================================================================

    def on_item_updated(self, id):
        """
        Recipe 更新回调：刷新对应的 Widget 显示

        Args:
            id: Recipe ID
        """
        item_widget = self.items_widget.get(id)
        if item_widget:
            item_widget.refresh_ui()


class Ui_Setting(QDialog):
    """
    设置对话框类

    提供 RecipeBox 的设置界面，包括库管理、图标选择等功能。
    """

    # 类级常量
    PACKAGE_SEPARATOR = " : "
    DEFAULT_PACKAGE = "SnailBox"

    # 默认 Recipe 数据模板
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
        """初始化设置对话框"""
        super().__init__(parent)
        self.pa = parent
        self._setup_window()
        self.init_ui()
        self.init_data()
        self.connect_signals()

    def _setup_window(self):
        """设置窗口属性"""
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        self.setWindowTitle("SnailBox Recipe Box Setting")
        # 移除帮助按钮，保留关闭按钮
        self.setWindowFlags(
            self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint
            | QtCore.Qt.WindowCloseButtonHint
        )

    def init_ui(self):
        """初始化设置界面"""
        tab = self._create_tab_widget()
        layout_main = QVBoxLayout(self)
        layout_main.addWidget(tab)

        # 创建 Library 标签页
        self.tab_library = self._create_library_tab()
        tab.addTab(self.tab_library, "Library")

        self.setLayout(layout_main)

    def _create_tab_widget(self):
        """创建标签页控件"""
        tab = QTabWidget(self)
        tab.setStyleSheet(
            "QTabBar::tab:selected {color: rgb(255,163,32);}"
            "QTabBar {font-family: Microsoft YaHei UI; font-size: 14px;}"
        )
        return tab

    def _create_library_tab(self):
        """创建库管理标签页"""
        layout_tab1 = QVBoxLayout()

        # 库列表表格
        self.tw_libList = self._create_library_table()
        layout_tab1.addWidget(self.tw_libList)

        # 选项区域
        layout_options = self._create_options_layout()
        layout_tab1.addLayout(layout_options)

        # 按钮区域
        layout_buttons = self._create_buttons_layout()
        layout_tab1.addLayout(layout_buttons)

        # 提示信息
        self.t_tips = Snail_TextBrowser(self)
        self.t_tips.setFixedHeight(80)
        layout_tab1.addWidget(self.t_tips)

        layout_tab1.setStretch(0, 1)

        tab_widget = QWidget()
        tab_widget.setLayout(layout_tab1)
        return tab_widget

    def _create_library_table(self):
        """创建库列表表格"""
        table = Snail_Table(self)
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Name", "Package"])
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.itemClicked.connect(self.on_lib_selected)
        return table

    def _create_options_layout(self):
        """创建选项布局"""
        layout = QHBoxLayout()

        # Package 下拉框
        self.cb_package = Snail_ComboBox(tip="Package : hda")
        self.cb_package.setFixedWidth(200)

        # Index 下拉框
        self.cb_index = Snail_ComboBox(tip="Index")
        self.cb_index.setFixedWidth(50)

        # Icon 下拉框
        self.cb_icon = Snail_ComboBox(tip="Icon")
        self.cb_icon.setFixedWidth(100)

        # Name 输入框
        self.le_name = Snail_LineEdit(tip="Library name")

        layout.addWidget(self.cb_package)
        layout.addWidget(self.cb_index)
        layout.addWidget(self.cb_icon)
        layout.addWidget(self.le_name)
        return layout

    def _create_buttons_layout(self):
        """创建按钮布局"""
        layout = QHBoxLayout()

        self.btn_del = Snail_Btn("Delete")
        self.btn_mod = Snail_Btn("Modify")
        self.btn_add = Snail_Btn("Add")

        layout.addWidget(self.btn_del)
        layout.addWidget(self.btn_mod)
        layout.addWidget(self.btn_add)
        return layout

    def init_data(self):
        """初始化设置数据"""
        self.refresh_lib_list()
        self.refresh_package_cb()
        self.refresh_index_cb()
        self.refresh_icon_cb()
        self.refresh_tips()

    def connect_signals(self):
        """连接信号"""
        self.btn_add.clicked.connect(self.add_lib)
        self.btn_del.clicked.connect(self.del_lib)
        self.btn_mod.clicked.connect(self.mod_lib)
        self.cb_package.currentTextChanged.connect(self.refresh_tips)

    def refresh_lib_list(self):
        """刷新库列表表格"""
        self.tw_libList.setRowCount(0)
        for lib_name in MYSET.lib_sort:
            lib_dict = MYSET.libs.get(lib_name)
            if not lib_dict:
                continue

            row = self.tw_libList.rowCount()
            self.tw_libList.insertRow(row)

            # 设置库名称
            self.tw_libList.setItem(row, 0, QTableWidgetItem(lib_dict.get("name", "")))

            # 设置 Package:HDA 显示
            package_display = self._format_package_display(lib_dict)
            self.tw_libList.setItem(row, 1, QTableWidgetItem(package_display))

        self.tw_libList.resizeColumnsToContents()

    def _format_package_display(self, lib_dict):
        """
        格式化 Package:HDA 显示字符串

        Args:
            lib_dict: 库配置字典

        Returns:
            str: 格式化后的显示字符串
        """
        package = lib_dict.get("package", "")
        hda = lib_dict.get("hda", "")
        return f"{package}{self.PACKAGE_SEPARATOR}{hda}" if package and hda else package

    def refresh_package_cb(self):
        """刷新 Package 下拉框"""
        self.cb_package.clear()

        # 从 Houdini Recipe Storage 获取所有可用的 packages
        packages = self._get_available_packages()
        packages = sorted(packages)
        packages.insert(0, "Add new lib")

        for pkg in packages:
            self.cb_package.addItem(pkg)

    def _get_available_packages(self):
        """
        从 Houdini Recipe Storage 获取可用的包列表

        Returns:
            set: 包名集合
        """
        store = storage.recipeStorage()
        all_refs = store.refs()
        packages = set()

        for ref in all_refs:
            location = ref.location()
            package = Path(location).parent.parent.name
            custom_lib_name = ALLSET.custom_lib.split("/")[-1]
            if package == "SnailBox_dev":
                package = self.DEFAULT_PACKAGE
            if package == custom_lib_name:
                package = self.DEFAULT_PACKAGE
            name = Path(location).stem
            packages.add(f"{package}{self.PACKAGE_SEPARATOR}{name}")

        return packages

    def refresh_index_cb(self):
        """刷新 Index 下拉框"""
        self.cb_index.clear()
        for i in range(len(MYSET.lib_sort) + 1):
            self.cb_index.addItem(str(i))

    def refresh_icon_cb(self):
        """刷新 Icon 下拉框"""
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
        """刷新提示信息"""
        tips = [
            "* Add: Add a new library to the list",
            "* Delete: Select a library and click delete",
            "* Modify: Select a library and modify its properties",
            "* Package: 'package : hda_name'",
            "* Name: The name of the library",
        ]
        self.t_tips.update_tips(tips)

    def on_lib_selected(self):
        """当选择库列表中的某一行时"""
        row = self.tw_libList.currentRow()
        if not self._is_valid_row(row):
            return

        lib_name = MYSET.lib_sort[row]
        lib_dict = MYSET.libs.get(lib_name)
        if not lib_dict:
            return

        self._fill_library_options(lib_name, lib_dict, row)

    def _is_valid_row(self, row):
        """
        检查行号是否有效

        Args:
            row: 行号

        Returns:
            bool: 有效返回 True，否则返回 False
        """
        return row >= 0 and row < len(MYSET.lib_sort)

    def _fill_library_options(self, lib_name, lib_dict, row):
        """
        填充库选项到界面控件

        Args:
            lib_name: 库名称
            lib_dict: 库配置字典
            row: 行号
        """
        # 填充名称
        self.le_name.setText(lib_dict.get("name", ""))

        # 填充 Package:HDA
        package_hda = self._format_package_display(lib_dict)
        self.cb_package.setCurrentText(package_hda)

        # 填充索引
        self.cb_index.setCurrentText(str(row))

        # 填充图标
        self._set_current_icon(lib_dict.get("icon", ""))

    def _set_current_icon(self, icon_num):
        """
        设置当前选中的图标

        Args:
            icon_num: 图标编号
        """
        if icon_num:
            index = self.cb_icon.findData(icon_num)
            if index >= 0:
                self.cb_icon.setCurrentIndex(index)

    def get_selected_lib_name(self):
        """获取当前选中的库名称，如果没有选中返回 None"""
        row = self.tw_libList.currentRow()
        if not self._is_valid_row(row):
            hou.ui.displayMessage("Please select a library from the list")
            return None
        return MYSET.lib_sort[row]

    def add_lib(self):
        """添加新库"""
        # 获取输入值
        package_hda = self.cb_package.currentText()
        index = int(self.cb_index.currentText())
        icon = self.cb_icon.currentText()
        name = self.le_name.text()

        # 验证名称
        if not name:
            hou.ui.displayMessage("Please enter a library name")
            return

        # 处理添加新库
        if package_hda == "Add new lib":
            if not self._create_new_library(name):
                return
            package_hda = f"{self.DEFAULT_PACKAGE}{self.PACKAGE_SEPARATOR}{name}"

        # 解析 package:hda
        parsed = self._parse_package_hda(package_hda)
        if not parsed:
            return

        package, hda = parsed

        # 构建库配置
        lib_dict = {
            "name": name,
            "icon": icon,
            "package": package,
            "hda": hda,
        }

        # 调用 Setting.add_lib()
        result = MYSET.add_lib(index, lib_dict)

        if result:
            self._refresh_after_change()

    def _create_new_library(self, name):
        """
        创建新库 HDA

        Args:
            name: 库名称

        Returns:
            bool: 成功返回 True，失败返回 False
        """
        res = self.add_hda(name)
        return res is not None

    def _parse_package_hda(self, package_hda):
        """
        解析 Package:HDA 格式字符串

        Args:
            package_hda: Package:HDA 格式字符串

        Returns:
            tuple: (package, hda) 或 None（解析失败时）
        """
        if self.PACKAGE_SEPARATOR in package_hda:
            return package_hda.split(self.PACKAGE_SEPARATOR, 1)

        hou.ui.displayMessage(f"Invalid package format: {package_hda}")
        return None

    def _refresh_after_change(self):
        """库列表变更后刷新界面"""
        self.refresh_lib_list()
        self.refresh_index_cb()
        self.refresh_package_cb()
        # 刷新主窗口的 manager
        if hasattr(self.pa, "refresh_manager"):
            self.pa.refresh_manager()

    def del_lib(self):
        """删除库"""
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
        """修改库"""
        lib_name = self.get_selected_lib_name()
        if not lib_name:
            return

        # 获取输入值
        package_hda = self.cb_package.currentText()
        new_index = int(self.cb_index.currentText())
        icon = self.cb_icon.currentText()
        name = self.le_name.text()

        # 验证名称
        if not name:
            hou.ui.displayMessage("Please enter a library name")
            return

        # 解析 package:hda
        parsed = self._parse_package_hda(package_hda)
        if not parsed:
            return

        package, hda = parsed

        # 获取库配置
        lib_dict = MYSET.libs.get(lib_name)
        if not lib_dict:
            hou.ui.displayMessage(f"Library '{lib_name}' not found")
            return

        # 验证不可修改的字段
        if not self._validate_modifiable_fields(lib_name, lib_dict, name, package, hda):
            return

        # 更新可修改的属性
        lib_dict["icon"] = icon

        # 调用 Setting.update_lib()
        result = MYSET.update_lib(lib_name, new_index, lib_dict)

        if result:
            self.refresh_lib_list()
            if hasattr(self.pa, "refresh_manager"):
                self.pa.refresh_manager()

    def _validate_modifiable_fields(self, lib_name, lib_dict, name, package, hda):
        """
        验证可修改字段

        Args:
            lib_name: 原库名称
            lib_dict: 库配置字典
            name: 新名称
            package: 新 package
            hda: 新 hda

        Returns:
            bool: 验证通过返回 True，否则返回 False
        """
        # 名称不能修改
        if lib_name != name:
            hou.ui.displayMessage("Library name cannot be modified")
            self.on_lib_selected()
            return False

        # package 和 hda 也不能修改
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
        """
        添加新 HDA

        Args:
            name: HDA 名称

        Returns:
            bool: 成功返回 True，失败返回 None
        """
        if not name:
            return None

        # 检查是否已存在
        if self._hda_exists(name):
            hou.ui.displayMessage(f"HDA '{name}' already exists")
            return None

        # 保存新 HDA
        try:
            store = storage.recipeStorage()
            hda_path = os.path.join(ALLSET.custom_lib, "otls", f"{name}.hda")
            if not hda_path:
                raise ValueError(f"Add {name}.hda failed.")
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
        """
        检查 HDA 是否已存在

        Args:
            name: HDA 名称

        Returns:
            bool: 存在返回 True，否则返回 False
        """
        libs = MYSET.libs if MYSET.libs else {}
        for lib in libs.values():
            if lib.get("hda") == name and lib.get("package").startswith(self.DEFAULT_PACKAGE):
                return True
        return False


class Item_Widget(QToolButton):
    """
    Recipe 项目显示组件

    显示 Recipe 的预览图和名称，支持悬停交互。

    设计原则：
        - 只存储 item_id，通过 property 动态获取数据
        - 所有按钮信号内置处理
    """

    # 预览图尺寸常量
    THUMB_WIDTH = 128
    THUMB_HEIGHT = 128

    def __init__(self, parent, item_id):
        """初始化 Recipe 项目组件

        Args:
            parent: 父窗口 (RB_Win)
            item_id: Recipe ID
        """
        super().__init__(parent)
        self._main_window = parent
        self._item_id = item_id
        self.inter = False  # 鼠标悬停状态

        self._setup_widget()
        self.refresh_ui()

    # ========================================================================
    # Property - 动态获取数据
    # ========================================================================

    @property
    def item(self):
        """动态获取 Recipe_Item 对象"""
        return self._main_window.manager.get_item(self._item_id)

    @property
    def id(self):
        """获取 Recipe ID"""
        return self._item_id

    @property
    def title(self):
        """动态获取标题"""
        return self.item.title if self.item else ""

    @property
    def name(self):
        """动态获取名称"""
        return self.item.name if self.item else ""

    @property
    def type(self):
        """动态获取类型"""
        return self.item.type if self.item else ""

    @property
    def fav(self):
        """动态获取收藏状态"""
        return self.item.fav if self.item else False

    @property
    def thumb_abs(self):
        """动态获取预览图路径"""
        return self.item.thumb_abs if self.item else ""

    # ========================================================================
    # UI 设置和刷新
    # ========================================================================

    def _setup_widget(self):
        """设置控件属性"""
        self.setObjectName("item")
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setMouseTracking(True)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._set_stylesheet()
        self._set_sizes()

    def _set_stylesheet(self):
        """设置样式表"""
        self.setStyleSheet(
            "QToolButton#item{ background-color:rgb(29,29,29);padding: 0px; padding-top: -2px; border:none;}"
            "QToolButton#item:hover{color: rgb(255,163,32); background-color:rgb(60,60,60);}"
        )

    def _set_sizes(self):
        """设置控件尺寸"""
        widget_size = QtCore.QSize(self.THUMB_WIDTH, self.THUMB_HEIGHT + 25)
        self.setFixedSize(widget_size)
        icon_size = QtCore.QSize(self.THUMB_WIDTH, self.THUMB_HEIGHT)
        self.setIconSize(icon_size)
        self.icon_size = icon_size

    def refresh_ui(self):
        """刷新 UI 显示（通过 property 动态获取数据）"""
        self._set_display_text()
        self._update_thumb()
        self._setup_buttons()
        self._update_type_icon()
        self._update_fav_display()

    def _set_display_text(self):
        """设置显示文本（优先使用 title，否则使用 name）"""
        display_text = self.title or self.name
        self.setText(display_text)

    def _update_thumb(self):
        """更新预览图"""
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
        """
        获取预览图路径（如果文件不存在则返回默认路径）

        Returns:
            str: 预览图绝对路径
        """
        thumb_abs = self.thumb_abs
        if not thumb_abs or not Path(thumb_abs).is_file():
            thumb_abs = ALLSET.sbox_path + "/file/tex/thumb_def.jpg"
        return thumb_abs

    # ========================================================================
    # 按钮创建和信号内置处理
    # ========================================================================

    def _setup_buttons(self):
        """初始化所有按钮"""
        self._create_apply_button()
        self._create_cap_button()
        self._create_fav_button()
        self._create_type_button()

    def _create_apply_button(self):
        """创建应用按钮"""
        if not hasattr(self, "tb_apply"):
            self.tb_apply = Snail_IconBtn("snail_add", "Apply recipe", pa=self)
            self.tb_apply.move(self.THUMB_WIDTH - 26, self.THUMB_HEIGHT)
            self.tb_apply.clicked.connect(self._on_apply_clicked)
        self.tb_apply.setVisible(self.inter)

    def _create_cap_button(self):
        """创建截图按钮"""
        if not hasattr(self, "tb_cap"):
            self.tb_cap = Snail_IconBtn("snail_matThumb2", "Capture thumb", pa=self)
            self.tb_cap.move(self.THUMB_WIDTH - 52, self.THUMB_HEIGHT)
            self.tb_cap.clicked.connect(self._on_cap_clicked)
        self.tb_cap.setVisible(self.inter)

    def _create_fav_button(self):
        """创建收藏按钮"""
        if not hasattr(self, "tb_fav"):
            self.tb_fav = Snail_IconBtn_toggle("snail_fav1", "snail_fav2", bg=2, pa=self)
            self.tb_fav.move(self.THUMB_WIDTH - 52, 2)
            self.tb_fav.clicked.connect(self._on_fav_clicked)
        self._update_fav_display()

    def _create_type_button(self):
        """创建类型图标按钮"""
        if not hasattr(self, "tb_type"):
            icon = self._get_type_icon()
            self.tb_type = Snail_IconBtn(icon, "recipe_type", bg=2, pa=self)
            self.tb_type.move(self.THUMB_WIDTH - 26, 2)

    def _get_type_icon(self):
        """
        根据类型获取对应图标名称

        Returns:
            str: 图标名称
        """
        icon_dict = {
            "nodePreset": "DATATYPES_preset_parms",
            "tool": "DATATYPES_node_path",
            "decoration": "DATATYPES_preset_nodes_central",
        }
        return icon_dict.get(self.type, "BUTTONS_recipe")

    def _update_type_icon(self):
        """更新类型图标"""
        pass

    def _update_fav_display(self):
        """更新收藏按钮显示"""
        if hasattr(self, "tb_fav"):
            self.tb_fav.setChecked(self.fav)
            self.tb_fav.setVisible(self.fav or self.inter)

    # ------------------------------------------------------------------------
    # 内部信号处理方法
    # ------------------------------------------------------------------------

    def _on_apply_clicked(self):
        """应用按钮点击 - 内部信号处理"""
        self._main_window.manager.apply_item(self._item_id)

    def _on_cap_clicked(self):
        """截图按钮点击 - 内部信号处理"""
        cap_img = cap.CaptureImage(self.thumb_abs)
        cap_img.finish_sig.connect(self._update_thumb)
        cap_img.show()

    def _on_fav_clicked(self):
        """收藏按钮点击 - 内部信号处理"""
        self.item.toggle_fav()
        self._update_fav_display()

    # ------------------------------------------------------------------------
    # 鼠标事件处理
    # ------------------------------------------------------------------------

    def _toggle_button_visibility(self):
        """切换按钮显示状态（鼠标悬停时）"""
        if hasattr(self, "tb_apply"):
            self.tb_apply.setVisible(self.inter)
        if hasattr(self, "tb_cap"):
            self.tb_cap.setVisible(self.inter)
        if hasattr(self, "tb_fav"):
            self.tb_fav.setVisible(self.inter or self.fav)

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        """鼠标双击事件"""
        event.ignore()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """鼠标按下事件"""
        super().mousePressEvent(event)
        event.ignore()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """鼠标释放事件"""
        super().mouseReleaseEvent(event)
        event.ignore()

    def enterEvent(self, event):
        """鼠标进入事件"""
        self.inter = True
        self._toggle_button_visibility()

    def leaveEvent(self, event):
        """鼠标离开事件"""
        self.inter = False
        self._toggle_button_visibility()

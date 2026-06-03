"""
Flipbook 前端 UI 组件模块 (重构版)

本模块包含前后端分离后的前端 UI 组件类。

类结构:
    Ui_Main - 主界面布局 (设置区 + 预设工具栏 + 文字列表 + 底部按钮)
    ItemTextWidget - 文字项 UI 组件
"""

import os
import hou
from PySide6 import QtCore
from PySide6.QtWidgets import *
from utils import *


# ============================================================================
# Ui_Main - 主界面布局类
# ============================================================================


class Ui_Main(QWidget):
    """
    Flipbook 主界面布局类

    界面结构 (从上到下):
        1. 设置面板区域
           - 文件路径行 (路径输入 + 格式选择 + 浏览按钮)
           - 分辨率行 (宽度 + 高度 + 视图/相机按钮)
           - 帧范围行 (起始帧 + 结束帧 + 帧率 + 刷新按钮)
           - 预设工具栏 (预设下拉 + 添加/删除 + 捕获按钮组)
        2. 文字列表区域 (可滚动的 ItemTextWidget 列表)
        3. 底部按钮区域 (帮助 + 显示文本 + 捕获序列)

    职责:
        - 创建和管理所有 UI 控件和布局
        - 所有信号内部连接，取代 Fb_win 的透传方法
        - 从 Fb_Manager 同步数据到 UI 显示

    Args:
        parent: 父窗口 (Fb_win 实例)
    """

    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent      # Fb_win
        self._manager = parent.manager    # Fb_Manager
        self._setup_ui()

    def _setup_ui(self):
        """创建主界面 UI

        按顺序创建三个主要区域:
        1. 设置面板 (_create_settings_area)
        2. 文字列表 (_create_items_area)
        3. 底部按钮 (_create_buttons_area)
        """
        self._layout_main = QVBoxLayout(self)
        self._layout_main.setSpacing(0)
        self._layout_main.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout_main)

        self._create_settings_area()
        self._create_items_area()
        self._create_buttons_area()

        self._connect_internal_signals()

    # ========================================================================
    # 设置面板区域 (包含4行控件)
    # ========================================================================

    def _create_settings_area(self):
        """创建设置面板区域

        包含4行控件:
        1. 文件路径行
        2. 分辨率行
        3. 帧范围行
        4. 预设工具栏
        """
        settings_layout = QVBoxLayout()
        settings_layout.setContentsMargins(4, 4, 4, 4)
        settings_layout.setSpacing(4)

        settings_layout.addLayout(self._create_path_row())
        settings_layout.addLayout(self._create_resolution_row())
        settings_layout.addLayout(self._create_frame_range_row())
        settings_layout.addLayout(self._create_preset_toolbar_row())

        self._layout_main.addLayout(settings_layout)

    def _create_path_row(self):
        """创建文件路径行

        控件:
        - 标签: "File path"
        - 输入框: 路径输入
        - 下拉框: 输出格式选择
        - 按钮: 选择路径
        - 按钮: 打开文件夹
        """
        self._label_path = Snail_LabelA("File path")
        self._label_path.set_radius("left")
        self._line_path = Snail_LineEdit()
        self._line_path.set_radius("none")
        self._combo_format = Snail_ComboBox(self._manager.formats)
        self._combo_format.set_radius("right")
        self._btn_select_path = Snail_IconBtn("BUTTONS_chooser_folder", "Select save path")
        self._btn_open_folder = Snail_IconBtn("BUTTONS_folder", "Open save folder")

        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(self._label_path)
        layout.addWidget(self._line_path)
        layout.addWidget(self._combo_format)
        layout.addWidget(self._btn_select_path)
        return layout

    def _create_resolution_row(self):
        """创建分辨率行

        控件:
        - 标签: "Image res"
        - 输入框: 宽度 (可编辑)
        - 输入框: 高度 (自动计算，禁用)
        - 按钮: 从视图获取分辨率
        - 按钮: 从相机获取分辨率
        """
        self._label_res = Snail_LabelA("Image res")
        self._label_res.set_radius("left")
        self._line_res_x = Snail_IntLine()
        self._line_res_x.set_radius("none")
        self._line_res_y = Snail_IntLine()
        self._line_res_y.set_radius("right")
        self._line_res_y.setDisabled(True)
        self._btn_res_view = Snail_IconBtn("snail_view", "Set resolution with viewer")
        self._btn_res_cam = Snail_IconBtn("TOOLS_view_mode_camera", "Set resolution with camera")

        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(self._label_res)
        layout.addWidget(self._line_res_x)
        layout.addWidget(self._line_res_y)
        layout.addWidget(self._btn_res_view)
        layout.addWidget(self._btn_res_cam)
        return layout

    def _create_frame_range_row(self):
        """创建帧范围行

        控件:
        - 标签: "F range"
        - 输入框: 起始帧
        - 输入框: 结束帧
        - 标签: "F rate"
        - 输入框: 帧率 (自动获取，禁用)
        - 按钮: 刷新动画设置
        """
        self._label_range = Snail_LabelA("F range")
        self._label_range.set_radius("left")
        self._line_start = Snail_IntLine()
        self._line_start.set_radius("none")
        self._line_end = Snail_IntLine()
        self._line_end.set_radius("right")
        self._label_rate = Snail_LabelA("F rate")
        self._label_rate.set_radius("left")
        self._line_fps = Snail_IntLine()
        self._line_fps.set_radius("right")
        self._line_fps.setDisabled(True)
        self._btn_refresh = Snail_IconBtn("BUTTONS_reload", "Refresh animation setting")

        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(self._label_range)
        layout.addWidget(self._line_start)
        layout.addWidget(self._line_end)
        layout.addWidget(self._label_rate)
        layout.addWidget(self._line_fps)
        layout.addWidget(self._btn_refresh)
        return layout

    def _create_preset_toolbar_row(self):
        """创建预设工具栏行

        控件:
        - 下拉框: 预设选择
        - 按钮: 添加预设
        - 按钮: 删除预设
        - [弹性空间]
        - 按钮: 打开文件夹
        - 按钮: 捕获 MP4
        - 按钮: 捕获序列
        - 按钮: 捕获单帧
        - 按钮: 添加文字
        """
        self._combo_preset = Snail_ComboBox(self._manager.preset_names)
        self._btn_preset_add = Snail_IconBtn("snail_preset_save", "Add preset")
        self._btn_preset_del = Snail_IconBtn("snail_preset_del", "Delete preset")
        self._btn_add_text = Snail_IconBtn("BUTTONS_set_add", "Add text")
        self._btn_capture_frame = Snail_IconBtn("BUTTONS_capture", "Capture frame")
        self._btn_capture_seq = Snail_IconBtn("DESKTOP_image_sequence", "Capture sequence")
        self._btn_capture_mp4 = Snail_IconBtn("BUTTONS_render", "Capture mp4")

        layout = QHBoxLayout()
        layout.addWidget(self._combo_preset)
        layout.addWidget(self._btn_preset_add)
        layout.addWidget(self._btn_preset_del)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addWidget(self._btn_open_folder)
        layout.addWidget(self._btn_capture_mp4)
        layout.addWidget(self._btn_capture_seq)
        layout.addWidget(self._btn_capture_frame)
        layout.addWidget(self._btn_add_text)
        return layout

    # ========================================================================
    # 文字列表区域
    # ========================================================================

    def _create_items_area(self):
        """创建文字列表区域

        显示所有 ItemTextWidget 的可滚动列表。
        列表项样式:
        - 边框: 2px 深灰色
        - 圆角: 5px
        - 背景: 深灰色
        - 选中: 橙色边框
        """
        self._list_items = QListWidget(self)
        self._list_items.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self._list_items.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        scrollbar = self._list_items.verticalScrollBar()
        scrollbar.setSingleStep(10)
        self._list_items.setSpacing(4)
        self._list_items.setStyleSheet(
            "QListWidget::Item {border: 2px solid rgb(30, 30, 30);border-radius: 5px;background-color: rgb(40, 40, 40);}"
            "QListWidget::Item:hover {background-color: rgb(100,100,100);}"
            "QListWidget::Item:selected {border: 1px solid rgb(255, 163, 32);}"
        )
        self._layout_main.addWidget(self._list_items)

    # ========================================================================
    # 底部按钮区域
    # ========================================================================

    def _create_buttons_area(self):
        """创建底部按钮区域

        包含4个按钮:
        - 帮助按钮 (SnailBox 信息)
        - 显示文本按钮
        - 捕获序列按钮
        """
        layout = QHBoxLayout()

        self._btn_bz = Snail_IconBtn_bz()
        self._btn_help = Snail_IconBtn_help()
        self._btn_show_text = Snail_Btn("Show Text")
        self._btn_capture_seq_bottom = Snail_Btn("Capture Sequence")

        layout.addWidget(self._btn_bz)
        layout.addWidget(self._btn_help)
        layout.addWidget(self._btn_show_text)
        layout.addWidget(self._btn_capture_seq_bottom)

        self._layout_main.addLayout(layout)

    # ========================================================================
    # 数据同步方法
    # ========================================================================

    def refresh(self):
        """从 manager 同步数据到 UI

        将 Fb_Manager 中的所有属性值同步到对应的 UI 控件显示。
        通常在数据变更后调用。
        """
        self._line_path.setText(self._manager.path)
        self._combo_format.setCurrentIndex(self._manager.format_index)
        self._line_res_x.setText(str(self._manager.res_x))
        self._line_res_y.setText(str(self._manager.res_y))
        self._line_start.setText(str(self._manager.f_start))
        self._line_end.setText(str(self._manager.f_end))
        self._line_fps.setText(str(self._manager.fps))

    def clear_item_list(self):
        """清空文字列表

        删除列表中的所有 ItemTextWidget。
        通常在切换预设时调用。
        """
        if self._list_items:
            self._list_items.clear()

    def add_item_widget(self, widget):
        """添加一个 ItemTextWidget 到列表

        Args:
            widget: ItemTextWidget 实例
        """
        if not self._list_items:
            return
        item = QListWidgetItem("")
        height = widget.sizeHint().height()
        item.setSizeHint(QtCore.QSize(0, height))
        self._list_items.addItem(item)
        self._list_items.setItemWidget(item, widget)

    def init_presets(self, preset_names, current_index):
        """初始化预设下拉框

        Args:
            preset_names: 预设名称列表
            current_index: 当前选中的索引 (0 表示 Last Input)
        """
        self._combo_preset.blockSignals(True)
        self._combo_preset.clear()
        self._combo_preset.addItems(preset_names)
        self._combo_preset.setCurrentIndex(current_index)
        self._combo_preset.blockSignals(False)

    # ========================================================================
    # 信号连接
    # ========================================================================

    def _connect_internal_signals(self):
        """连接所有内部信号槽

        将 UI 控件的信号连接到对应的处理方法。
        """
        # 设置区输入框
        self._line_path.editingFinished.connect(self._on_path_changed)
        self._combo_format.currentIndexChanged.connect(self._on_format_changed)
        self._line_res_x.editingFinished.connect(self._on_res_x_changed)
        self._line_start.editingFinished.connect(self._on_f_start_changed)
        self._line_end.editingFinished.connect(self._on_f_end_changed)
        self._combo_preset.currentIndexChanged.connect(self._on_preset_changed)

        # 设置区按钮
        self._btn_select_path.clicked.connect(self._on_select_path_clicked)
        self._btn_open_folder.clicked.connect(self._on_open_folder_clicked)
        self._btn_res_view.clicked.connect(self._on_res_view_clicked)
        self._btn_res_cam.clicked.connect(self._on_res_cam_clicked)
        self._btn_refresh.clicked.connect(self._on_refresh_clicked)
        self._btn_preset_add.clicked.connect(self._on_preset_add_clicked)
        self._btn_preset_del.clicked.connect(self._on_preset_del_clicked)

        # 捕获按钮
        self._btn_add_text.clicked.connect(self._on_add_text_clicked)
        self._btn_capture_frame.clicked.connect(self._on_capture_frame_clicked)
        self._btn_capture_seq.clicked.connect(self._on_capture_sequence_clicked)
        self._btn_capture_mp4.clicked.connect(self._on_capture_mp4_clicked)

        # 底部按钮
        self._btn_show_text.clicked.connect(self._on_show_text_clicked)
        self._btn_capture_seq_bottom.clicked.connect(self._on_capture_sequence_clicked)

    # ========================================================================
    # 回调方法 - 设置区输入框
    # ========================================================================

    def _on_path_changed(self):
        """文件路径输入框变更"""
        self._manager.path = self._line_path.text()

    def _on_format_changed(self):
        """输出格式下拉框变更"""
        self._manager.format_index = self._combo_format.currentIndex()
        self.refresh()

    def _on_res_x_changed(self):
        """分辨率宽度输入框变更

        自动计算对应的高度，保持宽高比。
        结果为偶数 (符合视频编码要求)。
        """
        ox = self._manager.res_x
        oy = self._manager.res_y
        oratio = oy / ox
        try:
            x = int(self._line_res_x.text())
        except ValueError:
            return
        x = x + 1 if x % 2 else x
        if x:
            self._manager.res_x = x
            y = int(x * oratio)
            y = y + 1 if y % 2 else y
            if y:
                self._manager.res_y = y
        self.refresh()

    def _on_f_start_changed(self):
        """起始帧输入框变更"""
        try:
            int_start = int(self._line_start.text())
        except ValueError:
            return
        self._manager.f_start = int_start
        if int_start > self._manager.f_end:
            self._manager.f_end = int_start + 1
        self.refresh()

    def _on_f_end_changed(self):
        """结束帧输入框变更"""
        try:
            int_end = int(self._line_end.text())
        except ValueError:
            return
        self._manager.f_end = int_end
        if self._manager.f_start > int_end:
            self._manager.f_end = self._manager.f_start + 1
        self.refresh()

    def _on_preset_changed(self, index):
        """预设下拉框变更

        切换预设时重新加载文字项列表。
        """
        self._manager.change_preset(index)
        self._parent._update_text_item_list()

    # ========================================================================
    # 回调方法 - 设置区按钮
    # ========================================================================

    def _on_select_path_clicked(self):
        """选择路径按钮点击 - 打开文件夹选择对话框"""
        res = hou.ui.selectFile(
            start_directory="$HIP",
            title="Select Path",
            collapse_sequences=True,
            file_type=hou.fileType.Directory,
        )
        if res:
            self._manager.path = res
            self.refresh()

    def _on_open_folder_clicked(self):
        """打开文件夹按钮点击 - 在系统文件管理器中显示"""
        path = self._manager.get_path()
        path_dir = os.path.dirname(path)
        path_dir_abs = hou.text.expandString(path_dir)
        hou.ui.showInFileBrowser(path_dir_abs)

    def _on_res_view_clicked(self):
        """视图分辨率按钮点击 - 从当前视图获取分辨率"""
        self._manager.update_res_from_view()
        self.refresh()

    def _on_res_cam_clicked(self):
        """相机分辨率按钮点击 - 从相机获取分辨率"""
        self._manager.update_res_from_cam()
        self.refresh()

    def _on_refresh_clicked(self):
        """刷新按钮点击 - 重新获取帧范围和帧率"""
        self._manager.update_frame_range()
        self.refresh()

    def _on_preset_add_clicked(self):
        """添加预设按钮点击 - 保存当前设置为新预设"""
        preset_name = self._manager.new_user_preset()
        if preset_name:
            # 刷新整个预设列表 (同名预设会覆盖)
            preset_names = self._manager.preset_names
            # 找到新增/更新预设的索引并选中
            try:
                index = preset_names.index(preset_name)
            except ValueError:
                index = 0  # 默认 Last Input
            self.init_presets(preset_names, index)

    def _on_preset_del_clicked(self):
        """删除预设按钮点击 - 删除当前选中的预设"""
        current_name = self._combo_preset.currentText()
        self._manager.del_user_preset(current_name)
        # 删除后保持 Last Input 选中
        self.init_presets(self._manager.preset_names, 0)

    # ========================================================================
    # 回调方法 - 捕获按钮
    # ========================================================================

    def _on_add_text_clicked(self):
        """添加文字按钮点击"""
        self._parent.on_add_text_clicked()

    def _on_capture_frame_clicked(self):
        """捕获单帧按钮点击"""
        self._parent.setFocus()
        self._manager.capture(0)

    def _on_capture_sequence_clicked(self):
        """捕获序列按钮点击"""
        self._parent.setFocus()
        self._manager.capture(1)

    def _on_capture_mp4_clicked(self):
        """捕获 MP4 按钮点击"""
        self._parent.setFocus()
        self._manager.capture_mp4()

    # ========================================================================
    # 回调方法 - 底部按钮
    # ========================================================================

    def _on_show_text_clicked(self):
        """显示文本按钮点击 - 在 viewport 中显示/隐藏文字"""
        self._manager.show_text()


# ============================================================================
# ItemTextWidget - 文字项 UI 组件
# ============================================================================


class ItemTextWidget(QWidget):
    """
    文字项 UI 组件

    显示和编辑单个文字项的所有属性，包括：
    - 文本内容和类型
    - 字体大小、粗体、斜体
    - 数字填充选项
    - 对齐位置和边距
    - 文本颜色

    职责:
        - 创建和管理单个文字项的 UI 控件
        - 所有信号内部连接，属性变更自动同步到数据模型
        - 通过 _main_window 回调通知 viewport 更新显示

    Args:
        item_id: 文字项的唯一标识符
        parent: 父窗口 (Fb_win 实例)
    """

    def __init__(self, item_id, parent=None):
        super().__init__(parent)
        self.item_id = item_id
        self._main_window = parent  # Fb_win
        self._setup_ui()

    @property
    def item(self):
        """动态获取 Item_Text 对象

        通过 property 延迟获取，避免直接持有 Item_Text 引用，
        实现 Widget 与数据模型的解耦。
        """
        return self._main_window.manager.get_text_item(self.item_id)

    def _setup_ui(self):
        """创建 UI"""
        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)

        layout.addLayout(self._create_text_row())
        layout.addLayout(self._create_size_row())
        layout.addLayout(self._create_align_row())

        self.setLayout(layout)
        self._connect_internal_signals()

    def _create_text_row(self):
        """创建文本内容行

        包含：
        - 标签: "Text cont"
        - 输入框: 支持拖入参数的文本输入
        - 下拉框: 文本类型选择 (Text/Parm/Hscript/Python)
        """
        item = self.item
        self._label_text = Snail_LabelA("Text cont")
        self._line_text = Snail_DropLine(item.text, "Set text content", None, self._on_drop_parm)
        text_types = [
            ("snail_text", "Text"),
            ("snail_parm", "Parm"),
            ("BUTTONS_hscript", "Hscript"),
            ("MISC_python", "Python"),
        ]
        self._combo_text_type = Snail_ComboBox(text_types)
        self._combo_text_type.setCurrentIndex(item.text_type)

        layout = QHBoxLayout()
        layout.addWidget(self._label_text)
        layout.addWidget(self._line_text)
        layout.addWidget(self._combo_text_type)
        return layout

    def _create_size_row(self):
        """创建字体样式行

        包含：
        - 标签: "Text size"
        - 下拉框: 字体大小 (1-7)
        - 复选框: 粗体
        - 复选框: 斜体
        - [弹性空间]
        - 复选框: 数字填充
        - 微调框: 前缀位数 (00.)
        - 微调框: 后缀位数 (.00)
        """
        item = self.item
        self._label_size = Snail_LabelA("Text size")
        sizes = [str(i) for i in range(1, 8)]
        self._combo_size = Snail_ComboBox(sizes)
        self._combo_size.setFixedWidth(60)
        self._combo_size.set_radius("none")
        self._combo_size.setCurrentText(str(item.text_size))

        self._cb_bold = Snail_CheckBox("Bold")
        self._cb_bold.set_radius("none")
        self._cb_bold.setChecked(item.text_bold)
        self._cb_italic = Snail_CheckBox("Italic")
        self._cb_italic.set_radius("right")
        self._cb_italic.setChecked(item.text_italic)
        self._cb_digit = Snail_CheckBox("Digit")
        self._cb_digit.set_radius("left")
        self._cb_digit.setChecked(item.num_fill)

        self._spinbox_pre = Snail_SpinBox("00. ", None, 1, 10, 100)
        self._spinbox_pre.set_radius("none")
        self._spinbox_pre.setValue(item.num_pre)
        self._spinbox_pre.setDisabled(not item.num_fill)
        self._spinbox_suf = Snail_SpinBox(".00 ", None, 0, 10, 100)
        self._spinbox_suf.set_radius("right")
        self._spinbox_suf.setValue(item.num_suf)
        self._spinbox_suf.setDisabled(not item.num_fill)

        layout = QHBoxLayout()
        layout.addWidget(self._label_size)
        layout.addWidget(self._combo_size)
        layout.addWidget(self._cb_bold)
        layout.addWidget(self._cb_italic)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addWidget(self._cb_digit)
        layout.addWidget(self._spinbox_pre)
        layout.addWidget(self._spinbox_suf)
        return layout

    def _create_align_row(self):
        """创建对齐和样式行

        包含：
        - 标签: "Align pos"
        - 下拉框: 对齐位置 (8种方位)
        - 微调框: X边距
        - 微调框: Y边距
        - [弹性空间]
        - 标签: "Color"
        - 按钮: 颜色选择
        - 按钮: 关闭(删除此项)
        """
        item = self.item
        self._label_align = Snail_LabelA("Align pos")
        aligns = [
            ("snail_align0", "LB"),
            ("snail_align1", "CB"),
            ("snail_align2", "RB"),
            ("snail_align3", "LC"),
            ("snail_align4", "RC"),
            ("snail_align5", "LT"),
            ("snail_align6", "CT"),
            ("snail_align7", "RT"),
        ]
        self._combo_align = Snail_ComboBox(aligns)
        self._combo_align.setFixedWidth(80)
        self._combo_align.setCurrentIndex(item.rel_pos)
        self._spinbox_margin_x = Snail_SpinBox("X  ", None, -1000, 1000, 100)
        self._spinbox_margin_x.set_radius("none")
        self._spinbox_margin_x.setValue(item.margin_x)
        self._spinbox_margin_y = Snail_SpinBox("Y  ", None, -1000, 1000, 100)
        self._spinbox_margin_y.set_radius("right")
        self._spinbox_margin_y.setValue(item.margin_y)
        self._label_color = Snail_LabelA("Color", width=60)
        self._btn_color = Snail_ColorBtn()
        self._btn_color.set_radius("right")
        if item.color:
            self._btn_color.changeColor(item.color)
        else:
            color = self._btn_color.set_randomColor()
            item.color = color
        self._btn_close = Snail_IconBtn("BUTTONS_close")

        layout = QHBoxLayout()
        layout.addWidget(self._label_align)
        layout.addWidget(self._combo_align)
        layout.addWidget(self._spinbox_margin_x)
        layout.addWidget(self._spinbox_margin_y)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addWidget(self._label_color)
        layout.addWidget(self._btn_color)
        layout.addWidget(self._btn_close)
        return layout

    def _connect_internal_signals(self):
        """连接内部信号槽

        将所有 UI 控件的信号连接到对应的处理方法，
        属性变更会自动同步到数据模型并触发 viewport 更新。
        """
        # 文本内容行
        self._line_text.textChanged.connect(self._on_text_changed)
        self._combo_text_type.currentIndexChanged.connect(self._on_text_type_changed)
        # 字体样式行
        self._combo_size.currentIndexChanged.connect(self._on_text_size_changed)
        self._cb_bold.clicked.connect(self._on_bold_toggled)
        self._cb_italic.clicked.connect(self._on_italic_toggled)
        self._cb_digit.clicked.connect(self._on_fill_toggled)
        self._spinbox_pre.valueChanged.connect(self._on_pre_changed)
        self._spinbox_suf.valueChanged.connect(self._on_suf_changed)
        # 对齐和样式行
        self._combo_align.currentIndexChanged.connect(self._on_align_changed)
        self._spinbox_margin_x.valueChanged.connect(self._on_margin_x_changed)
        self._spinbox_margin_y.valueChanged.connect(self._on_margin_y_changed)
        self._btn_color.clicked.connect(self._on_color_clicked)
        self._btn_close.clicked.connect(self._on_close_clicked)

    def _notify_changed(self):
        """通知 viewport 更新

        当文字项属性变更时，通过主窗口回调触发 viewport 刷新。
        """
        if self._main_window:
            self._main_window.on_text_item_changed()

    def _update_digit_ui(self):
        """更新数字填充相关 UI 状态

        当数字填充选项改变时，启用/禁用前缀和后缀微调框。
        """
        self._spinbox_pre.setDisabled(not self.item.num_fill)
        self._spinbox_suf.setDisabled(not self.item.num_fill)

    # ========================================================================
    # 内部信号槽处理方法
    # ========================================================================

    def _on_text_changed(self):
        """文本内容输入框变更"""
        self.item.text = self._line_text.text()
        self._notify_changed()

    def _on_text_type_changed(self):
        """文本类型下拉框变更"""
        self.item.text_type = self._combo_text_type.currentIndex()
        self._notify_changed()

    def _on_text_size_changed(self):
        """字体大小下拉框变更"""
        self.item.text_size = int(self._combo_size.currentText())
        self._notify_changed()

    def _on_bold_toggled(self):
        """粗体复选框变更"""
        self.item.text_bold = self._cb_bold.isChecked()
        self._notify_changed()

    def _on_italic_toggled(self):
        """斜体复选框变更"""
        self.item.text_italic = self._cb_italic.isChecked()
        self._notify_changed()

    def _on_fill_toggled(self):
        """数字填充复选框变更"""
        self.item.num_fill = self._cb_digit.isChecked()
        self._update_digit_ui()
        self._notify_changed()

    def _on_pre_changed(self):
        """前缀位数微调框变更"""
        self.item.num_pre = self._spinbox_pre.value()
        self._notify_changed()

    def _on_suf_changed(self):
        """后缀位数微调框变更"""
        self.item.num_suf = self._spinbox_suf.value()
        self._notify_changed()

    def _on_align_changed(self):
        """对齐位置下拉框变更"""
        self.item.rel_pos = self._combo_align.currentIndex()
        self._notify_changed()

    def _on_margin_x_changed(self):
        """X边距微调框变更"""
        self.item.margin_x = self._spinbox_margin_x.value()
        self._notify_changed()

    def _on_margin_y_changed(self):
        """Y边距微调框变更"""
        self.item.margin_y = self._spinbox_margin_y.value()
        self._notify_changed()

    def _on_color_clicked(self):
        """颜色按钮点击 - 打开颜色选择对话框"""
        rgb = self._btn_color.changeColor(None)
        if rgb:
            self.item.color = rgb
        self._notify_changed()

    def _on_close_clicked(self):
        """关闭按钮点击 - 删除此文字项"""
        if self._main_window:
            self._main_window.on_delete_text(self.item_id)

    def _on_drop_parm(self, parm_path, node_path):
        """拖拽参数到文本输入框的回调处理

        Args:
            parm_path: 拖入的参数路径
            node_path: 拖入的节点路径 (不支持)
        """
        if parm_path:
            parm_paths = parm_path.split()
            if len(parm_paths) > 1:
                parm_path = parm_paths[1][:-1]
            self._line_text.setText(parm_path)
            self.item.text = parm_path
            self._combo_text_type.setCurrentIndex(1)  # 切换到 Parm 模式
        if node_path:
            hou.ui.displayMessage("Please drop Parameter, not drop Node")

    def sizeHint(self):
        return QtCore.QSize(100, 96)

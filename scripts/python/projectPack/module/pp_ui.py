# -*- coding: utf-8 -*-

import os
import hou
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from utils import *
from utils.imageViewer import ImageViewer
from .pp_set import PPSET


class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(
            ALLSET.sbox_path + "/file/icon01/SnailBox.svg"))
        self.setWindowTitle("SnailBox Assets Settings")
        self.setStyleSheet("*{background-color: rgb(35, 35, 39);}")
        self.resize(500, 300)
        self.setWindowFlags(
            self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint
            | QtCore.Qt.WindowCloseButtonHint
        )

        layout = QVBoxLayout()
        self.tip_2 = Snail_Label("File formats separated by spaces, lowercase")
        self.tip_2.setFixedHeight(25)
        layout.addWidget(self.tip_2)

        for i in range(7):
            layout_1a = QHBoxLayout()
            layout_1b = QHBoxLayout()
            label_1 = Snail_LabelA(f"Class {i+1}")
            class_1 = Snail_LineEdit()
            class_1.setFixedWidth(200)
            format_1 = Snail_LineEdit()

            setattr(self, f"class_{i+1}", class_1)
            setattr(self, f"format_{i+1}", format_1)
            layout_1a.addWidget(label_1)
            layout_1a.addWidget(class_1)
            layout_1b.addWidget(format_1)
            if i == 0:
                self.tip_1 = Snail_Label("Categorized folder name")
                self.tip_1.setFixedHeight(25)
                layout_1a.addWidget(self.tip_1)
            else:
                spacer = QSpacerItem(
                    0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
                layout_1a.addItem(spacer)

            layout.addLayout(layout_1a)
            layout.addLayout(layout_1b)
            layout.addWidget(Snail_line())

        self.cb_1 = Snail_CheckBox(
            "Ignore Cache nodes that are not activated Load from Disk.")
        self.cb_2 = Snail_CheckBox("Ignore Bypass nodes.")
        self.cb_3 = Snail_CheckBox("Ignore locked HDA nodes.")
        self.cb_4 = Snail_CheckBox("Package all network editor node preview images.")
        self.cb_5 = Snail_CheckBox("Package file preview images.")
        layout.addWidget(self.cb_1)
        layout.addWidget(self.cb_2)
        layout.addWidget(self.cb_3)
        layout.addWidget(self.cb_4)
        layout.addWidget(self.cb_5)
        layout.addWidget(Snail_line())

        layout_3 = QHBoxLayout()
        self.btn_2 = Snail_Btn("Cancel")
        self.btn_2.clicked.connect(self.close)
        self.btn_1 = Snail_Btn("Save")
        layout_3.addWidget(self.btn_2)
        layout_3.addWidget(self.btn_1)
        layout.addLayout(layout_3)

        self.setLayout(layout)
        # 设置对话框为模态窗口
        self.setModal(True)


class Ui_Main(QWidget):
    """主界面布局类 (手写重建，参照 recipeBox)

    职责：
        - 创建和管理所有 UI 控件和布局
        - 信号槽全部内部处理
        - 表格刷新、信息显示、预览图显示
        - 过滤、点击、右键菜单、工具栏按钮、搜索替换、路径切换
        - 背景样式
        - 跨组件操作(打包、设置对话框)通过回调调用父窗口

    设计原则：
        - 拥有完整 UI 自主权，不依赖父窗口操作任何 UI 控件
        - 文件/节点逻辑通过 self._manager(AllFiles) 访问
        - 打包、设置对话框、语言切换等重活调用 self.pa(PP_Win) 完成
    """

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.pa = parent
        self._manager = manager
        self.show_ignore = False
        self.info_flip_index = 0

        # 语言文本默认值(英文)，语言切换时由 PP_Win.retranslateUi 覆写
        self.tr_localization = "Local Path"
        self.tr_absolutePath = "Absolute Path"
        self.tr_customPath = "Custom Path"
        self.tr_replace = "Replace File"
        self.tr_goNode = "Go Node"
        self.tr_bigView = "Big View"
        self.tr_openInExplorer = "Open Folder"
        self.tr_toggleIgnore = "Toggle Ignore"
        self.tr_toggleUsdFolder = "USD Folder"

        # 背景 (参照 recipeBox)
        self.setStyleSheet("*{background-color: #2d2d2d;}")

        self.yes_icon = Snail_icon("STATUS_yes")
        self.no_icon = Snail_icon("STATUS_no")
        self.img_viewer = ImageViewer()

        self._setup_main_layout()
        self._connect_internal_signals()
        self.init_format_list()

    # ========================================================================
    # 布局创建
    # ========================================================================

    def _setup_main_layout(self):
        self.setObjectName("Snail_PP_ui")
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        self.resize(760, 660)

        self.layout_main = QVBoxLayout(self)
        self.layout_main.setSpacing(0)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_main)

        self._create_row_filter()
        self._create_search_bar()
        self._create_table_splitter()
        self._create_format_row()
        self.layout_main.addWidget(self._make_line())
        self._create_path_row()
        self.layout_main.addWidget(self._make_line())
        self._create_bottom_bar()

    def _make_line(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line

    def _create_row_filter(self):
        self.v0 = QHBoxLayout()
        self.cb_cacheNode = Snail_CheckBox("Cache node")
        self.cb_cacheNode.setChecked(True)
        self._tint_checkbox(self.cb_cacheNode, QtGui.QColor(255, 170, 0))
        self.v0.addWidget(self.cb_cacheNode)

        self.cb_renderNode = Snail_CheckBox("Render node")
        self._tint_checkbox(self.cb_renderNode, QtGui.QColor(150, 104, 236))
        self.v0.addWidget(self.cb_renderNode)

        self.cb_soloNonlocal = Snail_CheckBox("Solo non local")
        self._tint_checkbox(self.cb_soloNonlocal, QtGui.QColor(85, 170, 255))
        self.v0.addWidget(self.cb_soloNonlocal)

        self.cb_soloError = Snail_CheckBox("Solo error")
        self._tint_checkbox(self.cb_soloError, QtGui.QColor(231, 93, 99))
        self.v0.addWidget(self.cb_soloError)

        self.v0.addSpacerItem(
            QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        self._create_tool_buttons()
        for btn in (self.tb_goNode, self.tb_bigView, self.tb_folder,
                    self.tb_ignore, self.tb_search, self.tb_flip):
            self.v0.addWidget(btn)

        self.layout_main.addLayout(self.v0)

    def _tint_checkbox(self, cb, color):
        """用调色板给勾选框文字上色，不覆盖 Snail_CheckBox 自带的字体/背景"""
        pal = cb.palette()
        pal.setColor(QtGui.QPalette.WindowText, color)
        pal.setColor(QtGui.QPalette.ButtonText, color)
        cb.setPalette(pal)

    def _create_tool_buttons(self):
        self.tb_goNode = Snail_IconBtn("NETWORKS_sop", "Go to node")
        self.tb_bigView = Snail_IconBtn("snail_big_viewer", "Zoom view")
        self.tb_folder = Snail_IconBtn("BUTTONS_folder", "Open File folder")
        self.tb_ignore = Snail_IconBtn2("snail_ignore1", "snail_ignore2", "Toggle ignore")
        self.tb_search = Snail_IconBtn("BUTTONS_search", "Search and replace")
        self.tb_flip = Snail_IconBtn2("snail_info_flip1", "snail_info_flip2", "Flip info")

    def _create_search_bar(self):
        self.w_search = QWidget(self)
        self.w_search.setHidden(True)
        self.v4 = QHBoxLayout(self.w_search)
        self.v4.setSpacing(6)
        self.v4.setContentsMargins(8, 0, 8, -1)

        self.le_s1 = Snail_LineEdit()
        self.le_s1.setPlaceholderText("Search")
        self.le_s2 = Snail_LineEdit()
        self.le_s2.setPlaceholderText("Replace")
        self.btn_replace = Snail_Btn("Replace")
        self.btn_replace.setFixedWidth(100)

        self.v4.addWidget(self.le_s1)
        self.v4.addWidget(self.le_s2)
        self.v4.addWidget(self.btn_replace)
        self.layout_main.addWidget(self.w_search)

    def _create_table_splitter(self):
        # 表格
        self.tableWidget = QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(
            ["File path", "Node", "Class", "State"])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setColumnWidth(0, 360)
        self.tableWidget.setColumnWidth(1, 170)
        self.tableWidget.setColumnWidth(2, 60)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        # info_splitter：信息 + 预览图 (无标题，参照 recipeBox)
        self.lw_info = Snail_List2(self)
        self.lw_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thumb_viewer = Snail_thumbViewer()
        self.splitter = QSplitter(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.lw_info)
        self.splitter.addWidget(self.thumb_viewer)
        self.splitter.setSizes([100, 100])  # 默认 50:50

        # splitter_v：上表格，下 info_splitter
        self.splitter_v = QSplitter(QtCore.Qt.Vertical)
        self.splitter_v.addWidget(self.tableWidget)
        bottom = QWidget()
        self.layout_v = QVBoxLayout(bottom)
        self.layout_v.setSpacing(0)
        self.layout_v.setContentsMargins(0, 0, 0, 0)
        self.layout_v.addWidget(self.splitter)
        self.splitter_v.addWidget(bottom)
        # 表格占满余量，info 为底部面板 (参照 recipe 的信息面板比例)
        self.splitter_v.setStretchFactor(0, 1)
        self.splitter_v.setStretchFactor(1, 0)
        self.splitter_v.setSizes([700, 220])

        # splitter_h：左 splitter_v，右 layout_h
        self.splitter_h = QSplitter(QtCore.Qt.Horizontal)
        left = QWidget()
        lay_l = QVBoxLayout(left)
        lay_l.setSpacing(0)
        lay_l.setContentsMargins(0, 0, 0, 0)
        lay_l.addWidget(self.splitter_v)
        self.splitter_h.addWidget(left)
        self.splitter_h.setSizes([100, 0])  # 初始收起翻转面板

        right = QWidget()
        self.layout_h = QVBoxLayout(right)
        self.layout_h.setSpacing(0)
        self.layout_h.setContentsMargins(0, 0, 0, 0)
        self.splitter_h.addWidget(right)

        self.layout_main.addWidget(self.splitter_h)

    def _create_format_row(self):
        self.v2 = QHBoxLayout()
        for i in range(1, 8):
            cb = Snail_CheckBox("Format_%02d" % i)
            cb.setChecked(True)
            setattr(self, "checkBox_%d" % i, cb)
            self.v2.addWidget(cb)
        self.layout_main.addLayout(self.v2)

    def _create_path_row(self):
        self.v5 = QHBoxLayout()
        # 使用 snailWidget 控件（YaHei 字体 + 深色样式），保证中文路径显示正常
        self.p_Path = Snail_LabelA("Path:", width=50)
        self.v5.addWidget(self.p_Path)

        self.label_5 = Snail_LineEdit()
        self.label_5.setReadOnly(True)
        self.label_5.setMinimumWidth(400)
        self.v5.addWidget(self.label_5)

        self.radioButton_2 = QRadioButton("HIP")
        self.radioButton_2.setChecked(True)
        self.radioButton = QRadioButton("JOB")
        self.v5.addWidget(self.radioButton_2)
        self.v5.addWidget(self.radioButton)

        self.btn_pfolder = Snail_Btn("Project folder")
        self.v5.addWidget(self.btn_pfolder)
        self.layout_main.addLayout(self.v5)

    def _create_bottom_bar(self):
        self.v6 = QHBoxLayout()
        self.tb_set = Snail_IconBtn("snail_set", "Settings")
        self.tb_bz = Snail_IconBtn_bz()
        self.tb_help = Snail_IconBtn_help()
        self.tb_language = Snail_IconBtn("snail_language", "Toggle language")
        self.btn_pack = Snail_Btn("Pack Project")
        self.btn_refresh = Snail_Btn("Refresh")
        for w in (self.tb_set, self.tb_bz, self.tb_help,
                  self.tb_language, self.btn_pack, self.btn_refresh):
            self.v6.addWidget(w)
        self.layout_main.addLayout(self.v6)

    # ========================================================================
    # 信号连接
    # ========================================================================

    def _connect_internal_signals(self):
        self.cb_cacheNode.toggled.connect(self.refresh)
        self.cb_renderNode.toggled.connect(self.refresh)
        self.cb_soloNonlocal.toggled.connect(self.refresh)
        self.cb_soloError.toggled.connect(self.refresh)

        self.tb_goNode.clicked.connect(self.on_go_node)
        self.tb_bigView.clicked.connect(self.on_big_view)
        self.tb_folder.clicked.connect(self.on_open_folder)
        self.tb_ignore.clicked.connect(self.on_toggle_show_ignore)
        self.tb_search.clicked.connect(self.on_toggle_show_search)
        self.tb_flip.clicked.connect(self.on_flip_info)

        self.btn_replace.clicked.connect(self.on_replace_string)
        self.btn_pfolder.clicked.connect(self.on_open_project_folder)
        self.radioButton.toggled.connect(self.on_toggle_local_set)

        self.tb_set.clicked.connect(self.pa.open_settings)
        self.btn_pack.clicked.connect(self.pa.pack_project)
        self.btn_refresh.clicked.connect(self.refresh)
        self.tb_language.clicked.connect(self.pa.toggle_language)

        self.tableWidget.itemClicked.connect(self.on_click)
        self.tableWidget.itemDoubleClicked.connect(self.on_double_click)
        self.tableWidget.customContextMenuRequested.connect(self.on_right_click)
        self.splitter_h.splitterMoved.connect(self.on_stop_flip_move)
        self.splitter_v.splitterMoved.connect(self.on_stop_flip_move)

    # ========================================================================
    # 刷新
    # ========================================================================

    def refresh(self):
        self.set_local_path()
        self._manager.refresh()
        self._refresh_table()

    def _files_filter(self):
        fileFilterDict = {}
        for id, file in self._manager.file_dict.items():
            try:
                fileclass = file.fileClass
                if not fileclass:
                    continue
                file_class_index = PPSET.formatKeys.index(fileclass)
                checkBox = getattr(self, "checkBox_" + str(file_class_index + 1))
                if not checkBox.isChecked():
                    continue
                if PPSET.bypass and file.Bypass == 1:
                    continue
                if PPSET.cacheDisk and file.unloadFromdisk == 1:
                    continue
                if not self.cb_cacheNode.isChecked() and file.isCacheNode > 0:
                    continue
                if self.cb_soloNonlocal.isChecked() and file.local == 1:
                    continue
                if not self.cb_renderNode.isChecked() and file.render == 1:
                    continue
                if self.cb_soloError.isChecked() and file.abs_path:
                    continue
                if not self.show_ignore and file.ignore == 1:
                    continue
                fileFilterDict[id] = file
            except Exception as e:
                display_status(f"Snail_error_pp0: filesFilter {file.parm} _ {e}")
        return fileFilterDict

    def get_filter_ids(self):
        return list(self._files_filter().keys())

    def _refresh_table(self):
        fileFilterDict = self._files_filter()
        oldSort = self.tableWidget.horizontalHeader().sortIndicatorSection()
        oldOrder = self.tableWidget.horizontalHeader().sortIndicatorOrder()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(fileFilterDict))
        row = 0
        for id, item_obj in fileFilterDict.items():
            try:
                file_path = item_obj.filePath
                file_icon = self.yes_icon if item_obj.abs_path else self.no_icon
                tableItem_0 = QTableWidgetItem(file_icon, file_path)
                tableItem_0.setData(QtCore.Qt.UserRole, id)
                self.tableWidget.setItem(row, 0, tableItem_0)

                icon_name = hou.node(item_obj.nodePath).type().icon()
                node_icon = hou.qt.Icon(icon_name)
                self.tableWidget.setItem(row, 1, QTableWidgetItem(node_icon, item_obj.nodePath))

                self.tableWidget.setItem(row, 2, QTableWidgetItem(item_obj.fileClass))

                status = item_obj.status
                tableItem_3 = QTableWidgetItem(status)
                tableItem_3.setForeground(QtGui.QBrush(item_obj.statusColor))
                self.tableWidget.setItem(row, 3, tableItem_3)
                row += 1
            except Exception as e:
                display_status(f"Snail_error_pp0: refreshTable {item_obj.filePath} _ {e}")
        self.tableWidget.sortItems(oldSort, oldOrder)
        self.tableWidget.setSortingEnabled(True)

    def _selected_ids(self):
        btnItems = self.tableWidget.selectedItems()
        if not btnItems:
            msg = "请在表格中选择一项" if ALLSET.language else "Please select one item"
            hou.ui.displayMessage(msg)
            return None
        ids = [item.data(QtCore.Qt.UserRole) for item in btnItems if item.column() == 0]
        return ids or None

    def _refresh_info(self, ids):
        try:
            self.lw_info.clear()
            item_obj = self._manager.file_dict[ids[0]]
            info_dict = item_obj.file_info
            self._refresh_thumb(ids)
            if not info_dict:
                return
            for key, value in info_dict.items():
                self.lw_info.add_item(key, value, readOnly=True)
        except Exception as e:
            display_status(f"Snail_error_pp0: RefreshInfo _ {e}")

    def _refresh_thumb(self, ids):
        try:
            item_obj = self._manager.file_dict.get(ids[0])
            if not item_obj or not item_obj.thumbnail:
                self.thumb_viewer.set_image(None)
            else:
                thumbnail_abs = hou.text.expandString(item_obj.thumbnail)
                self.thumb_viewer.set_image(thumbnail_abs)
        except Exception as e:
            display_status(f"Snail_error_pp0: RefreshThumb _ {e}")

    # ========================================================================
    # 点击 / 双击 / 右键
    # ========================================================================

    def on_click(self):
        ids = self._selected_ids()
        if ids:
            self._refresh_info(ids)

    def on_double_click(self, item):
        column = item.column()
        if column == 0:
            self.on_big_view()
        elif column == 1:
            self.on_go_node()
        elif column == 3:
            self.on_open_folder()

    def on_right_click(self, position):
        try:
            btnItems = self.tableWidget.selectedItems()
            ids = [item.data(QtCore.Qt.UserRole) for item in btnItems if item.column() == 0]
            if ids:
                menu = Snail_Menu()
                menu.addAction(self.tr_localization, self.on_local_path)
                menu.addAction(self.tr_absolutePath, self.on_absolute_path)
                menu.addAction(self.tr_customPath, self.on_custom_path)
                if len(ids) == 1:
                    menu.addAction(self.tr_replace, self.on_replace_file)
                    menu.addAction(self.tr_goNode, self.on_go_node)
                    menu.addAction(self.tr_bigView, self.on_big_view)
                    menu.addAction(self.tr_openInExplorer, self.on_open_folder)
                menu.addAction(self.tr_toggleIgnore, self.on_toggle_ignore)
                menu.addAction(self.tr_toggleUsdFolder, self.on_toggle_usd)
                menu.addSeparator()
                menu.exec_(self.tableWidget.viewport().mapToGlobal(position))
        except Exception as e:
            display_status(f"Snail_error_pp0: rightClickContext _ {e}")

    # ========================================================================
    # 文件/节点操作
    # ========================================================================

    def on_local_path(self):
        ids = self._selected_ids()
        if ids:
            self._manager.copyfile(ids)
            self.refresh()

    def on_absolute_path(self):
        ids = self._selected_ids()
        if ids:
            self._manager.absPath(ids)
            self.refresh()

    def on_custom_path(self):
        ids = self._selected_ids()
        if not ids:
            return
        targetPath = self.pa.browse_path()
        if targetPath and ids:
            self._manager.copyfile(ids, targetPath)
            self.refresh()

    def on_replace_file(self):
        ids = self._selected_ids()
        if not ids:
            return
        self._manager.file_dict[ids[0]].replaceFile()
        self.refresh()

    def on_go_node(self):
        ids = self._selected_ids()
        if ids:
            self._manager.file_dict[ids[0]].goNode()

    def on_open_folder(self):
        ids = self._selected_ids()
        if ids:
            self._manager.file_dict[ids[0]].openInExplorer()

    def on_big_view(self):
        ids = self._selected_ids()
        if not ids:
            return
        item_obj = self._manager.file_dict[ids[0]]
        if not item_obj.abs_path:
            msg = "文件未找到" if ALLSET.language else "File not found"
            hou.ui.displayMessage(msg)
            return
        if item_obj.extension in ALLSET.img_formats:
            self.show_img(item_obj.abs_path)
        else:
            item_obj.solo_node(1)

    def show_img(self, path_abs):
        try:
            if not path_abs:
                return
            if self.img_viewer.isMinimized():
                self.img_viewer.showNormal()
            if self.img_viewer.isHidden():
                right_x = self.geometry().x() + self.width()
                right_y = self.geometry().y()
                height = self.height()
                self.img_viewer.setGeometry(right_x, right_y, height, height)
            self.img_viewer.refresh(path_abs)
            self.img_viewer.raise_()
        except Exception as e:
            display_status(f"Snail_error_pp0: show_img _ {e}")

    # ========================================================================
    # 过滤 / 搜索 / 路径
    # ========================================================================

    def on_toggle_show_ignore(self):
        self.show_ignore = not self.show_ignore
        self._refresh_table()

    def on_toggle_ignore(self):
        ids = self._selected_ids()
        if ids:
            self._manager.setIgnore(ids)
            self._refresh_table()

    def on_toggle_usd(self):
        ids = self._selected_ids()
        if ids:
            self._manager.toggleUsdFolder(ids)
            self._refresh_table()

    def on_toggle_show_search(self):
        self.w_search.setHidden(not self.w_search.isHidden())

    def on_replace_string(self):
        text1 = self.le_s1.text()
        text2 = self.le_s2.text()
        if not text1:
            return
        search = text1.replace("\\", "/")
        replace = text2.replace("\\", "/")
        fileFilterList = self._files_filter()
        for id, oneObj in fileFilterList.items():
            try:
                filePath = oneObj.filePath.replace("\\", "/")
                if search not in filePath:
                    continue
                newPath = filePath.replace(search, replace)
                oneObj.setParm(newPath)
            except Exception as e:
                display_status(f"Snail_error_pp0: replaceString _ {e}")
        self.refresh()

    def set_local_path(self):
        try:
            isHip = self.radioButton_2.isChecked()
            PPSET.localSet = "$HIP" if isHip else "$JOB"
            projectPath = hou.text.expandString(PPSET.localSet)
            # 只读输入框保留完整路径（可选中复制），不再手动省略号截断
            self.label_5.setText(projectPath)
        except Exception as e:
            display_status(f"Snail_error_pp0: setLocalPath _ {e}")

    def on_toggle_local_set(self):
        self.set_local_path()
        self.refresh()

    def on_open_project_folder(self):
        try:
            self.set_local_path()
            packPath = self.label_5.text()
            if not os.path.exists(packPath):
                msg = "工程路径不存在" if ALLSET.language else "Project path does not exist"
                hou.ui.displayMessage(msg)
                return
            os.startfile(packPath)
        except Exception as e:
            display_status(f"Snail_error_pp0: openProjectFolder _ {e}")

    # ========================================================================
    # 信息面板翻转
    # ========================================================================

    def on_stop_flip_move(self):
        if self.info_flip_index:
            self.splitter_v.setSizes([100, 0])
        else:
            self.splitter_h.setSizes([100, 0])

    def on_flip_info(self):
        try:
            if self.splitter.orientation() == QtCore.Qt.Vertical:
                self.layout_h.removeWidget(self.splitter)
                vsizes = self.splitter_v.sizes()
                vsize2 = [vsizes[1] + vsizes[0] - 160, 160]
                self.splitter_v.setSizes(vsize2)
                self.splitter_h.setSizes([100, 0])
                self.info_flip_index = 0
                self.layout_v.addWidget(self.splitter)
                self.splitter.setOrientation(QtCore.Qt.Horizontal)
            else:
                self.layout_v.removeWidget(self.splitter)
                hsizes = self.splitter_h.sizes()
                hsize2 = [hsizes[1] + hsizes[0] - 160, 160]
                self.splitter_h.setSizes(hsize2)
                self.splitter_v.setSizes([100, 0])
                self.info_flip_index = 1
                self.layout_h.addWidget(self.splitter)
                self.splitter.setOrientation(QtCore.Qt.Vertical)
        except Exception as e:
            display_status(f"Snail_error_pp0: FlipInfo _ {e}")

    # ========================================================================
    # 分类复选框
    # ========================================================================

    def init_format_list(self):
        keyList = PPSET.formatKeys
        for i in range(1, 8):
            try:
                checkBox = getattr(self, "checkBox_" + str(i))
                checkBox.toggled.connect(self.refresh)
                if i <= len(keyList):
                    checkBox.setHidden(False)
                    checkBox.setText(keyList[i - 1])
                else:
                    checkBox.setHidden(True)
            except Exception as e:
                display_status(f"Snail_error_pp0: init_format_list _ {e}")

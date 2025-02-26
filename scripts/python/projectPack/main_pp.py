import os
import hou
from .module import *
from utils import *
from utils.imgViewer import ImgViewer


class PP_Win(QWidget):
    def __init__(self):
        super().__init__()
        self.show_ignore = False
        self.filesObj = None
        self.formatDir = {}
        self.info_flip_index = 0

        self.translator = QtCore.QTranslator()
        QApplication.installTranslator(self.translator)

        self.init_ui()
        self.init_data()

    def init_ui(self):
        self.ui = Ui_Snail_PP()
        self.ui.setupUi(self.ui)
        self.ui2 = Ui_Dialog()
        self.setStyleSheet("*{background-color: rgb(35, 35, 39);}")

        self.table = self.ui.tableWidget
        mainlayout = QVBoxLayout()
        mainlayout.setSpacing(0)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.addWidget(self.ui)
        self.setLayout(mainlayout)
        self.resize(760, 660)
        self.setWindowTitle("SnailBox Assets Manager")
        self.setWindowIcon(Snail_icon("SnailBox"))

        self.yes_icon = Snail_icon("STATUS_yes")
        self.no_icon = Snail_icon("STATUS_no")

        self.ui.lw_info = QListWidget(self.ui)
        self.ui.lw_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.lw_info.setGridSize(QtCore.QSize(0, 25))
        self.ui.lw_info.setStyleSheet(
            "QListWidget {font-family: Microsoft YaHei UI;font-size: 10pt;}"
            "QListWidget::item { background-color: rgb(45,45,45); border-radius: 4px; padding: 2px;}"
            "QListWidget::item:hover {color: rgb(255,163,32); border-radius: 5px; border: 2px solid rgb(255,163,32);}"
        )
        self.ui.layout_info.addWidget(self.ui.lw_info)
        self.ui.splitter_h.splitterMoved.connect(self.stop_flipMove)
        self.ui.splitter_v.splitterMoved.connect(self.stop_flipMove)

        self.thumb_viewer = thumbViewer()
        self.img_viewer = ImgViewer()
        self.ui.layout_asset.addWidget(self.thumb_viewer)
        self.table.itemClicked.connect(self.click_item)
        self.table.itemDoubleClicked.connect(self.doubleClick_item)
        self.ui.w_search.setHidden(True)

        self.tb_goNode = Snail_IconBtn("NETWORKS_sop", "Go to node")
        self.tb_goNode.clicked.connect(self.goToNode)
        self.ui.v0.addWidget(self.tb_goNode)
        self.tb_bigView = Snail_IconBtn("snail_big_viewer", "Zoom view")
        self.tb_bigView.clicked.connect(self.big_view)
        self.ui.v0.addWidget(self.tb_bigView)
        self.tb_folder = Snail_IconBtn("BUTTONS_folder", "Open File folder")
        self.tb_folder.clicked.connect(self.openInExplorer)
        self.ui.v0.addWidget(self.tb_folder)
        self.tb_ignore = Snail_IconBtn2("snail_ignore1", "snail_ignore2", "Toggle ignore")
        self.tb_ignore.clicked.connect(self.toggle_showIgnore)
        self.ui.v0.addWidget(self.tb_ignore)
        self.tb_search = Snail_IconBtn("BUTTONS_search", "Search and replace")
        self.tb_search.clicked.connect(self.toggle_showSearch)
        self.ui.v0.addWidget(self.tb_search)
        self.tb_flip = Snail_IconBtn2("snail_info_flip1", "snail_info_flip2", "Flip info")
        self.tb_flip.clicked.connect(self.flip_info)
        self.ui.v0.addWidget(self.tb_flip)

        self.le_s1 = Snail_LineEdit()
        self.le_s1.setPlaceholderText("Search")
        self.le_s2 = Snail_LineEdit()
        self.le_s2.setPlaceholderText("Replace")
        self.btn_replace = Snail_Btn("Replace")
        self.btn_replace.setFixedWidth(100)
        self.ui.v4.addWidget(self.le_s1)
        self.ui.v4.addWidget(self.le_s2)
        self.ui.v4.addWidget(self.btn_replace)
        self.ui.v4.setSpacing(6)
        self.btn_pfolder = Snail_Btn("Project folder")
        self.ui.v5.addWidget(self.btn_pfolder)

        self.tb_bz = Snail_IconBtn_bz()
        self.tb_help = Snail_IconBtn_help()
        self.tb_language = Snail_IconBtn("snail_language", "Toggle language")
        self.tb_language.clicked.connect(self.toggle_language)
        self.btn_refresh = Snail_Btn("Refresh")
        self.btn_pack = Snail_Btn("Pack Project")
        self.tb_set = Snail_IconBtn("snail_set", "Settings")
        self.tb_set.clicked.connect(self.openDialog)
        self.ui.v6.addWidget(self.tb_set)
        self.ui.v6.addWidget(self.tb_bz)
        self.ui.v6.addWidget(self.tb_help)
        self.ui.v6.addWidget(self.tb_language)
        self.ui.v6.addWidget(self.btn_pack)
        self.ui.v6.addWidget(self.btn_refresh)

        self.table.setColumnWidth(0, 360)
        self.table.setColumnWidth(1, 170)
        self.table.setColumnWidth(2, 60)

        self.init_format_list()

        self.ui.cb_cacheNode.toggled.connect(self.refreshTable)
        self.ui.cb_renderNode.toggled.connect(self.refreshTable)
        self.ui.cb_soloNonlocal.toggled.connect(self.refreshTable)
        self.ui.cb_soloError.toggled.connect(self.refreshTable)
        self.btn_refresh.clicked.connect(self.refresh)
        self.ui.radioButton.toggled.connect(self.toggleLocalSet)
        self.btn_pack.clicked.connect(self.packProject)
        self.btn_replace.clicked.connect(self.replaceString)
        self.btn_pfolder.clicked.connect(self.openProjectFolder)
        self.ui2.btn_1.clicked.connect(self.setFormatList)
        self.table.customContextMenuRequested.connect(lambda pos: self.rightClickContext(pos))

    def init_data(self):
        self.filesObj = AllFiles(self)
        self.load_language()
        self.refreshTable()
        self.setLocalPath()

    def filesFilter(self):
        fileFilterDict = {}

        for id, file in self.filesObj.file_dict.items():
            try:
                fileclass = file.fileClass
                if not fileclass:
                    continue
                file_class_index = PPSET.formatKeys.index(fileclass)
                checkValue = getattr(self.ui, "checkBox_" + str(file_class_index + 1)).isChecked()
                if not checkValue:
                    continue
                if PPSET.bypass and file.Bypass == 1:
                    continue
                if PPSET.cacheDisk and file.unloadFromdisk == 1:
                    continue
                if not self.ui.cb_cacheNode.isChecked() and file.isCacheNode > 0:
                    continue
                if self.ui.cb_soloNonlocal.isChecked() and file.local == 1:
                    continue
                if not self.ui.cb_renderNode.isChecked() and file.render == 1:
                    continue
                if self.ui.cb_soloError.isChecked() and file.abs_path:
                    continue
                if not self.show_ignore and file.ignore == 1:
                    continue
                fileFilterDict[id] = file
            except Exception as e:
                display_status(f"Snail_error_pp: filesFilter {file.parm} _ {e}")
        return fileFilterDict

    def refreshTable(self):
        fileFilterDict = self.filesFilter()
        oldSort = self.table.horizontalHeader().sortIndicatorSection()
        oldOrder = self.table.horizontalHeader().sortIndicatorOrder()
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        self.table.clearContents()

        row = 0
        self.table.setRowCount(len(fileFilterDict))
        for id, item_obj in fileFilterDict.items():
            try:
                file_path = item_obj.filePath
                if item_obj.abs_path:
                    file_icon = self.yes_icon
                else:
                    file_icon = self.no_icon
                tableItem_0 = QTableWidgetItem(file_icon, file_path)
                tableItem_0.setData(QtCore.Qt.UserRole, id)
                self.table.setItem(row, 0, tableItem_0)

                node_path = item_obj.nodePath
                icon_name = hou.node(node_path).type().icon()
                node_icon = hou.qt.Icon(icon_name)
                tableItem_1 = QTableWidgetItem(node_icon, node_path)
                self.table.setItem(row, 1, tableItem_1)

                file_class = item_obj.fileClass
                tableItem_2 = QTableWidgetItem(file_class)
                self.table.setItem(row, 2, tableItem_2)

                status = item_obj.status
                tableItem_3 = QTableWidgetItem(status)
                tableItem_3.setTextColor(item_obj.statusColor)
                self.table.setItem(row, 3, tableItem_3)

                row += 1
            except Exception as e:
                display_status(f"Snail_error_pp: refreshTable {item_obj.filePath} _ {e}")

        self.table.sortItems(oldSort, oldOrder)
        self.table.setSortingEnabled(True)

    def current_items(func):
        def wrapper(self):
            btnItems = self.table.selectedItems()
            if not btnItems:
                msg = "请在表格中选择一项" if ALLSET.language else "Please select one item"
                hou.ui.displayMessage(msg)
                return
            ids = [item.data(QtCore.Qt.UserRole) for item in btnItems if item.column() == 0]
            if not ids:
                return
            func(self, ids)

        return wrapper

    def refresh_thumb_viewer(self, ids):
        try:
            item_obj = self.filesObj.file_dict.get(ids[0])
            if not item_obj or not item_obj.thumbnail:
                self.thumb_viewer.update_img(None)
            else:
                thumbnail_abs = hou.text.expandString(item_obj.thumbnail)
                self.thumb_viewer.update_img(thumbnail_abs)
        except Exception as e:
            display_status(f"Snail_error_pp: RefreshThumb _ {e}")

    @current_items
    def refresh_info(self, ids):
        try:
            self.ui.lw_info.clear()
            item_obj = self.filesObj.file_dict[ids[0]]
            info_dict = item_obj.file_info
            self.refresh_thumb_viewer(ids)
            if not info_dict:
                return
            for key, value in info_dict.items():
                newItem = QListWidgetItem(f"{key} : {value}")
                self.ui.lw_info.addItem(newItem)
        except Exception as e:
            display_status(f"Snail_error_pp: RefreshInfo _ {e}")

    def refresh(self):
        self.setLocalPath()
        self.filesObj.refresh()
        self.refreshTable()

    def click_item(self):
        self.refresh_info()

    def doubleClick_item(self, item):
        column = item.column()
        if column == 0:
            self.big_view()
        elif column == 1:
            self.goToNode()
        elif column == 3:
            self.openInExplorer()

    @current_items
    def setlocalPath(self, ids):
        self.filesObj.copyfile(ids)
        self.refresh()

    @current_items
    def setCustomPath(self, ids):
        targetPath = self.browseLocalPath()
        if targetPath and ids:
            self.filesObj.copyfile(ids, targetPath)
            self.refresh()

    @current_items
    def setAbsolutePath(self, ids):
        self.filesObj.absPath(ids)
        self.refresh()

    @current_items
    def replaceFile(self, ids):
        item_obj = self.filesObj.file_dict[ids[0]]
        item_obj.replaceFile()
        self.refresh()

    @current_items
    def big_view(self, ids):
        item_obj = self.filesObj.file_dict[ids[0]]
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
            display_status(f"Snail_error_pp: show_img _ {e}")

    @current_items
    def goToNode(self, ids):
        item_obj = self.filesObj.file_dict[ids[0]]
        item_obj.goNode()

    @current_items
    def openInExplorer(self, ids):
        item_obj = self.filesObj.file_dict[ids[0]]
        item_obj.openInExplorer()

    def toggle_showIgnore(self):
        self.show_ignore = not self.show_ignore
        self.refreshTable()

    @current_items
    def toggleIgnore(self, ids):
        self.filesObj.setIgnore(ids)
        self.refreshTable()

    @current_items
    def toggleUsdFolder(self, ids):
        self.filesObj.toggleUsdFolder(ids)
        self.refreshTable()

    def stop_flipMove(self):
        if self.info_flip_index:
            self.ui.splitter_v.setSizes([100, 0])
        else:
            self.ui.splitter_h.setSizes([100, 0])

    def flip_info(self):  # 翻转信息面板
        try:
            font = QtGui.QFont("Microsoft YaHei UI", 9)
            self.ui.gb_asset.setFont(font)
            if self.ui.splitter.orientation() == QtCore.Qt.Vertical:
                self.ui.layout_h.removeWidget(self.ui.splitter)
                vsizes = self.ui.splitter_v.sizes()
                vsize2 = [vsizes[1] + vsizes[0] - 160, 160]
                self.ui.splitter_v.setSizes(vsize2)
                self.ui.splitter_h.setSizes([100, 0])
                self.info_flip_index = 0
                self.ui.layout_v.addWidget(self.ui.splitter)
                self.ui.splitter.setOrientation(QtCore.Qt.Horizontal)
            else:
                self.ui.layout_v.removeWidget(self.ui.splitter)
                hsizes = self.ui.splitter_h.sizes()
                hsize2 = [hsizes[1] + hsizes[0] - 160, 160]
                self.ui.splitter_h.setSizes(hsize2)
                self.ui.splitter_v.setSizes([100, 0])
                self.info_flip_index = 1
                self.ui.layout_h.addWidget(self.ui.splitter)
                self.ui.splitter.setOrientation(QtCore.Qt.Vertical)
        except Exception as e:
            display_status(f"Snail_error_pp: FlipInfo _ {e}")

    def openProjectFolder(self):
        try:
            self.setLocalPath()
            packPath = self.ui.label_5.text()
            if not os.path.exists(packPath):
                msg = "工程路径不存在" if ALLSET else "Project path does not exist"
                hou.ui.displayMessage(msg)
                return
            os.startfile(packPath)
        except Exception as e:
            display_status(f"Snail_error_pp: openProjectFolder _ {e}")

    def toggle_showSearch(self):
        hide = self.ui.w_search.isHidden()
        self.ui.w_search.setHidden(not hide)

    def replaceString(self):
        text1 = self.ui.le_s1.text()
        text2 = self.ui.le_s2.text()
        fileFilterList = self.filesFilter()
        for id, oneObj in fileFilterList.items():
            try:
                filePath = oneObj.filePath
                if text1 not in filePath:
                    continue
                newPath = filePath.replace(text1, text2)
                oneObj.setParm(newPath)
            except Exception as e:
                display_status(f"Snail_error_pp: replaceString _ {e}")
        self.refresh()

    def setLocalPath(self):
        try:
            isHip = self.ui.radioButton_2.isChecked()
            PPSET.localSet = "$HIP" if isHip else "$JOB"
            projectPath = hou.text.expandString(PPSET.localSet)
            fm = self.ui.label_5.fontMetrics()
            labelWidth = self.ui.label_5.width()
            elideNote = fm.elidedText(projectPath, QtCore.Qt.ElideRight, labelWidth)
            self.ui.label_5.setText(elideNote)
        except Exception as e:
            display_status(f"Snail_error_pp: setLocalPath _ {e}")

    def toggleLocalSet(self):
        self.setLocalPath()
        self.refresh()

    def browseLocalPath(self):
        packPath = hou.ui.selectFile(file_type=hou.fileType.Directory, title="选择路径")
        if not packPath:
            return
        if not os.path.isdir(packPath):
            packPath = os.path.dirname(packPath)
        if not os.path.exists(packPath):
            os.makedirs(packPath)
        if packPath.endswith("/"):
            packPath = packPath[:-1]
        return packPath

    def packProject(self):
        if hou.hipFile.hasUnsavedChanges():
            msg = "打包之前是否保存工程?" if ALLSET.language else "Save the project before packing?"
            if hou.ui.displayMessage(msg, buttons=("Yes", "No")) == 0:
                hou.hipFile.save()
        try:
            packPath = self.browseLocalPath()
            if not packPath:
                return
            indexs = [index for index in self.filesFilter().keys()]
            self.filesObj.packProject(indexs, PPSET.localSet, packPath)
        except:

            msg = "打包失败,回退工程" if ALLSET.language else "Pack failed, rollback"
            if hou.ui.displayMessage("打包失败,回退工程", buttons=("Yes", "No")) == 0:
                hou.hipFile.load(hou.hipFile.name(), suppress_save_prompt=True)
        self.refresh()

    def init_format_list(self):
        keyList = PPSET.formatKeys
        for i in range(1, 8):
            try:
                checkBox = getattr(self.ui, "checkBox_" + str(i))
                checkBox.toggled.connect(self.refreshTable)
                if i <= len(keyList):
                    checkBox.setHidden(False)
                    key = keyList[i - 1]
                    checkBox.setText(key)
                else:
                    checkBox.setHidden(True)
            except Exception as e:
                display_status(f"Snail_error_pp: init_format_list _ {e}")

    def openDialog(self):
        try:
            formatClass = PPSET.formatDir
            i = 1
            for key, value in formatClass.items():
                classA = "class_" + str(i)
                formatB = "format_" + str(i)
                getattr(self.ui2, classA).setText(str(key))
                var = " ".join(value)
                getattr(self.ui2, formatB).setText(str(var))
                i += 1
            self.ui2.cb_1.setChecked(PPSET.cacheDisk)
            self.ui2.cb_2.setChecked(PPSET.bypass)
            self.ui2.cb_3.setChecked(PPSET.lockedNode)
            self.ui2.cb_4.setChecked(PPSET.packThumb)
        except Exception as e:
            display_status(f"Snail_error_pp: openDialog _ {e}")
            if ALLSET.language:
                msg = "读取 conf/projectPack.json 配置文件失败"
            else:
                msg = "Failed to read conf/projectPack.json configuration file"
            hou.ui.displayMessage(msg)
        finally:
            self.ui2.show()

    def setFormatList(self):
        formatDir2 = {}
        for i in range(7):
            try:
                j = str(i + 1)
                classA = "class_" + j
                formatB = "format_" + j
                le = getattr(self.ui2, classA)
                if not le:
                    continue
                key = le.text()
                value = getattr(self.ui2, formatB).text()
                if not key or not value:
                    continue
                value2 = value.replace(",", " ")
                subList = value2.split()
                subList2 = [subf.lower() for subf in subList]
                formatDir2[key] = subList2
            except Exception as e:
                display_status(f"Snail_error_pp: setFormatList {e}")
        PPSET.formatDir = formatDir2
        PPSET.cacheDisk = self.ui2.cb_1.isChecked()
        PPSET.bypass = self.ui2.cb_2.isChecked()
        PPSET.lockedNode = self.ui2.cb_3.isChecked()
        PPSET.packThumb = self.ui2.cb_4.isChecked()

        PPSET.saveJson()
        self.init_format_list()
        self.ui2.close()
        self.refresh()

    def rightClickContext(self, position=None):
        try:
            btnItems = self.table.selectedItems()
            ids = [item.data(QtCore.Qt.UserRole) for item in btnItems if item.column() == 0]
            if ids:
                menu = Snail_Menu()
                menu.addAction(self.tr_localization, self.setlocalPath)
                menu.addAction(self.tr_absolutePath, self.setAbsolutePath)
                menu.addAction(self.tr_customPath, self.setCustomPath)
                if len(ids) == 1:
                    menu.addAction(self.tr_replace, self.replaceFile)
                    menu.addAction(self.tr_goNode, self.goToNode)
                    menu.addAction(self.tr_bigView, self.big_view)
                    menu.addAction(self.tr_openInExplorer, self.openInExplorer)
                menu.addAction(self.tr_toggleIgnore, self.toggleIgnore)
                menu.addAction(self.tr_toggleUsdFolder, self.toggleUsdFolder)
                menu.addSeparator()
                menu.exec_(self.table.viewport().mapToGlobal(position))
        except Exception as e:
            display_status(f"Snail_error_pp: rightClickContext _ {e}")

    def closeEvent(self, event):
        sc_tab = hou.ui.findPaneTab("Snail_sc2")
        if sc_tab and sc_tab.qtParentWindow():
            sc_tab.qtParentWindow().close()
        view_node = hou.node("/obj/SnailBox_view")
        if view_node:
            view_node.destroy()
        super().closeEvent(event)

    def toggle_language(self):
        ALLSET.toggle_language()
        self.load_language()

    def load_language(self):
        try:
            if ALLSET.language:
                self.translator.load(f"{ALLSET.sbox_path}/scripts/python/projectPack/tr_zh.pm")
            else:
                self.translator.load(f"{ALLSET.sbox_path}/scripts/python/projectPack/tr_en.pm")
            self.retranslateUi()
            self.tb_bz.toggle_language(ALLSET.language)
        except:
            hou.ui.displayMessage("Can't find language file")

    def retranslateUi(self):
        try:
            self.btn_refresh.setText(self.tr("Refresh"))
            self.btn_pack.setText(self.tr("Pack project"))
            self.btn_replace.setText(self.tr("Replace"))
            self.btn_pfolder.setText(self.tr("Project folder"))

            self.ui.cb_cacheNode.setText(self.tr("Cache node"))
            self.ui.cb_renderNode.setText(self.tr("Render node"))
            self.ui.cb_soloNonlocal.setText(self.tr("Solo non local"))
            self.ui.cb_soloError.setText(self.tr("Solo error"))
            self.ui.p_Path.setText(self.tr("Path:"))

            self.tb_goNode.setToolTip(self.tr("Go node"))
            self.tb_bigView.setToolTip(self.tr("Zoom view"))
            self.tb_folder.setToolTip(self.tr("Open file folder"))
            self.tb_ignore.setToolTip(self.tr("Toggle ignore"))
            self.tb_search.setToolTip(self.tr("Search and replace"))
            self.tb_flip.setToolTip(self.tr("Flip info"))

            self.ui2.tip_1.setText(self.tr("Categorized folder name"))
            self.ui2.tip_2.setText(self.tr("File formats separated by spaces, lowercase."))
            self.ui2.cb_1.setText(
                self.tr("Ignore Cache nodes that are not activated Load from Disk.")
            )
            self.ui2.cb_2.setText(self.tr("Ignore Bypass nodes."))
            self.ui2.cb_3.setText(self.tr("Ignore locked HDA nodes."))
            self.ui2.cb_4.setText(self.tr("Package all preview image files."))

            self.tb_set.setToolTip(self.tr("Settings"))
            self.tb_help.setToolTip(self.tr("Online document"))
            self.tb_language.setToolTip(self.tr("Toggle language"))

            self.tr_localization = self.tr("Local Path")
            self.tr_absolutePath = self.tr("Absolute Path")
            self.tr_customPath = self.tr("Custom Path")
            self.tr_replace = self.tr("Replace File")
            self.tr_goNode = self.tr("Go Node")
            self.tr_bigView = self.tr("Big View")
            self.tr_openInExplorer = self.tr("Open Folder")
            self.tr_toggleIgnore = self.tr("Toggle Ignore")
            self.tr_toggleUsdFolder = self.tr("USD Folder")
        except Exception as e:
            display_status(f"Snail_error_pp: retranslateUi _ {e}")


def main_show():
    try:
        houMainWindow = hou.qt.mainWindow()
        getChildWin = houMainWindow.findChild(QWidget, "Snail_PP")
        getChildWin.parent().close()
        getChildWin.parent().deleteLater()
    except:
        pass
    ALLSET.verify_sig("pp")
    mywin2 = PP_Win()
    mywin2.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    mywin2.show()


def callInterface():
    panel = None
    pane_name = "SnailBox_projectPack"

    ALLSET.verify_sig("pp")
    for pane in hou.ui.floatingPaneTabs():
        if pane.floatingPanel().name() == pane_name:

            ae_win = pane.activeInterfaceRootWidget()
            ae_win.refresh()
            panel = pane
    if not panel:
        panel = hou.ui.curDesktop().createFloatingPaneTab(
            hou.paneTabType.PythonPanel, (500, 500), (500, 650), pane_name
        )
    if panel:
        panel.showToolbar(0)
        panel.expandToolbar(0)
    if panel.floatingPanel():
        panel.floatingPanel().setName(pane_name)

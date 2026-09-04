import os
import hou
from utils import *
from .module import *
from .module import pp_item as ppp
import importlib

importlib.reload(ppp)


class PP_Win(QWidget):
    """项目打包主窗口 (薄协调层)

    职责：
        - 创建 AllFiles 与 Ui_Main
        - 打包、设置对话框、语言切换等重活
        - 窗口生命周期 (main_show / callInterface / closeEvent)
    所有 UI 布局、信号、刷新、交互都在 Ui_Main 中内聚完成。
    """

    def __init__(self):
        super().__init__()
        self.filesObj = None
        self.formatDir = {}

        self.translator = QtCore.QTranslator()
        QApplication.installTranslator(self.translator)

        # 数据
        self.filesObj = ppp.AllFiles(self)
        # UI (自包含布局+信号+刷新)
        self.ui = Ui_Main(self, self.filesObj)
        # 设置对话框
        self.ui2 = Ui_Dialog()

        self.setObjectName("Snail_PP")

        mainlayout = QVBoxLayout()
        mainlayout.setSpacing(0)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.addWidget(self.ui)
        self.setLayout(mainlayout)
        self.resize(760, 660)
        self.setWindowTitle("SnailBox Assets Manager")
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))

        self.load_language()
        self.ui.refresh()

    # ========================================================================
    # 语言
    # ========================================================================

    def toggle_language(self):  # 切换语言
        ALLSET.toggle_language()
        self.load_language()

    def load_language(self):  # 加载语言
        try:
            if ALLSET.language:
                self.translator.load(f"{ALLSET.sbox_path}/scripts/python/projectPack/tr_zh.qm")
            else:
                self.translator.load(f"{ALLSET.sbox_path}/scripts/python/projectPack/tr_en.qm")
            self.retranslateUi()
        except:
            hou.ui.displayMessage("Can't find language file")

    def retranslateUi(self):  # 重新翻译
        try:
            ui = self.ui
            ui.btn_refresh.setText(self.tr("Refresh"))
            ui.btn_pack.setText(self.tr("Pack project"))
            ui.btn_replace.setText(self.tr("Replace"))
            ui.btn_pfolder.setText(self.tr("Project folder"))

            ui.cb_cacheNode.setText(self.tr("Cache node"))
            ui.cb_renderNode.setText(self.tr("Render node"))
            ui.cb_soloNonlocal.setText(self.tr("Solo non local"))
            ui.cb_soloError.setText(self.tr("Solo error"))
            ui.p_Path.setText(self.tr("Path:"))
            # 标签宽度按翻译文本自适应（中文“项目路径:”较长，需加宽防截断）
            ui.p_Path.setFixedWidth(
                ui.p_Path.fontMetrics().horizontalAdvance(ui.p_Path.text()) + 14
            )

            ui.tb_goNode.setToolTip(self.tr("Go node"))
            ui.tb_bigView.setToolTip(self.tr("Zoom view"))
            ui.tb_folder.setToolTip(self.tr("Open file folder"))
            ui.tb_ignore.setToolTip(self.tr("Toggle ignore"))
            ui.tb_search.setToolTip(self.tr("Search and replace"))
            ui.tb_flip.setToolTip(self.tr("Flip info"))

            ui.tb_set.setToolTip(self.tr("Settings"))
            ui.tb_help.setToolTip(self.tr("Online document"))
            ui.tb_language.setToolTip(self.tr("Toggle language"))

            ui.tr_localization = self.tr("Local Path")
            ui.tr_absolutePath = self.tr("Absolute Path")
            ui.tr_customPath = self.tr("Custom Path")
            ui.tr_replace = self.tr("Replace File")
            ui.tr_goNode = self.tr("Go Node")
            ui.tr_bigView = self.tr("Big View")
            ui.tr_openInExplorer = self.tr("Open Folder")
            ui.tr_toggleIgnore = self.tr("Toggle Ignore")
            ui.tr_toggleUsdFolder = self.tr("USD Folder")

            ui.tb_bz.toggle_language(ALLSET.language)
        except Exception as e:
            display_status(f"Snail_error_pp0: retranslateUi _ {e}")

    # ========================================================================
    # 打包
    # ========================================================================

    def browse_path(self):  # 选择打包路径
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

    def pack_project(self):  # 打包文件
        if hou.hipFile.hasUnsavedChanges():
            msg = "打包之前是否保存工程?" if ALLSET.language else "Save the project before packing?"
            if hou.ui.displayMessage(msg, buttons=("Yes", "No")) == 0:
                hou.hipFile.save()
        try:
            packPath = self.browse_path()
            if not packPath:
                return
            indexs = self.ui.get_filter_ids()
            self.filesObj.packProject(indexs, PPSET.localSet, packPath)
        except Exception as e:
            display_status(f"Snail_error_pp0: packProject _ {e}")
            msg = "打包失败,回退工程" if ALLSET.language else "Pack failed, rollback"
            if hou.ui.displayMessage(msg, buttons=("Yes", "No")) == 0:
                hou.hipFile.load(hou.hipFile.name(), suppress_save_prompt=True)
        self.ui.refresh()

    # ========================================================================
    # 设置对话框
    # ========================================================================

    def open_settings(self):  # 打开设置对话框
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
            self.ui2.cb_5.setChecked(PPSET.packPreview)
        except Exception as e:
            display_status(f"Snail_error_pp0: openDialog _ {e}")
            if ALLSET.language:
                msg = "读取 conf/projectPack.json 配置文件失败"
            else:
                msg = "Failed to read conf/projectPack.json configuration file"
            hou.ui.displayMessage(msg)
        finally:
            self.ui2.show()

    def setFormatList(self):  # 保存格式设置
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
                display_status(f"Snail_error_pp0: setFormatList {e}")
        PPSET.formatDir = formatDir2
        PPSET.cacheDisk = self.ui2.cb_1.isChecked()
        PPSET.bypass = self.ui2.cb_2.isChecked()
        PPSET.lockedNode = self.ui2.cb_3.isChecked()
        PPSET.packThumb = self.ui2.cb_4.isChecked()
        PPSET.packPreview = self.ui2.cb_5.isChecked()

        PPSET.saveJson()
        self.ui.init_format_list()
        self.ui2.close()
        self.ui.refresh()

    # ========================================================================
    # 窗口生命周期
    # ========================================================================

    def closeEvent(self, event):
        sc_tab = hou.ui.findPaneTab("Snail_sc2")
        if sc_tab and sc_tab.qtParentWindow():
            sc_tab.qtParentWindow().close()
        view_node = hou.node("/obj/SnailBox_view")
        if view_node:
            view_node.destroy()
        super().closeEvent(event)


def main_show():
    # 单开模式：用 ALLSET 保存窗口引用。shelf 每次会 reload(main_pp)，
    # 模块级全局会被重置，而 ALLSET(utils.allSetting 单例) 不会被 reload，引用可持久。
    old = getattr(ALLSET, "_pp_win", None)
    if old is not None:
        try:
            old.close()
            old.deleteLater()
        except Exception:
            pass
    if not ALLSET.verify_sig("pp"):
        return
    win = PP_Win()
    win.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    win.show()
    ALLSET._pp_win = win


def callInterface():  # 调用界面
    panel = None
    pane_name = "SnailBox_projectPack"
    ALLSET.verify_sig("pp")
    for pane in hou.ui.floatingPaneTabs():
        if pane.floatingPanel().name() == pane_name:
            ae_win = pane.activeInterfaceRootWidget()
            ae_win.ui.refresh()
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

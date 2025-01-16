import hou
from .module import *


class Fb_win(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Snail_fb")
        self.sbox_path = hou.getenv("SnailBox")
        self.st = St(self)

        self.translator = QtCore.QTranslator()
        QApplication.installTranslator(self.translator)

        self.init_ui()
        self.init_data()

    def init_ui(self):
        self.setStyleSheet("*{background-color: rgb(35, 35, 39);}")
        self.mainlayout = QVBoxLayout()
        self.mainlayout.setSpacing(0)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainlayout)
        self.resize(560, 650)
        self.setWindowTitle("SnailBox Flipbook")
        self.setWindowIcon(QtGui.QIcon(self.sbox_path + "/file/SnailBox.svg"))

        self.lw_textItem = QListWidget(self)
        self.lw_textItem.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lw_textItem.setSpacing(4)
        self.lw_textItem.setStyleSheet(
            "QListWidget::Item{ border:2px solid rgb(25,25,25); border-radius: 5px;}"
            "QListWidget::Item:selected{background-color:rgb(35, 35, 39); border:1px solid rgb(255,163,32);}"
        )
        textItemlayout = QVBoxLayout()
        self.startlayout = QHBoxLayout()
        textItemlayout.addWidget(self.lw_textItem)
        self.mainlayout.addLayout(self.startlayout)
        self.mainlayout.addLayout(textItemlayout)

        self.start = Starter(self)
        self.startlayout.addWidget(self.start.ui)

        endlayout = QHBoxLayout()
        self.tb_bz = Snail_IconBtn_bz()
        self.tb_help = Snail_IconBtn_help()
        self.tb_language = Snail_IconBtn("snail_language", "Change language")
        self.bt_showText = Snail_Btn("Show Text")
        self.bt_out = Snail_Btn("Capture Sequence")
        self.tb_language.clicked.connect(self.toggle_language)
        self.bt_showText.clicked.connect(self.showText)
        self.bt_out.clicked.connect(self.capture_sequence)

        endlayout.addWidget(self.tb_bz)
        endlayout.addWidget(self.tb_help)
        endlayout.addWidget(self.tb_language)
        endlayout.addWidget(self.bt_showText)
        endlayout.addWidget(self.bt_out)
        self.mainlayout.addLayout(endlayout)

    def init_data(self):
        if self.st.textItems:
            self.refreh_textItem_uis()
        else:
            self.add_text()
        self.load_language()

    def refresh(self):
        self.start.refresh()
        self.retranslateUi()

    def refreh_textItem_uis(self):
        self.lw_textItem.clear()
        textItems = self.st.textItems
        if not textItems:
            return
        for one in textItems:
            o_ui = one.initUI()
            if not o_ui:
                continue
            self.textItem_bind(one)
            newItem = QListWidgetItem("")
            height = o_ui.sizeHint().height()
            size = QtCore.QSize(0, height)
            newItem.setSizeHint(size)
            self.lw_textItem.addItem(newItem)
            self.lw_textItem.setItemWidget(newItem, o_ui)
        if hasattr(self, "bt_out"):
            self.retranslateUi()
        self.showText()

    def change_preset(self, index=None):
        self.st.change_preset(index)

    def add_preset(self):
        self.st.new_preset()

    def del_preset(self):
        self.st.del_preset()

    def sel_path(self):
        self.start.sel_path()

    def open_folder(self):
        self.start.open_folder()

    def capture_frame(self):
        self.st.capture(0)

    def capture_sequence(self):
        self.st.capture(1)

    def capture_mp4(self):
        self.st.capture_mp4()

    def add_text(self):
        self.st.add_text()

    def showText(self):
        self.st.showText()

    def change_res_view(self):
        self.st.change_res_view()

    def change_res_cam(self):
        self.st.change_res_cam()

    def change_frame(self):
        self.st.change_frame()

    def current_item(func):
        def wrapper(self, *args, **kwargs):
            pos = self.lw_textItem.mapFromGlobal(QtGui.QCursor.pos())
            item = self.lw_textItem.itemAt(pos)
            if item:
                index = self.lw_textItem.row(item)
                self.lw_textItem.setCurrentRow(index)
            func(self, *args, **kwargs)

        return wrapper

    def path_change(self):
        self.start.path_change()

    def change_format(self):
        self.start.change_format()

    def res_change_x(self):
        self.start.res_change_x()

    def res_change_y(self):
        self.start.res_change_y()

    def frame_change_start(self):
        self.start.frame_change_start()

    def frame_change_end(self):
        self.start.frame_change_end()

    def frame_change_current(self):
        self.start.frame_change_current()

    def frame_change_rate(self):
        self.start.frame_change_rate()

    def toggle_preview(self, bool):
        self.st.preview = bool

    def del_textItem(self, textItems):
        self.st.remove_text(textItems)
        self.refreh_textItem_uis()

    def change_text(self, textItems):
        textItems.change_text()

    def change_textType(self, textItems):
        textItems.change_textType()

    def change_textSize(self, textItems):
        textItems.change_textSize()

    def change_textBold(self, textItems):
        textItems.change_textBold()

    def change_textItalic(self, textItems):
        textItems.change_textItalic()

    def change_numFill(self, textItems):
        textItems.change_numFill()

    def change_numPre(self, textItems):
        textItems.change_numPre()

    def change_numSuf(self, textItems):
        textItems.change_numSuf()

    def change_color(self, textItems):
        textItems.change_color()

    def change_relPos(self, textItems):
        textItems.change_relPos()

    def change_marginX(self, textItems):
        textItems.change_marginX()

    def change_marginY(self, textItems):
        textItems.change_marginY()

    def textItem_bind(self, one):
        one.line_a2.editingFinished.connect(lambda: self.change_text(one))

        one.combo_a3.currentIndexChanged.connect(lambda: self.change_textType(one))
        one.icon_close.clicked.connect(lambda: self.del_textItem(one))
        one.combo_b2.currentIndexChanged.connect(lambda: self.change_textSize(one))
        one.cb_b3.clicked.connect(lambda: self.change_textBold(one))
        one.cb_b4.clicked.connect(lambda: self.change_textItalic(one))
        one.cb_b5.clicked.connect(lambda: self.change_numFill(one))
        one.spinbox_b6.valueChanged.connect(lambda: self.change_numPre(one))
        one.spinbox_b7.valueChanged.connect(lambda: self.change_numSuf(one))
        one.combo_c2.currentIndexChanged.connect(lambda: self.change_relPos(one))
        one.spinbox_c3.valueChanged.connect(lambda: self.change_marginX(one))
        one.spinbox_c4.valueChanged.connect(lambda: self.change_marginY(one))
        one.bt_c5.clicked.connect(lambda: self.change_color(one))

    def toggle_language(self):
        ALLSET.toggle_language()
        self.load_language()

    def load_language(self):
        try:
            if ALLSET.language:
                self.translator.load(f"{self.sbox_path}/scripts/python/flipbook/tr_zh.pm")
            else:
                self.translator.load(f"{self.sbox_path}/scripts/python/flipbook/tr_en.pm")
            self.retranslateUi()
            self.tb_bz.toggle_language(ALLSET.language)
        except:
            hou.ui.displayMessage("Can't find language file")

    def retranslateUi(self):
        self.bt_out.setText(self.tr("Capture Sequence"))
        self.bt_showText.setText(self.tr("Show Text"))
        self.start.label_a.setText(self.tr("File path"))
        self.start.label_b.setText(self.tr("Image res"))
        self.start.label_c.setText(self.tr("F range"))
        self.start.label_c2.setText(self.tr("F rate"))
        self.start.icon_add.setToolTip(self.tr("Add text"))
        self.start.icon_pic.setToolTip(self.tr("Capture frame"))
        self.start.icon_pics.setToolTip(self.tr("Capture sequence"))
        self.start.icon_mp4.setToolTip(self.tr("Capture mp4"))
        self.start.icon_view.setToolTip(self.tr("Set resolution with viewer"))
        self.start.icon_cam.setToolTip(self.tr("Set resolution with camera"))
        self.start.icon_reload.setToolTip(self.tr("Refresh animation setting"))
        self.start.icon_selPath.setToolTip(self.tr("Select save path"))
        self.start.icon_openFolder.setToolTip(self.tr("Open save folder"))
        self.start.icon_presetAdd.setToolTip(self.tr("Add preset"))
        self.start.icon_presetDel.setToolTip(self.tr("Delete preset"))

        self.tb_help.setToolTip(self.tr("Online documents"))
        self.tb_language.setToolTip(self.tr("Change language"))

        for one in self.st.textItems:
            one.label_a1.setText(self.tr("Text cont"))
            one.label_b1.setText(self.tr("Text size"))
            one.cb_b3.setText(self.tr("Bold"))
            one.cb_b4.setText(self.tr("Italic"))
            one.cb_b5.setText(self.tr("Digit"))
            one.label_c1.setText(self.tr("Align pos"))

    def closeEvent(self, event):
        self.st.save_preset_close()
        super().closeEvent(event)


def main_show():
    try:
        houMainWindow = hou.qt.mainWindow()
        getChildWin = houMainWindow.findChild(QWidget, "Snail_fb")
        getChildWin.close()
        getChildWin.deleteLater()
    except:
        pass

    if not ALLSET.verify_sig("fb"):
        return
    mywin2 = Fb_win()
    mywin2.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    mywin2.show()


def callInterface():
    panel = None
    pane_name = "SnailBox_Fb"
    if not ALLSET.verify_sig("fb"):
        return
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
    try:
        panel.floatingPanel().qtParentWindow().showNormal()
    except:
        pass

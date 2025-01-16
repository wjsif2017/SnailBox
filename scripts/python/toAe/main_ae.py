import hou
from .module import *


class Ae_win(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Snail_toAe")
        self.sbox_path = hou.getenv("SnailBox")
        self.aec = Aec(self)
        self.start = Starter(self)
        self.translator = QtCore.QTranslator()
        QApplication.installTranslator(self.translator)
        self.init_ui()
        self.load_language()

    def init_ui(self):
        self.setStyleSheet("*{background-color: rgb(35, 35, 39);}")
        self.mainlayout = QVBoxLayout()
        self.mainlayout.setSpacing(0)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainlayout)
        self.resize(550, 650)
        self.setWindowTitle("SnailBox Ae Bridge")
        self.setWindowIcon(QtGui.QIcon(self.sbox_path + "/file/SnailBox.svg"))

        self.lw_outer = QListWidget(self)
        self.lw_outer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lw_outer.setSpacing(4)
        self.lw_outer.setStyleSheet(
            "QListWidget::Item{ border:2px solid rgb(25,25,25); border-radius: 5px;}"
            "QListWidget::Item:selected{background-color:rgb(35, 35, 39); border:1px solid rgb(255,163,32);}"
        )
        outerlayout = QVBoxLayout()
        self.startlayout = QHBoxLayout()

        self.startlayout.addWidget(self.start.ui)
        outerlayout.addWidget(self.lw_outer)
        self.mainlayout.addLayout(self.startlayout)
        self.mainlayout.addLayout(outerlayout)

        endlayout = QHBoxLayout()
        self.tb_bz = Snail_IconBtn_bz()
        self.tb_help = Snail_IconBtn_help()
        self.tb_language = Snail_IconBtn("snail_language", "Change language")
        self.tb_language.clicked.connect(self.toggle_language)
        self.bt_refresh = Snail_Btn("Refresh")
        self.bt_export = Snail_Btn("Export AEC")
        self.bt_toAe = Snail_Btn("To Ae ")
        self.bt_refresh.clicked.connect(self.refresh)
        self.bt_export.clicked.connect(self.output_file)
        self.bt_toAe.clicked.connect(self.out_toAe)
        endlayout.addWidget(self.tb_bz)
        endlayout.addWidget(self.tb_help)
        endlayout.addWidget(self.tb_language)
        endlayout.addWidget(self.bt_refresh)
        endlayout.addWidget(self.bt_export)
        endlayout.addWidget(self.bt_toAe)
        self.mainlayout.addLayout(endlayout)
        self.refreh_outer_uis()

    def refreh_outer_uis(self):
        self.lw_outer.clear()
        outers = self.aec.outers
        if not outers:
            return
        for one in outers:
            o_ui = one.initUI()
            if not o_ui:
                continue
            self.outer_bind(one)
            newItem = QListWidgetItem("")
            newItem.setSizeHint(o_ui.sizeHint())
            self.lw_outer.addItem(newItem)
            self.lw_outer.setItemWidget(newItem, o_ui)
        self.retranslateUi()

    def refresh(self):
        self.aec.refreh_outers()
        self.aec.refreh_starter()
        self.start.refresh()
        self.refreh_outer_uis()

    def output_file(self):
        self.aec.output_file()

    def out_toAe(self):
        self.aec.out_toAe()

    def name_change(self):
        self.start.name_change()

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

    def toggle_all_animate(self, bool):
        self.aec.toggle_all_animate(bool)

    def toggle_preview(self, bool):
        self.aec.preview = bool

    def current_item(func):
        def wrapper(self, *args, **kwargs):
            pos = self.lw_outer.mapFromGlobal(QtGui.QCursor.pos())
            item = self.lw_outer.itemAt(pos)
            if item:
                index = self.lw_outer.row(item)
                self.lw_outer.setCurrentRow(index)
            func(self, *args, **kwargs)

        return wrapper

    def del_outer(self, outer):
        if outer in self.aec.outers:
            self.aec.outers.remove(outer)
            self.refreh_outer_uis()

    def toggle_animate(self, outer):
        outer.toggle_animate(bool)

    def toggle_null(self, outer):
        outer.toggle_null()

    def rec_change_x(self, outer):
        outer.rec_change_x()

    def rec_change_y(self, outer):
        outer.rec_change_y()

    def change_anchor(self, outer):
        outer.change_anchor()

    def change_color(self, outer):
        outer.change_color()

    def toggle_lightType(self, outer, option):
        outer.toggle_lightType(option)

    def outer_bind(self, one):
        one.icon_close.clicked.connect(lambda: self.del_outer(one))
        one.cb_static.toggled.connect(lambda: self.toggle_animate(one))
        if one.type == "null":
            one.cb_null.toggled.connect(lambda: self.toggle_null(one))
            one.bt_color.clicked.connect(lambda: self.change_color(one))
            one.spin_sx.valueChanged.connect(lambda: self.rec_change_x(one))
            one.spin_sy.valueChanged.connect(lambda: self.rec_change_y(one))
            one.combo_anchor.currentIndexChanged.connect(lambda: self.change_anchor(one))
        elif one.type == "light":
            one.ra_c1.clicked.connect(lambda: self.toggle_lightType(one, "OMNI"))
            one.ra_c2.clicked.connect(lambda: self.toggle_lightType(one, "SPOT"))
            one.ra_c3.clicked.connect(lambda: self.toggle_lightType(one, "PAR"))
        else:
            pass

    def toggle_language(self):
        ALLSET.toggle_language()
        self.load_language()

    def load_language(self):
        try:
            if ALLSET.language:
                self.translator.load(f"{self.sbox_path}/scripts/python/toAe/tr_zh.pm")
            else:
                self.translator.load(f"{self.sbox_path}/scripts/python/toAe/tr_en.pm")
            self.retranslateUi()
        except:
            hou.ui.displayMessage("Can't find language file")

    def retranslateUi(self):
        self.bt_refresh.setText(self.tr("Refresh"))
        self.bt_export.setText(self.tr("Export AEC"))
        self.bt_toAe.setText(self.tr("To Ae"))
        self.start.label_a.setText(self.tr("C name"))
        self.start.label_b.setText(self.tr("C size"))
        self.start.label_c.setText(self.tr("F range"))
        self.start.label_d.setText(self.tr("F rate"))
        self.start.label_e.setText(self.tr("Frame"))
        self.start.cb_d1.setText(self.tr("Export Flipbook"))
        self.start.cb_e1.setText(self.tr("Toggle Static"))
        self.start.label_adder.setText(self.tr("Drag node here"))

        self.tb_bz.setToolTip(self.tr("Bilibili"))
        self.tb_help.setToolTip(self.tr("Online documents"))
        self.tb_language.setToolTip(self.tr("Change language"))

        for one in self.aec.outers:
            one.label_b3.setText(self.tr("Options"))
            one.cb_static.setText(self.tr("Static"))
            if one.type == "light":
                one.ra_c1.setText(self.tr("Point"))
                one.ra_c2.setText(self.tr("Spot"))
                one.ra_c3.setText(self.tr("Parallel"))
            elif one.type == "null":
                one.cb_null.setText(self.tr("Null Object"))
                one.label_color.setText(self.tr("Solid color"))
                one.label_d1.setText(self.tr("Solid size"))
                one.label_anchor.setText(self.tr("Anchor point"))

    def closeEvent(self, event):
        self.aec.save_preset()
        super().closeEvent(event)


def main_show():
    try:
        houMainWindow = hou.qt.mainWindow()
        getChildWin = houMainWindow.findChild(QWidget, "SnailBox AeBridge")
        getChildWin.close()
        getChildWin.deleteLater()
    except:
        pass
    if not ALLSET.verify_sig("ae"):
        return
    mywin2 = Ae_win()
    mywin2.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    mywin2.show()


def callInterface():
    panel = None
    pane_name = "SnailBox_AeBridge"
    for pane in hou.ui.floatingPaneTabs():
        if pane.floatingPanel().name() == pane_name:
            ae_win = pane.activeInterfaceRootWidget()
            ae_win.refresh()
            panel = pane
    if not ALLSET.verify_sig("ae"):
        return
    if not panel:
        panel = hou.ui.curDesktop().createFloatingPaneTab(
            hou.paneTabType.PythonPanel, (500, 500), (550, 650), pane_name
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

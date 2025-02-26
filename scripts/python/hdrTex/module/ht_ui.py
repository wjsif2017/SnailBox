from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from utils import *
from .ht_set import MYSET


class Ui_Snail_HT(QWidget):
    def setupUi(self, Snail_HT):
        if not Snail_HT.objectName():
            Snail_HT.setObjectName("Snail_HT")
        Snail_HT.setWindowModality(Qt.NonModal)
        Snail_HT.resize(780, 602)
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Snail_HT.setFont(font)
        Snail_HT.setWindowTitle("Form")
        # if QT_CONFIG(tooltip)
        Snail_HT.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        Snail_HT.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        Snail_HT.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        Snail_HT.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        Snail_HT.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        Snail_HT.setAutoFillBackground(False)
        Snail_HT.setStyleSheet(
            "*{\n"
            "	background-color: rgb(35, 35, 39);\n"
            "}\n"
            "*:hover {	\n"
            "	color: rgb(255, 191, 0);\n"
            "}\n"
            "QSplitter{\n"
            "background-color: rgb(35, 35, 39);\n"
            "	color: rgb(255, 85, 0);\n"
            "}"
        )
        Snail_HT.setWindowFilePath("")
        self.horizontalLayout_4 = QHBoxLayout(Snail_HT)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QFrame(Snail_HT)
        self.leftmenu.setObjectName("leftmenu")
        self.leftmenu.setMaximumSize(QSize(70, 16777215))
        self.leftmenu.setStyleSheet("border:0;\n" "background-color: #2d2d2d;")
        self.leftmenu.setFrameShape(QFrame.StyledPanel)
        self.leftmenu.setFrameShadow(QFrame.Raised)
        self.leftMenu = QVBoxLayout(self.leftmenu)
        self.leftMenu.setSpacing(5)
        self.leftMenu.setObjectName("leftMenu")
        self.leftMenu.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.leftMenu.addItem(self.verticalSpacer_2)

        self.lw_menu1 = QListWidget(self.leftmenu)
        self.lw_menu1.setObjectName("lw_menu1")
        font1 = QFont()
        font1.setFamily("Microsoft YaHei UI")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.lw_menu1.setFont(font1)
        self.lw_menu1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lw_menu1.setStyleSheet("")
        self.lw_menu1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lw_menu1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lw_menu1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.lw_menu1.setAutoScroll(False)
        self.lw_menu1.setAutoScrollMargin(0)
        self.lw_menu1.setDragEnabled(False)
        self.lw_menu1.setDragDropOverwriteMode(False)
        self.lw_menu1.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.lw_menu1.setDefaultDropAction(Qt.IgnoreAction)
        self.lw_menu1.setSelectionMode(QAbstractItemView.SingleSelection)
        self.lw_menu1.setTextElideMode(Qt.ElideMiddle)
        self.lw_menu1.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.lw_menu1.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.lw_menu1.setMovement(QListView.Static)
        self.lw_menu1.setFlow(QListView.TopToBottom)
        self.lw_menu1.setProperty("isWrapping", False)
        self.lw_menu1.setResizeMode(QListView.Adjust)
        self.lw_menu1.setSpacing(0)
        self.lw_menu1.setViewMode(QListView.IconMode)
        self.lw_menu1.setModelColumn(0)
        self.lw_menu1.setItemAlignment(Qt.AlignCenter)

        self.leftMenu.addWidget(self.lw_menu1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.leftMenu.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4.addWidget(self.leftmenu)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.hl_top = QHBoxLayout()
        self.hl_top.setObjectName("hl_top")
        self.hl_top.setContentsMargins(-1, 0, -1, -1)

        self.verticalLayout_17.addLayout(self.hl_top)

        self.hl_2 = QHBoxLayout()
        self.hl_2.setObjectName("hl_2")
        self.hl_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.hl_2.setContentsMargins(0, 0, -1, -1)

        self.verticalLayout_17.addLayout(self.hl_2)

        self.splitter_h = QSplitter(Snail_HT)
        self.splitter_h.setObjectName("splitter_h")
        self.splitter_h.setMinimumSize(QSize(0, 30))
        self.splitter_h.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget_2 = QWidget(self.splitter_h)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.splitter_v = QSplitter(self.verticalLayoutWidget_2)
        self.splitter_v.setObjectName("splitter_v")
        self.splitter_v.setStyleSheet("QListWidget {background-color: rgba(0,0,0,0);}")
        self.splitter_v.setOrientation(Qt.Vertical)
        self.verticalLayoutWidget_3 = QWidget(self.splitter_v)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.lw_view = QListWidget(self.verticalLayoutWidget_3)
        self.lw_view.setObjectName("lw_view")
        self.lw_view.setStyleSheet(
            "QListWidget::item:selected {\n" "    background-color: #ffa320;\n" "}"
        )
        self.lw_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.lw_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lw_view.setProperty("isWrapping", True)
        self.lw_view.setResizeMode(QListView.Adjust)
        self.lw_view.setSpacing(4)
        self.lw_view.setViewMode(QListView.IconMode)

        self.verticalLayout.addWidget(self.lw_view)

        self.pb_progress = QProgressBar(self.verticalLayoutWidget_3)
        self.pb_progress.setObjectName("pb_progress")
        self.pb_progress.setMaximumSize(QSize(16777215, 10))
        font2 = QFont()
        font2.setFamily("Microsoft YaHei UI")
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.pb_progress.setFont(font2)
        self.pb_progress.setAutoFillBackground(False)
        self.pb_progress.setStyleSheet(
            "QProgressBar {\n"
            "        border: 1px solid grey;\n"
            "        text-align: center;\n"
            "    }\n"
            "    QProgressBar::chunk {\n"
            "        background-color: #ffa320;\n"
            "        width: 2px;\n"
            "    }"
        )
        self.pb_progress.setMinimum(0)
        self.pb_progress.setMaximum(100)
        self.pb_progress.setValue(0)
        self.pb_progress.setTextVisible(False)
        self.pb_progress.setOrientation(Qt.Horizontal)
        self.pb_progress.setInvertedAppearance(False)
        self.pb_progress.setTextDirection(QProgressBar.TopToBottom)
        self.pb_progress.setFormat("")

        self.verticalLayout.addWidget(self.pb_progress)

        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.splitter_v.addWidget(self.verticalLayoutWidget_3)
        self.verticalLayoutWidget_4 = QWidget(self.splitter_v)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.layout_v = QVBoxLayout()
        self.layout_v.setObjectName("layout_v")
        self.layout_v.setContentsMargins(-1, 0, -1, -1)
        self.splitter = QSplitter(self.verticalLayoutWidget_4)
        self.splitter.setObjectName("splitter")
        self.splitter.setMinimumSize(QSize(0, 0))
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(True)
        self.gb_info = QGroupBox(self.splitter)
        self.gb_info.setObjectName("gb_info")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_info.sizePolicy().hasHeightForWidth())
        self.gb_info.setSizePolicy(sizePolicy)
        self.gb_info.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily("Microsoft YaHei UI")
        self.gb_info.setFont(font3)
        self.gb_info.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.gb_info.setTitle("Info")
        self.horizontalLayout_13 = QHBoxLayout(self.gb_info)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 6, 2, 2)
        self.scrollArea_3 = QScrollArea(self.gb_info)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollArea_3.setStyleSheet("border: none;")
        self.scrollArea_3.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.w_info = QWidget()
        self.w_info.setObjectName("w_info")
        self.w_info.setGeometry(QRect(0, 0, 334, 148))
        self.w_info.setStyleSheet("")
        self.verticalLayout_6 = QVBoxLayout(self.w_info)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.layout_info = QVBoxLayout()
        self.layout_info.setSpacing(4)
        self.layout_info.setObjectName("layout_info")
        self.layout_info.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addLayout(self.layout_info)

        self.scrollArea_3.setWidget(self.w_info)

        self.horizontalLayout_13.addWidget(self.scrollArea_3)

        self.splitter.addWidget(self.gb_info)
        self.gb_asset = QGroupBox(self.splitter)
        self.gb_asset.setObjectName("gb_asset")
        sizePolicy.setHeightForWidth(self.gb_asset.sizePolicy().hasHeightForWidth())
        self.gb_asset.setSizePolicy(sizePolicy)
        self.gb_asset.setMinimumSize(QSize(0, 0))
        self.gb_asset.setFont(font3)
        self.gb_asset.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.gb_asset.setTitle("Assets")
        self.horizontalLayout_14 = QHBoxLayout(self.gb_asset)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 6, 2, 2)
        self.scrollArea_4 = QScrollArea(self.gb_asset)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollArea_4.setStyleSheet("border: none;;")
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.w_asset = QWidget()
        self.w_asset.setObjectName("w_asset")
        self.w_asset.setGeometry(QRect(0, 0, 333, 148))
        self.w_asset.setAutoFillBackground(False)
        self.w_asset.setStyleSheet("")
        self.verticalLayout_12 = QVBoxLayout(self.w_asset)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.layout_asset = QVBoxLayout()
        self.layout_asset.setObjectName("layout_asset")

        self.verticalLayout_12.addLayout(self.layout_asset)

        self.scrollArea_4.setWidget(self.w_asset)

        self.horizontalLayout_14.addWidget(self.scrollArea_4)

        self.splitter.addWidget(self.gb_asset)

        self.layout_v.addWidget(self.splitter)

        self.verticalLayout_8.addLayout(self.layout_v)

        self.splitter_v.addWidget(self.verticalLayoutWidget_4)

        self.verticalLayout_5.addWidget(self.splitter_v)

        self.splitter_h.addWidget(self.verticalLayoutWidget_2)
        self.horizontalLayoutWidget_2 = QWidget(self.splitter_h)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layout_h = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_h.setSpacing(0)
        self.layout_h.setObjectName("layout_h")
        self.layout_h.setContentsMargins(0, 0, 0, 0)
        self.splitter_h.addWidget(self.horizontalLayoutWidget_2)

        self.verticalLayout_17.addWidget(self.splitter_h)

        self.layout_bottom = QHBoxLayout()
        self.layout_bottom.setObjectName("layout_bottom")
        self.layout_bottom.setSizeConstraint(QLayout.SetMinimumSize)
        self.layout_bottom.setContentsMargins(5, 0, 5, 0)

        self.verticalLayout_17.addLayout(self.layout_bottom)

        self.verticalLayout_17.setStretch(2, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_17)

        self.lw_menu1.setCurrentRow(-1)

        QMetaObject.connectSlotsByName(Snail_HT)


class Ui_Dialog_other(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pa = parent
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        self.setWindowTitle("SnailBox Add Custom Lib")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.init_ui()
        self.setModal(True)

    def init_ui(self):
        layout_41 = QHBoxLayout()
        self.lb_filter1 = Snail_LabelA("Prefix Filter", width=100)
        self.le_filter1 = Snail_LineEdit(tip="sm_ (Exclude sm_xxx.exr files)")
        self.lb_filter2 = Snail_LabelA("Suffix Filter", width=100)
        self.le_filter2 = Snail_LineEdit(tip="_sm (Exclude xxx_sm.exr files)")

        layout_41.addWidget(self.lb_filter1)
        layout_41.addWidget(self.le_filter1)
        layout_41.addWidget(self.lb_filter2)
        layout_41.addWidget(self.le_filter2)

        layout_42 = QHBoxLayout()
        self.lb_filter3 = Snail_LabelA("Folder Filter", width=100)
        self.le_filter3 = Snail_LineEdit(
            tip="folder_1, folder_2 (Exclude folder_1 folder_2, separate with ' , ')"
        )
        layout_42.addWidget(self.lb_filter3)
        layout_42.addWidget(self.le_filter3)

        layout_43 = QHBoxLayout()
        self.lb_format = Snail_LabelA("Format Filter", width=100)
        self.cb_exr = Snail_CheckBox("exr")
        self.cb_hdr = Snail_CheckBox("hdr")
        self.cb_tif = Snail_CheckBox("tif")
        self.cb_png = Snail_CheckBox("png")
        self.cb_jpg = Snail_CheckBox("jpg")
        self.le_otherFormat = Snail_LineEdit(tip="other format")
        self.le_otherFormat.setFixedWidth(100)
        layout_43.addWidget(self.lb_format)
        layout_43.addWidget(self.cb_exr)
        layout_43.addWidget(self.cb_hdr)
        layout_43.addWidget(self.cb_tif)
        layout_43.addWidget(self.cb_png)
        layout_43.addWidget(self.cb_jpg)
        layout_43.addWidget(self.le_otherFormat)

        layout_44 = QHBoxLayout()
        self.lb_size = Snail_LabelA("Size Filter", width=100)
        self.sb_size = Snail_SpinBox(suf="Kb", min=0, width=100)
        self.sb_size.setValue(30)
        self.lb_sizeTip = Snail_LabelTip("Exclude files smaller than the set size", 10)
        layout_44.addWidget(self.lb_size)
        layout_44.addWidget(self.sb_size)
        layout_44.addWidget(self.lb_sizeTip)

        layout_45 = QHBoxLayout()
        self.lb_group = Snail_LabelA("Group Level", width=100)
        self.rb_group1 = Snail_RadioButton("1")
        self.rb_group1.setChecked(True)
        self.rb_group2 = Snail_RadioButton("2")
        self.rb_group3 = Snail_RadioButton("3")
        self.lb_groupTip = Snail_LabelTip("D:/xx/3/2/1/xxx.exr Group with folder hierarchy", 10)
        layout_45.addWidget(self.lb_group)
        layout_45.addWidget(self.rb_group1)
        layout_45.addWidget(self.rb_group2)
        layout_45.addWidget(self.rb_group3)
        layout_45.addWidget(self.lb_groupTip)

        layout_46 = QHBoxLayout()
        self.btn_cancel = Snail_Btn("Cancel")
        self.btn_cancel.clicked.connect(self.close)
        self.btn_ok = Snail_Btn("OK")
        self.btn_ok.clicked.connect(self.pa.get_dialog_dict)
        layout_46.addWidget(self.btn_cancel)
        layout_46.addWidget(self.btn_ok)

        layout_main4 = QVBoxLayout()
        layout_main4.addLayout(layout_41)
        layout_main4.addLayout(layout_42)
        layout_main4.addLayout(layout_43)
        layout_main4.addLayout(layout_44)
        layout_main4.addLayout(layout_45)
        layout_main4.addLayout(layout_46)
        self.setLayout(layout_main4)


class Ui_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pa = parent
        # self.translator = QtCore.QTranslator()
        # QApplication.installTranslator(self.pa.translator)
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        self.setWindowTitle("SnailBox Texture Browser Settings")
        self.setStyleSheet(
            "*{background-color: rgb(35, 35, 39);}" "*:hover{color: rgb(255, 191, 0);}"
        )
        self.resize(640, 560)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        # self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.dialog = Ui_Dialog_other(self)

        self.init_ui()

    def init_ui(self):
        layout_main = QVBoxLayout()
        self.stw = QTabWidget(self)
        self.stw.setStyleSheet(
            "QTabBar::tab:selected {color: rgb(255,163,32);}"
            "QTabBar {font-family: Microsoft YaHei UI; font-size: 14px;}"
        )
        layout_main.addWidget(self.stw)
        line = Snail_line()
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)

        # region tab0
        layout_01 = QVBoxLayout()
        self.cb_rename01 = Snail_CheckBox("Node rename for set texture")
        self.cb_rename02 = Snail_CheckBox("Node rename for add preset texture node")
        self.cb_nodebg = Snail_CheckBox("Set node background for set texture")
        self.cb_rename01.toggled.connect(self.toggle_rename01)
        self.cb_rename02.toggled.connect(self.toggle_rename02)
        self.cb_nodebg.toggled.connect(self.toggle_setBg)
        layout_01.addWidget(self.cb_rename01)
        layout_01.addWidget(self.cb_rename02)
        layout_01.addWidget(self.cb_nodebg)

        layout_main0 = QVBoxLayout()
        layout_main0.addLayout(layout_01)
        layout_main0.addItem(spacer)
        self.s_tab_0 = QWidget()
        self.s_tab_0.setEnabled(True)
        self.s_tab_0.setLayout(layout_main0)
        self.stw.addTab(self.s_tab_0, "")
        self.stw.setTabText(self.stw.indexOf(self.s_tab_0), "Options")
        # endregion

        # region tab1
        layout_11 = QVBoxLayout()
        self.stw_libList = Snail_Table(self)
        self.stw_libList.setColumnCount(2)
        self.stw_libList.itemClicked.connect(self.refresh_lib_set)

        layout_11.addWidget(self.stw_libList)
        layout_12 = QHBoxLayout()
        self.scb_lib_type = Snail_ComboBox()
        self.scb_lib_type.activated.connect(self.refresh_lib_tips)
        # self.scb_lib_type.currentIndexChanged.connect(self.refresh_lib_tips)
        self.scb_index = Snail_ComboBox()
        self.scb_icon = Snail_ComboBox()
        self.sle_libName = Snail_LineEdit(tip="Library name")
        layout_12.addWidget(self.scb_lib_type)
        layout_12.addWidget(self.scb_index)
        layout_12.addWidget(self.scb_icon)
        layout_12.addWidget(self.sle_libName)
        layout_12.setStretch(0, 2)
        layout_12.setStretch(1, 1)
        layout_12.setStretch(2, 1)
        layout_12.setStretch(3, 1)

        layout_13 = QHBoxLayout()
        self.sle_libPath = Snail_LineEdit(tip="Library path")
        self.sb_selPath = Snail_IconBtn("BUTTONS_chooser_folder", "Select lib path")
        self.sb_selPath.clicked.connect(self.sel_lib_floder)
        layout_13.addWidget(self.sle_libPath)
        layout_13.addWidget(self.sb_selPath)
        layout_13.setStretch(0, 1)

        layout_14 = QHBoxLayout()
        self.sb_libDel = Snail_Btn("Delete")
        self.sb_libMod = Snail_Btn("Modify")
        self.sb_libRescan = Snail_Btn("Update")
        self.sr_libAutoUpdate = Snail_CheckBox("Auto Update")
        self.sb_libAdd = Snail_Btn("Add")
        self.sb_libAdd.clicked.connect(self.add_lib)
        self.sb_libDel.clicked.connect(self.del_lib)
        self.sb_libMod.clicked.connect(self.mod_lib)
        self.sb_libRescan.clicked.connect(self.rescan_lib)
        self.sr_libAutoUpdate.clicked.connect(self.toggle_autoUpdate)
        layout_14.addWidget(self.sb_libDel)
        layout_14.addWidget(self.sb_libMod)
        layout_14.addWidget(self.sb_libRescan)
        layout_14.addWidget(self.sr_libAutoUpdate)
        layout_14.addWidget(self.sb_libAdd)

        layout_15 = QHBoxLayout()
        self.t_tips = Snail_TextBrowser(self)
        self.t_tips.setFixedHeight(100)

        layout_15.addWidget(self.t_tips)

        layout_main1 = QVBoxLayout()
        layout_main1.addLayout(layout_11)
        layout_main1.addLayout(layout_12)
        layout_main1.addLayout(layout_13)
        layout_main1.addLayout(layout_14)
        layout_main1.addLayout(layout_15)
        layout_main1.setStretch(0, 1)
        self.s_tab_1 = QWidget()
        self.s_tab_1.setEnabled(True)
        self.s_tab_1.setLayout(layout_main1)
        self.stw.addTab(self.s_tab_1, "")
        self.stw.setTabText(self.stw.indexOf(self.s_tab_1), "Add Library")
        # endregion

        # region tab2
        layout_21 = QVBoxLayout()
        self.slw_node_preset = Snail_List(self)
        layout_21.addWidget(self.slw_node_preset)

        layout_22 = QHBoxLayout()
        self.sb_del_node_preset = Snail_Btn("Delete")
        self.sb_del_node_preset.clicked.connect(self.del_node_preset)
        self.lb_add_node_preset = Snail_DropLabel(
            "Drag and drop parameter here to Add", fun=self.add_preset
        )
        self.sb_del_node_preset.setFixedHeight(50)
        self.lb_add_node_preset.setFixedHeight(50)
        layout_22.addWidget(self.sb_del_node_preset)
        layout_22.addWidget(self.lb_add_node_preset)
        layout_22.setStretch(0, 1)
        layout_22.setStretch(1, 2)

        layout_23 = QHBoxLayout()
        self.t_tips2 = Snail_TextBrowser(self)
        self.t_tips2.setFixedHeight(100)
        tips2 = [
            "* 节点预设: 点击创建纹理节点按钮,选择预设,自动添加相应的节点并设置纹理参数",
            "* 添加预设: 拖拽节点参数到添加按钮上,不是拖拽节点",
            "* 删除预设: 选择预设列表一项,点击删除按钮即可删除",
        ]
        self.t_tips2.update_tips(tips2)
        layout_23.addWidget(self.t_tips2)

        layout_main2 = QVBoxLayout()
        layout_main2.addLayout(layout_21)
        layout_main2.addLayout(layout_22)
        layout_main2.addLayout(layout_23)
        self.s_tab_2 = QWidget()
        self.s_tab_2.setEnabled(True)
        self.s_tab_2.setLayout(layout_main2)
        self.stw.addTab(self.s_tab_2, "")
        self.stw.setTabText(self.stw.indexOf(self.s_tab_2), "Add Preset")
        # endregion

        # region tab3
        layout_31 = QVBoxLayout()
        self.slw_other_parm = Snail_List(self)
        layout_31.addWidget(self.slw_other_parm)

        layout_32 = QHBoxLayout()
        self.sb_del_other_parm = Snail_Btn("Delete")
        self.sb_del_other_parm.clicked.connect(self.del_other_parm)
        self.lb_add_other_parm = Snail_DropLabel(
            "Drag and drop parameter here to Add", fun=self.add_other_parm
        )
        self.sb_del_other_parm.setFixedHeight(50)
        self.lb_add_other_parm.setFixedHeight(50)
        layout_32.addWidget(self.sb_del_other_parm)
        layout_32.addWidget(self.lb_add_other_parm)
        layout_32.setStretch(0, 1)
        layout_32.setStretch(1, 2)

        layout_33 = QHBoxLayout()
        self.t_tips3 = Snail_TextBrowser(self)
        self.t_tips3.setFixedHeight(100)
        layout_33.addWidget(self.t_tips3)

        layout_main3 = QVBoxLayout()
        layout_main3.addLayout(layout_31)
        layout_main3.addLayout(layout_32)
        layout_main3.addLayout(layout_33)
        self.s_tab_3 = QWidget()
        self.s_tab_3.setEnabled(True)
        self.s_tab_3.setLayout(layout_main3)
        self.stw.addTab(self.s_tab_3, "")
        self.stw.setTabText(self.stw.indexOf(self.s_tab_3), "Custom Node")
        # endregion

        self.setLayout(layout_main)

    def init_set(self):  # 初始化界面
        self.refresh_option()
        self.refresh_node_preset()
        self.refresh_other_parm()
        self.refresh_table_libList()
        self.refresh_add_cb()
        self.refresh_index_cb()
        self.refresh_lib_tips(-1)
        self.refresh_other_tips()
        self.load_language()

    def refresh_option(self):  # 刷新设置选项
        self.cb_rename01.setChecked(MYSET.rename01)
        self.cb_rename02.setChecked(MYSET.rename02)
        self.cb_nodebg.setChecked(MYSET.setBg)

    def refresh_node_preset(self):  # 刷新一键创建节点列表
        self.slw_node_preset.clear()
        for key, one in MYSET.option_nodes.items():
            one_item = f"{key} > {one[0]} > {one[1]}"
            self.slw_node_preset.addItem(one_item)

    def refresh_other_parm(self):  # 刷新自定义节点参数
        self.slw_other_parm.clear()
        for node, parm in MYSET.node_parm_list.items():
            one_item = f"{node} > {parm}"
            self.slw_other_parm.addItem(one_item)

    def refresh_table_libList(self):  # 刷新库列表
        self.stw_libList.clearContents()  # 清理表格内容
        self.stw_libList.setRowCount(len(MYSET.lib_list))
        for index, lib in enumerate(MYSET.lib_list):
            name = lib["name"]
            path = lib["path"]
            if not path:
                continue
            self.stw_libList.setItem(index, 0, QTableWidgetItem(name))
            self.stw_libList.setItem(index, 1, QTableWidgetItem(path))
        item = self.stw_libList.item(0, 0)

    def refresh_add_cb(self):  # 添加库的下拉列表
        self.scb_lib_type.clear()
        self.scb_icon.clear()
        for one in MYSET.lib_type.keys():
            self.scb_lib_type.addItem(one)
        icon_folder = ALLSET.sbox_path + "/file/icon02/"
        icons = os.listdir(icon_folder)
        for icon in icons:
            icon_num = icon.split(".")[0]
            icon = QtGui.QIcon(f"{icon_folder}/{icon_num}.svg")
            self.scb_icon.addItem(icon, icon_num)
        self.scb_lib_type.setCurrentIndex(0)
        self.scb_icon.setCurrentIndex(0)

    def refresh_index_cb(self):  # 添加库的下拉列表
        self.scb_index.clear()
        for i in range(len(MYSET.lib_list) + 1):
            index = str(i + 1)
            self.scb_index.addItem(index)
        self.scb_index.setCurrentIndex(len(MYSET.lib_list))

    def refresh_lib_set(self):  # 点击lib_item刷新库选项设置
        self.refresh_lib_tips(-1)
        index = self.stw_libList.currentRow()
        lib = MYSET.lib_list[index]
        self.sle_libName.setText(lib["name"])
        self.sle_libPath.setText(lib["path"])

        self.scb_lib_type.setCurrentText(MYSET.lib_list[index]["type"])
        self.scb_icon.setCurrentText(MYSET.lib_list[index]["icon"])
        lib_index = str(index + 1)
        self.scb_index.setCurrentText(lib_index)
        if "auto_update" in lib:
            self.sr_libAutoUpdate.setChecked(lib["auto_update"])
        else:
            self.sr_libAutoUpdate.setChecked(False)

    def sel_lib_floder(self):  # 选择库文件夹
        packPath = hou.ui.selectFile(
            file_type=hou.fileType.Directory,
            title="Select Lib Path",
            start_directory="$SnailBox/lib",
        )
        if packPath:
            if packPath.endswith("/"):
                packPath = packPath[:-1]
            if not packPath.startswith("$SnailBox"):
                packPath = hou.text.expandString(packPath)
            packPath = packPath.replace("\\", "/")
            self.sle_libPath.setText(packPath)

    def refresh_lib_tips(self, option=0):  # 改变lib
        tips = []
        if option == -1:
            if ALLSET.language:
                tips = [
                    "* 删除: 需要点击选择表格中的库之后才能删除",
                    "* 更改: 可以更改资产库名,图标,序号,库路径等选项",
                    "* 更新: 如果资产库中增删了资产,点击手动更新一次,原资产设置会保留",
                    "* 自动更新: 每次打开插件会重新扫描库,资产常有增减的库,可以激活此项",
                ]
            else:
                tips = [
                    "* Delete: Select a lib, delete it",
                    "* Modify: Select a lib, Change the library name, icon, index, library path",
                    "* Update: If the lib has added or deleted assets, this lib will scanned again",
                    "* Auto Update: The library will be scanned again every time the tool is opened",
                ]
        else:
            lib_type = self.scb_lib_type.currentText()
            if ALLSET.language:
                tips = MYSET.lib_type[lib_type].get("tip_zh")
            else:
                tips = MYSET.lib_type[lib_type].get("tip_en")
        self.t_tips.update_tips(tips)

    def refresh_other_tips(self):  # 改变lib
        if ALLSET.language:
            tips2 = [
                "* 节点预设: 选择预设,点击创建纹理节点按钮,自动添加相应的节点并设置纹理参数",
                "* 添加预设: 拖拽节点参数到添加按钮上,不是拖拽节点",
                "* 删除预设: 选择预设列表一项,点击删除按钮即可删除",
            ]
            tips3 = [
                "* 工具不能检测出节点中有文件类型参数,可以手动设置一个参数",
                "* 设置纹理的节点有多个文件参数类型,指定一个参数作为纹理参数",
                "* 添加自定义节点: 拖拽节点参数到添加按钮上,不是拖拽节点",
                "* 删除预设: 选择预设列表一项,点击删除按钮即可删除",
            ]
        else:
            tips2 = [
                "* Select preset and click preset texture Node, tool create texture node and set texture parm",
                "* Drag and drop node parameter to Add, not drag and drop node",
                "* Select item from list, click Delate button to delate",
            ]
            tips3 = [
                "* The tool cannot detect a file type parameter, specify one parm from node",
                "* The nood have many file type parms, specify one parm as texture parm",
                "* Drag and drop node parameter to Add, not drag and drop node",
                "* Select item from list, click Delate button to delate",
            ]
        self.t_tips2.update_tips(tips2)
        self.t_tips3.update_tips(tips3)

    def sel_index(self):
        index = self.stw_libList.currentRow()
        if index == -1:
            msg = "请在表格中点击选择一个库" if ALLSET.language else "Select a lib"
            hou.ui.displayMessage(msg)
            return -1
        return index

    def rescan_lib(self):  # 更新库
        index = self.sel_index()
        if index == -1:
            return
        MYSET.gen_lib_json(index, 1)

    def del_lib(self):  # 删除库
        index = self.sel_index()
        if index == -1:
            return
        MYSET.del_lib(index)
        self.refresh_index_cb()
        self.refresh_table_libList()
        self.update_lib()

    def mod_lib(self):  # 修改库
        before_index = self.sel_index()
        if before_index == -1:
            return
            # 读取原来的lib.json
        lib_json = MYSET.lib_list[before_index]
        before_name = lib_json.get("name")
        before_type = lib_json.get("type")

        lib_type = self.scb_lib_type.currentText()
        lib_icon_index = self.scb_icon.currentText()
        lib_name = self.sle_libName.text()
        lib_path = self.sle_libPath.text()
        new_index = int(self.scb_index.currentText()) - 1
        if not lib_name or not lib_path:
            msg = (
                "请输入库名称和路径"
                if ALLSET.language
                else "Please enter the library name and path"
            )
            hou.ui.displayMessage(msg)
            return
        if before_name != lib_name:
            msg2 = "库名称不能修改" if ALLSET.language else "Library name can't be modified"
            hou.ui.displayMessage(msg2)
            self.refresh_lib_set()
            return
        if before_type != lib_type:
            msg3 = "库类型不能修改" if ALLSET.language else "Library type can't be modified"
            hou.ui.displayMessage(msg3)
            self.refresh_lib_set()
            return

        lib_json["icon"] = lib_icon_index
        lib_json["path"] = lib_path

        MYSET.lib_list.pop(before_index)
        MYSET.lib_list.insert(new_index, lib_json)
        MYSET.lib_sort.pop(before_index)
        MYSET.lib_sort.insert(new_index, lib_name)
        MYSET.save_set()
        MYSET.save_lib_json(lib_name)
        self.refresh_table_libList()
        self.refresh_lib_set()
        self.update_lib()

    def toggle_autoUpdate(self):  # 自动更新激活
        index = self.stw_libList.currentRow()
        if index == -1:
            return
        MYSET.lib_list[index]["auto_update"] = self.sr_libAutoUpdate.isChecked()
        lib_json = MYSET.lib_list[index]
        lib_name = lib_json.get("name")
        MYSET.save_lib_json(lib_name)

    def add_lib(self, custom_lib={}):  # 添加库
        lib_type = self.scb_lib_type.currentText()
        lib_icon_index = self.scb_icon.currentText()
        lib_name = self.sle_libName.text()
        lib_path = self.sle_libPath.text()
        lib_auto_updte = self.sr_libAutoUpdate.isChecked()

        lib_index = int(self.scb_index.currentText()) - 1
        if not lib_name or not lib_path:
            msg = (
                "请输入库名称和路径"
                if ALLSET.language
                else "Please enter the library name and path"
            )
            hou.ui.displayMessage(msg)
            return
        if lib_name in [one["name"] for one in MYSET.lib_list]:
            msg = f"{lib_name}库已存在" if ALLSET.language else f"{lib_name} library already exists"
            hou.ui.displayMessage(msg)
            return
        if not custom_lib:
            lib_dict = {
                "name": lib_name,
                "icon": lib_icon_index,
                "path": lib_path,
                "type": lib_type,
                "auto_update": lib_auto_updte,
            }
            if lib_type == "Custom lib":
                self.dialog.show()
                return
        else:
            lib_dict = {
                "name": lib_name,
                "icon": lib_icon_index,
                "path": lib_path,
                "type": lib_type,
                "auto_update": lib_auto_updte,
                "other_lib": custom_lib,
            }

        # MYSET.lib_list.insert(lib_index, lib_dict)
        # res = MYSET.gen_lib_json(lib_index)
        # if not res:
        #     MYSET.lib_list.pop(lib_index)
        #     return
        res = MYSET.add_lib(lib_index, lib_dict)
        if res:
            self.refresh_index_cb()
            self.refresh_table_libList()
            self.dialog.close()
            self.update_lib()

    def toggle_setBg(self):  # 设置背景
        MYSET.setBg = self.cb_nodebg.isChecked()
        MYSET.save_set()

    def toggle_rename01(self):  # 重命名选项
        MYSET.rename01 = self.cb_rename01.isChecked()
        MYSET.save_set()

    def toggle_rename02(self):  # 重命名选项
        MYSET.rename02 = self.cb_rename02.isChecked()
        MYSET.save_set()

    # region 添加预设和添加自定义节点
    def check_parm(self, parm_path, node_path):  # 添加预设
        res = True
        if node_path:
            if ALLSET.language:
                hou.ui.displayMessage("请拖入参数，而不是节点")
            else:
                hou.ui.displayMessage("Please drop parmater, not drop node")
            return
        parm = hou.parm(parm_path)
        if not parm:
            return False
        parmname = parm.parmTemplate().name()
        try:
            parmtype = str(hou.parm(parm_path).parmTemplate().fileType())
            if parmtype != "fileType.Image":
                raise Exception()
        except:
            if ALLSET.language:
                msg = f"检测参数类型非 File-Image,\n请确认是否强制添加参数 {parmname},\n设置纹理时可能会失败"
            else:
                msg = f"Parameter type need to be File-Image,\nPlease confirm whether to force add parameter {parmname},\nSetting texture may fail"
            btn_index2 = hou.ui.displayMessage(
                msg,
                buttons=("Cancel", "OK"),
                close_choice=0,
            )
            if not btn_index2:
                res = False
        finally:
            return res

    def add_preset(self, parm_path, node_path):  # 添加预设
        res = self.check_parm(parm_path, node_path)
        if not res:
            return
        nodeclass = hou.parm(parm_path).node().type().nameWithCategory()
        parmname = hou.parm(parm_path).parmTemplate().name()
        btn_index, preset_name = hou.ui.readInput(
            "Preset Name",
            buttons=("Cancel", "OK"),
            default_choice=1,
            title="Preset Name",
            close_choice=0,
            initial_contents=nodeclass,
        )
        if not btn_index or preset_name == "":
            return
        # item = f"{preset_name} > {nodeclass}  >  {parmname}"
        # self.slw_node_preset.addItem(item)
        if preset_name not in MYSET.option_nodes:
            MYSET.option_nodes[preset_name] = [nodeclass, parmname]
            MYSET.save_set()
            self.refresh_node_preset()
        else:
            msg = "此预设名已存在" if ALLSET.language else "This preset type has been exist"
            hou.ui.displayMessage(msg)

    def add_other_parm(self, parm_path, node_path):  # 添加预设
        res = self.check_parm(parm_path, node_path)
        if not res:
            return
        nodeclass = hou.parm(parm_path).node().type().nameWithCategory()
        parmname = hou.parm(parm_path).parmTemplate().name()
        # item = f"{nodeclass}  >  {parmname}"
        if nodeclass not in MYSET.node_parm_list:
            MYSET.node_parm_list[nodeclass] = parmname
            MYSET.save_set()
            self.refresh_other_parm()
        else:
            msg = "此节点类型已添加" if ALLSET.language else "This node type has been exist"
            hou.ui.displayMessage(msg)

    def del_node_preset(self):  # 删除节点预设
        index = self.slw_node_preset.currentRow()
        msg = "请在列表中选择一项" if ALLSET.language else "Please select one item in the list"
        if index == -1:
            hou.ui.displayMessage(msg)
            return
        else:
            node_preset = self.slw_node_preset.currentItem().text()
            key = node_preset.split(" > ")[0]
            MYSET.option_nodes.pop(key)
            self.refresh_node_preset()
            MYSET.save_set()

    def del_other_parm(self, index=0):  # 添加其他节点
        index = self.slw_other_parm.currentRow()
        if index == -1:
            msg = "请在列表中选择一项" if ALLSET.language else "Please select one item in the list"
            hou.ui.displayMessage(msg)
            return
        else:
            node_preset = self.slw_other_parm.currentItem().text()
            key = node_preset.split(" > ")[0]
            MYSET.node_parm_list.pop(key)
            self.refresh_other_parm()
            MYSET.save_set()

    # endregion

    def get_dialog_dict(self):  # 添加其它库时的对话框
        custom_lib = {}
        pre = self.dialog.le_filter1.text()
        suf = self.dialog.le_filter2.text()
        filter_folders_list = []
        filter_folders = self.dialog.le_filter3.text()
        if filter_folders:
            filter_folders_list = filter_folders.split(", ")
        formats = []
        f1 = self.dialog.cb_exr.isChecked()
        if f1:
            formats.append("exr")
        f2 = self.dialog.cb_hdr.isChecked()
        if f2:
            formats.append("hdr")
        f3 = self.dialog.cb_tif.isChecked()
        if f3:
            formats.append("tif")
        f4 = self.dialog.cb_png.isChecked()
        if f4:
            formats.append("png")
        f5 = self.dialog.cb_jpg.isChecked()
        if f5:
            formats.append("jpg")

        f6 = self.dialog.le_otherFormat.text()
        if f6 and f6 not in formats:
            formats.append(f6.lower())
        size = self.dialog.sb_size.value()
        sr_copy0 = self.dialog.rb_group1.isChecked()
        if sr_copy0:
            group_set = 1
        sr_copy1 = self.dialog.rb_group2.isChecked()
        if sr_copy1:
            group_set = 2
        sr_copy2 = self.dialog.rb_group3.isChecked()
        if sr_copy2:
            group_set = 3
        custom_lib = {
            "filter_pre": pre,
            "filter_suf": suf,
            "filter_folders": filter_folders_list,
            "formats": formats,
            "min_size": size,
            "group_iter": group_set,
        }
        self.add_lib(custom_lib)
        self.dialog.close()

    def load_language(self):  # 加载语言
        try:
            if ALLSET.language:
                self.pa.translator.load(f"{ALLSET.sbox_path}/scripts/python/hdrTex/tr_ui_zh.pm")
            else:
                self.pa.translator.load(f"{ALLSET.sbox_path}/scripts/python/hdrTex/tr_ui_en.pm")
            self.retranslateUi()
            # self.tb_bz.toggle_language(ALLSET.language)
        except:
            hou.ui.displayMessage("Can't find language file")

    def retranslateUi(self):  # 重新翻译
        try:
            self.cb_rename01.setText(self.tr("Node rename for set texture"))
            self.cb_rename02.setText(self.tr("Node rename for add preset texture node"))
            self.cb_nodebg.setText(self.tr("Set node background for set texture"))
            self.sb_libDel.setText(self.tr("Delete"))
            self.sb_libMod.setText(self.tr("Modify"))
            self.sb_libRescan.setText(self.tr("Update"))
            self.sr_libAutoUpdate.setText(self.tr("Auto Update"))
            self.sb_libAdd.setText(self.tr("Add"))
            self.sb_del_node_preset.setText(self.tr("Delete"))
            self.lb_add_node_preset.setText(self.tr("Drag and drop parameter here to Add"))
            self.sb_del_other_parm.setText(self.tr("Delete"))
            self.lb_add_other_parm.setText(self.tr("Drag and drop parameter here to Add"))
            self.stw.setTabText(self.stw.indexOf(self.s_tab_0), self.tr("Options"))
            self.stw.setTabText(self.stw.indexOf(self.s_tab_1), self.tr("Add Library"))
            self.stw.setTabText(self.stw.indexOf(self.s_tab_2), self.tr("Add Preset"))
            self.stw.setTabText(self.stw.indexOf(self.s_tab_3), self.tr("Custom Node"))

            self.dialog.lb_filter1.setText(self.tr("Prefix Filter"))
            self.dialog.le_filter1.setPlaceholderText(self.tr("sm_ (Exclude sm_xxx.exr files)"))
            self.dialog.lb_filter2.setText(self.tr("Suffix Filter"))
            self.dialog.le_filter2.setPlaceholderText(self.tr("_sm (Exclude xxx_sm.exr files)"))
            self.dialog.lb_filter3.setText(self.tr("Folder Filter"))
            self.dialog.le_filter3.setPlaceholderText(
                self.tr("folder_1, folder_2 (Exclude folder_1 folder_2, separate with ' , ')")
            )
            self.dialog.lb_size.setText(self.tr("Size Filter"))
            self.dialog.lb_sizeTip.setText(self.tr("Exclude files smaller than the set size"))
            self.dialog.lb_group.setText(self.tr("Group Level"))
            self.dialog.lb_groupTip.setText(
                self.tr("D:/xx/3/2/1/xxx.exr Group with folder hierarchy")
            )
        except Exception as e:
            display_status(f"Snail_error_ht4: retranslateUi _ {e}")

    def update_lib(self):
        self.pa.updateMenu()
        self.pa.change_lib()

    def main_show(self):
        self.init_set()
        self.show()

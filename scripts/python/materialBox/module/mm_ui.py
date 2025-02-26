from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from utils import *
from .mm_set import MYSET


class Ui_Snail_MM(QWidget):
    def setupUi(self, Snail_MM):
        if not Snail_MM.objectName():
            Snail_MM.setObjectName("Snail_MM")
        Snail_MM.setWindowModality(Qt.NonModal)
        Snail_MM.resize(780, 602)
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Snail_MM.setFont(font)
        Snail_MM.setAutoFillBackground(False)
        Snail_MM.setStyleSheet(
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
        self.horizontalLayout_4 = QHBoxLayout(Snail_MM)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QFrame(Snail_MM)
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

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, 0, -1)
        self.layout_top = QHBoxLayout()
        self.layout_top.setObjectName("layout_top")
        self.hl_2 = QHBoxLayout()
        self.hl_2.setObjectName("hl_2")
        self.hl_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.hl_2.setContentsMargins(-1, 0, 10, -1)

        self.layout_top.addLayout(self.hl_2)

        self.verticalLayout_15.addLayout(self.layout_top)

        self.splitter_h = QSplitter(Snail_MM)
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
        self.lw_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.lw_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lw_view.setProperty("isWrapping", True)
        self.lw_view.setResizeMode(QListView.Adjust)
        self.lw_view.setViewMode(QListView.IconMode)

        self.verticalLayout.addWidget(self.lw_view)

        self.pb_progress = QProgressBar(self.verticalLayoutWidget_3)
        self.pb_progress.setObjectName("pb_progress")
        self.pb_progress.setMaximumSize(QSize(16777215, 20))
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
        self.w_info.setGeometry(QRect(0, 0, 335, 148))
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
        self.w_asset.setGeometry(QRect(0, 0, 334, 148))
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

        self.verticalLayout_15.addWidget(self.splitter_h)

        self.layout_bottom = QHBoxLayout()
        self.layout_bottom.setObjectName("layout_bottom")
        self.layout_bottom.setSizeConstraint(QLayout.SetMinimumSize)
        self.layout_bottom.setContentsMargins(5, 0, 5, 0)

        self.verticalLayout_15.addLayout(self.layout_bottom)

        self.verticalLayout_15.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_15)
        self.lw_menu1.setCurrentRow(-1)
        QMetaObject.connectSlotsByName(Snail_MM)


class Ui_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pa = parent
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        self.setWindowTitle("SnailBox Texture Browser Settings")
        self.setStyleSheet(
            "*{background-color: rgb(35, 35, 39);}" "*:hover{color: rgb(255, 191, 0);}"
        )
        self.resize(640, 560)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        self.init_ui()

    def init_ui(self):
        layout_main = QVBoxLayout()
        self.stw = QTabWidget(self)
        self.stw.setStyleSheet(
            "QTabBar::tab:selected {color: rgb(255,163,32);}"
            "QTabBar {font-family: Microsoft YaHei UI; font-size: 14px;}"
        )
        layout_main.addWidget(self.stw)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout_01 = QVBoxLayout()
        self.cb_copyAssets = Snail_CheckBox("Copy assets to lib when Collecting material")
        self.cb_nodebg = Snail_CheckBox("Set node background for crate material")
        self.cb_copyAssets.toggled.connect(self.toggle_copy)
        self.cb_nodebg.toggled.connect(self.toggle_setBg)
        layout_01.addWidget(self.cb_copyAssets)
        layout_01.addWidget(self.cb_nodebg)

        layout_main0 = QVBoxLayout()
        layout_main0.addLayout(layout_01)
        layout_main0.addItem(spacer)
        self.s_tab_0 = QWidget()
        self.s_tab_0.setEnabled(True)
        self.s_tab_0.setLayout(layout_main0)
        self.stw.addTab(self.s_tab_0, "")
        self.stw.setTabText(self.stw.indexOf(self.s_tab_0), "Options")

        layout_11 = QVBoxLayout()
        self.stw_libList = Snail_Table(self)
        self.stw_libList.setColumnCount(2)
        self.stw_libList.itemClicked.connect(self.refresh_lib_set)

        layout_11.addWidget(self.stw_libList)
        layout_12 = QHBoxLayout()
        self.scb_lib_type = Snail_ComboBox()
        self.scb_lib_type.activated.connect(self.refresh_lib_tips)

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
        self.sle_libPath = Snail_LineEdit("snailBox_this")
        self.sle_libPath.setDisabled(True)
        self.sb_selPath = Snail_IconBtn("BUTTONS_chooser_folder", "Select lib path")
        self.sb_selPath.clicked.connect(self.sel_lib_floder)
        layout_13.addWidget(self.sle_libPath)
        layout_13.addWidget(self.sb_selPath)
        layout_13.setStretch(0, 1)

        layout_14 = QHBoxLayout()
        self.sb_libDel = Snail_Btn("Delete")
        self.sb_libMod = Snail_Btn("Modify")
        self.sb_libRescan = Snail_Btn("Update")
        self.sb_libAdd = Snail_Btn("Add")
        self.sb_libAdd.clicked.connect(self.add_lib)
        self.sb_libDel.clicked.connect(self.del_lib)
        self.sb_libMod.clicked.connect(self.mod_lib)
        self.sb_libRescan.clicked.connect(self.rescan_lib)
        layout_14.addWidget(self.sb_libDel)
        layout_14.addWidget(self.sb_libMod)
        layout_14.addWidget(self.sb_libRescan)
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

        layout_21 = QVBoxLayout()
        self.slw_other_nodes = Snail_List(self)
        layout_21.addWidget(self.slw_other_nodes)

        layout_22 = QHBoxLayout()
        self.sb_del_node_preset = Snail_Btn("Delete")
        self.sb_del_node_preset.clicked.connect(self.del_other_node)
        self.lb_add_node_preset = Snail_DropLabel(
            "Drag and drop node here to Add", fun=self.add_other_node
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
        layout_23.addWidget(self.t_tips2)

        layout_main2 = QVBoxLayout()
        layout_main2.addLayout(layout_21)
        layout_main2.addLayout(layout_22)
        layout_main2.addLayout(layout_23)
        self.s_tab_2 = QWidget()
        self.s_tab_2.setEnabled(True)
        self.s_tab_2.setLayout(layout_main2)
        self.stw.addTab(self.s_tab_2, "")
        self.stw.setTabText(self.stw.indexOf(self.s_tab_2), "Other Node")

        layout_31 = QVBoxLayout()
        self.slw_fliter_nodes = Snail_List(self)
        layout_31.addWidget(self.slw_fliter_nodes)

        layout_32 = QHBoxLayout()
        self.sb_del_other_parm = Snail_Btn("Delete")
        self.sb_del_other_parm.clicked.connect(self.del_filter_node)
        self.lb_add_other_parm = Snail_DropLabel(
            "Drag and drop node here to Add", fun=self.add_filter_node
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
        self.stw.setTabText(self.stw.indexOf(self.s_tab_3), "Filter Node")

        self.setLayout(layout_main)

    def init_set(self):
        self.refresh_option()
        self.refresh_other_node()
        self.refresh_filter_node()
        self.refresh_table_libList()
        self.refresh_add_cb()
        self.refresh_index_cb()
        self.refresh_lib_tips(-1)
        self.refresh_other_tips()
        self.load_language()

    def refresh_option(self):
        self.cb_copyAssets.setChecked(MYSET.copy_option)
        self.cb_nodebg.setChecked(MYSET.setBg)

    def refresh_other_node(self):
        self.slw_other_nodes.clear()
        for one in MYSET.other_nodes:
            self.slw_other_nodes.addItem(one)

    def refresh_filter_node(self):
        self.slw_fliter_nodes.clear()
        for one in MYSET.filter_nodes:
            self.slw_fliter_nodes.addItem(one)

    def refresh_table_libList(self):
        self.stw_libList.clearContents()
        self.stw_libList.setRowCount(len(MYSET.lib_list))
        for index, lib in enumerate(MYSET.lib_list):
            name = lib["name"]
            path = lib["path"]
            self.stw_libList.setItem(index, 0, QTableWidgetItem(name))
            self.stw_libList.setItem(index, 1, QTableWidgetItem(path))

    def refresh_add_cb(self):
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

    def refresh_index_cb(self):
        self.scb_index.clear()
        for i in range(len(MYSET.lib_list) + 1):
            index = str(i + 1)
            self.scb_index.addItem(index)
        self.scb_index.setCurrentIndex(len(MYSET.lib_list))

    def refresh_lib_set(self):
        self.refresh_lib_tips(-1)
        index = self.stw_libList.currentRow()
        lib = MYSET.lib_list[index]
        self.sle_libName.setText(lib["name"])
        self.sle_libPath.setText(lib["path"])
        self.scb_lib_type.setCurrentText(lib.get("type"))
        self.scb_icon.setCurrentText(lib.get("icon"))
        lib_index = str(index + 1)
        self.scb_index.setCurrentText(lib_index)

    def sel_lib_floder(self):
        path = MYSET.lib_path
        path_abs = hou.text.expandString(path)
        if not os.path.isdir(path_abs):
            os.makedirs(path_abs)
        mat_type = self.scb_lib_type.currentText()
        if mat_type == "Custom lib":
            hou.ui.showInFileBrowser(path_abs + "/")
        else:
            packPath = hou.ui.selectFile(
                file_type=hou.fileType.Directory,
                title="Select asset path",
                start_directory=path,
            )
            if packPath:
                if packPath.endswith("/"):
                    packPath = packPath[:-1]
                packPath = packPath.replace("\\", "/")
                self.sle_libPath.setText(packPath)

    def refresh_lib_tips(self, option=0):
        tips = []
        if option == -1:
            if ALLSET.language:
                tips = [
                    "* 删除: 需要点击选择表格中的库之后才能删除",
                    "* 更改: 可以更改资产库名,图标,序号,库路径等选项",
                    "* 更新: 手动扫描一次资产库,更新库lib_item.json文件",
                ]
            else:
                tips = [
                    "* Delete: Select a lib, delete it",
                    "* Modify: Select a lib, Change the library name, icon, index, library path",
                    "* Update: Scan the library manually, update the library lib_item.json file",
                ]
        else:
            lib_type = self.scb_lib_type.currentText()
            if ALLSET.language:
                tips = MYSET.lib_type[lib_type].get("tip_zh")
            else:
                tips = MYSET.lib_type[lib_type].get("tip_en")
            if lib_type == "Custom lib":
                self.sle_libPath.setDisabled(True)
            else:
                self.sle_libPath.setDisabled(False)
        self.t_tips.update_tips(tips)

    def refresh_other_tips(self):
        if ALLSET.language:
            tips2 = [
                "* 其它材质类型: 工具不能自动检测出一些材质节点类型,可以手动添加材质类型",
                "* 添加: 拖拽节点到添加按钮上,不是拖拽节点参数",
                "* 删除: 选择预设列表一项,点击删除按钮即可删除",
            ]
            tips3 = [
                "* 过滤材质类型: 可以过滤排除一些你不希望显示的材质类型",
                "* 添加: 拖拽节点到添加按钮上,不是拖拽节点参数",
                "* 删除: 选择预设列表一项,点击删除按钮即可删除",
            ]
        else:
            tips2 = [
                "* Other material type: Tool may can't detect some material node type, can add it manually",
                "* Drag and drop node to Add, not drag and drop node parameter",
                "* Select item from list, click Delate button to delate",
            ]
            tips3 = [
                "* Filter material type: You can filter out some material types that you don't want to show",
                "* Drag and drop node to Add, not drag and drop node parameter",
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

    def rescan_lib(self):
        index = self.sel_index()
        if index == -1:
            return
        lib_name = MYSET.lib_list[index].get("name")
        MYSET.scan_lib(lib_name)

    def del_lib(self):
        index = self.sel_index()
        if index == -1:
            return
        lib_name = MYSET.lib_list[index].get("name")
        MYSET.del_lib(lib_name)
        self.refresh_index_cb()
        self.refresh_table_libList()
        self.update_lib()

    def mod_lib(self):
        before_index = self.sel_index()
        if before_index == -1:
            return
        lib_json = MYSET.lib_list[before_index]
        before_name = lib_json.get("name")
        before_type = lib_json.get("type")

        lib_type = self.scb_lib_type.currentText()
        lib_icon_index = self.scb_icon.currentText()
        lib_name = self.sle_libName.text()
        lib_path = self.sle_libPath.text()
        new_index = int(self.scb_index.currentText()) - 1

        if not lib_name or not lib_path:
            msg1 = "请输入库名称和路径" if ALLSET.language else "Please enter library name and path"
            hou.ui.displayMessage(msg1)
            self.refresh_lib_set()
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

        try:
            lib_json["icon"] = lib_icon_index
            lib_json["path"] = lib_path
            lib_json_abs = MYSET.lib_path + "/" + before_name + "/lib.json"
            save_json(lib_json, lib_json_abs)
            MYSET.lib_list.pop(before_index)
            MYSET.lib_list.insert(new_index, lib_json)
            MYSET.lib_sort.pop(before_index)
            MYSET.lib_sort.insert(new_index, lib_name)
            MYSET.save_set()
        except Exception as e:
            display_status(f"Snail_error_usf: mod_lib _ {e}", 1)
            MYSET.scan_libs()
        self.refresh_table_libList()
        self.update_lib()

    def add_lib(self):
        lib_type = self.scb_lib_type.currentText()
        lib_icon_index = self.scb_icon.currentText()
        lib_name = self.sle_libName.text()
        if lib_type == "Custom lib":
            lib_path = "snailBox_this"
        else:
            lib_path = self.sle_libPath.text()
        lib_index = int(self.scb_index.currentText()) - 1

        if not lib_name or not lib_path:
            if ALLSET.language:
                msg = "请输入库名称和路径"
            else:
                msg = "Please enter the library name and path"
            hou.ui.displayMessage(msg)
            return

        if lib_name in [one["name"] for one in MYSET.lib_list]:
            if ALLSET.language:
                msg2 = f"{lib_name}库已存在"
            else:
                msg2 = f"{lib_name} library already exists"
            hou.ui.displayMessage(msg)
            return

        lib_dict = {
            "name": lib_name,
            "icon": lib_icon_index,
            "path": lib_path,
            "type": lib_type,
        }
        res = MYSET.add_lib(lib_dict, lib_index)
        if res:
            self.refresh_index_cb()
            self.refresh_table_libList()
            self.update_lib()

    def toggle_setBg(self):
        MYSET.setBg = self.cb_nodebg.isChecked()
        self.save_set()

    def toggle_copy(self):
        MYSET.copy_option = self.cb_copyAssets.isChecked()
        self.save_set()

    def add_other_node(self, parm_path, node_path):
        if parm_path:
            if ALLSET.language:
                hou.ui.displayMessage("请拖入节点，而不是参数")
            else:
                hou.ui.displayMessage("Please drop node, not drop parmater")
            return
        node_type = hou.node(node_path).type().nameWithCategory()
        if node_type not in MYSET.other_nodes:
            MYSET.other_nodes.append(node_type)
            self.save_set()
            self.refresh_other_node()
        else:
            msg = "此节点类型已存在" if ALLSET.language else "This node type has been exist"
            hou.ui.displayMessage(msg)

    def add_filter_node(self, parm_path, node_path):
        if parm_path:
            if ALLSET.language:
                hou.ui.displayMessage("请拖入节点，而不是参数")
            else:
                hou.ui.displayMessage("Please drop node, not drop parmater")
            return
        node_type = hou.node(node_path).type().nameWithCategory()

        if node_type not in MYSET.filter_nodes:
            MYSET.filter_nodes.append(node_type)
            self.save_set()
            self.refresh_filter_node()
        else:
            msg = "此节点类型已添加" if ALLSET.language else "This node type has been exist"
            hou.ui.displayMessage(msg)

    def del_other_node(self):
        index = self.slw_other_nodes.currentRow()
        msg = "请在列表中选择一项" if ALLSET.language else "Please select one item in the list"
        if index == -1:
            hou.ui.displayMessage(msg)
            return
        else:
            node_type = self.slw_other_nodes.currentItem().text()
            try:
                MYSET.other_nodes.remove(node_type)
                self.save_set()
            except Exception as e:
                display_status(f"Snail_error_set: del_other_node _ {e}")
            self.refresh_other_node()

    def del_filter_node(self):
        index = self.slw_fliter_nodes.currentRow()
        if index == -1:
            msg = "请在列表中选择一项" if ALLSET.language else "Please select one item in the list"
            hou.ui.displayMessage(msg)
            return
        else:
            node_type = self.slw_fliter_nodes.currentItem().text()
            try:
                MYSET.filter_nodes.remove(node_type)
                self.save_set()
            except Exception as e:
                display_status(f"Snail_error_set: del_filter_node _ {e}")
            self.refresh_filter_node()

    def save_set(self):
        MYSET.save_set()

    def load_language(self):
        try:
            if ALLSET.language:
                self.pa.translator.load(
                    f"{ALLSET.sbox_path}/scripts/python/materialBox/tr_ui_zh.pm"
                )
            else:
                self.pa.translator.load(
                    f"{ALLSET.sbox_path}/scripts/python/materialBox/tr_ui_en.pm"
                )
            self.retranslateUi()

        except:
            hou.ui.displayMessage("Can't find language file")

    def retranslateUi(self):
        try:
            self.cb_copyAssets.setText(self.tr("Copy assets to lib when Collecting material"))
            self.cb_nodebg.setText(self.tr("Set node background for crate material"))
            self.sb_libDel.setText(self.tr("Delete"))
            self.sb_libMod.setText(self.tr("Modify"))
            self.sb_libRescan.setText(self.tr("Update"))
            self.sb_libAdd.setText(self.tr("Add"))
            self.sb_del_node_preset.setText(self.tr("Delete"))
            self.lb_add_node_preset.setText(self.tr("Drag and drop node here to Add"))
            self.sb_del_other_parm.setText(self.tr("Delete"))
            self.lb_add_other_parm.setText(self.tr("Drag and drop node here to Add"))
            self.stw.setTabText(self.stw.indexOf(self.s_tab_0), self.tr("Options"))
            self.stw.setTabText(self.stw.indexOf(self.s_tab_1), self.tr("Add Library"))
            self.stw.setTabText(self.stw.indexOf(self.s_tab_2), self.tr("Other node"))
            self.stw.setTabText(self.stw.indexOf(self.s_tab_3), self.tr("Filter Node"))
        except Exception as e:
            display_status(f"Snail_error_ht4: retranslateUi _ {e}")

    def update_lib(self):
        self.pa.updateMenu()
        self.pa.menu_toggle()

    def main_show(self):
        self.init_set()
        self.show()

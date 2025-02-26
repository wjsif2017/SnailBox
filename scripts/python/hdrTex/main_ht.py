import threading
import time
from utils import *
from .module import *


class HT_Win(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Snail_ht")
        self.lib_index = 0
        self.lib = None
        self.filter_items = {}
        self.group_index = 0
        self.current_id = 0
        self.info_flip_index = 0

        self.translator = QtCore.QTranslator()
        QApplication.installTranslator(self.translator)

        self.item_start = 0
        self.add_num = 20

        self.init_ui()
        self.init_data()

    def init_ui(self):

        if 0:
            ufile = ALLSET.sbox_path + "/scripts/python/hdrTex/file/ht.ui"
            self.ui = QtUiTools.QUiLoader().load(ufile, parentWidget=self)
        else:
            self.ui = Ui_Snail_HT()
            self.ui.setupUi(self.ui)
            self.setStyleSheet("*{background-color: rgb(35, 35, 39);}")
        self.ui_set = Ui_Dialog(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        mainlayout = QVBoxLayout()
        mainlayout.setSpacing(0)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.addWidget(self.ui)
        self.setLayout(mainlayout)
        self.resize(780, 650)
        self.setWindowTitle("SnailBox Texture Browser")
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))

        self.ui.pb_progress.setHidden(True)

        self.ui.lw_view.setStyleSheet(
            "QListWidget::item:hover{background-color:rgba(0, 0, 0, 0);}"
            "QListWidget::item:selected{border: 2px solid rgb(255,163,32);}"
        )
        self.ui.lw_menu1.setStyleSheet(
            "QListWidget::item:selected {background-color:rgb(35, 35, 39); border-left: 6px solid rgb(255,163,32);}"
        )
        self.ui.lw_menu1.setIconSize(QtCore.QSize(40, 40))
        self.ui.lw_menu1.setGridSize(QtCore.QSize(70, 72))
        self.ui.splitter_h.splitterMoved.connect(self.stop_flipMove)
        self.ui.splitter_v.splitterMoved.connect(self.stop_flipMove)

        self.lw_info = Snail_List(self)
        self.lw_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.layout_info.addWidget(self.lw_info)
        self.thumb_viewer = thumbViewer()
        self.ui.layout_asset.addWidget(self.thumb_viewer)

        self.l_title = Snail_LabelB("Texture Browser", 14)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.cb_group = Snail_ComboBox()
        self.cb_group.setFixedWidth(200)
        self.cb_group_level = Snail_ComboBox()
        self.cb_group_level.setFixedWidth(100)
        self.cb_group_node = Snail_ComboBox()
        self.cb_group_node.setFixedWidth(150)
        self.cb_group.activated.connect(self.change_groups)
        self.cb_group_level.activated.connect(self.change_group_level)
        self.cb_group_node.activated.connect(self.change_group_node)
        self.ui.hl_top.addWidget(self.l_title)
        self.ui.hl_top.addItem(spacer)
        self.ui.hl_top.addWidget(self.cb_group_node)
        self.ui.hl_top.addWidget(self.cb_group_level)
        self.ui.hl_top.addWidget(self.cb_group)

        self.tb_bz = Snail_IconBtn_bz()
        self.tb_help = Snail_IconBtn_help()
        self.tb_language = Snail_IconBtn("snail_language", "Toggle language")
        self.tb_language.clicked.connect(self.toggle_language)
        self.tb_set = Snail_IconBtn("snail_set", "Settings")
        self.tb_set.clicked.connect(self.go_set)
        self.btn_refresh = Snail_Btn("Refresh")
        self.btn_createImg = Snail_Btn("Create thumbnail")
        self.btn_refresh.clicked.connect(self.change_lib)
        self.btn_createImg.clicked.connect(self.create_thumbnail_smart)
        self.ui.layout_bottom.addWidget(self.tb_set)
        self.ui.layout_bottom.addWidget(self.tb_bz)
        self.ui.layout_bottom.addWidget(self.tb_help)
        self.ui.layout_bottom.addWidget(self.tb_language)
        self.ui.layout_bottom.addWidget(self.btn_createImg)
        self.ui.layout_bottom.addWidget(self.btn_refresh)

        spacer2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ui.hl_2.addItem(spacer2)
        self.tb_addTexNode = Snail_IconBtn("snail_nodeTex", "Add node and set texture")
        self.tb_addTexNode.clicked.connect(self.add_nodes)
        self.ui.hl_2.addWidget(self.tb_addTexNode)
        self.tb_setTex = Snail_IconBtn("snail_setTex", "Set texture")
        self.tb_setTex.clicked.connect(self.set_Tex)
        self.ui.hl_2.addWidget(self.tb_setTex)
        self.tb_bigView = Snail_IconBtn("snail_big_viewer", "Zoom view")
        self.tb_bigView.clicked.connect(self.show_img)
        self.ui.hl_2.addWidget(self.tb_bigView)
        self.tb_folder = Snail_IconBtn("BUTTONS_folder", "Asset folder")
        self.tb_folder.clicked.connect(self.open_folder)
        self.ui.hl_2.addWidget(self.tb_folder)
        self.tb_ignore = Snail_IconBtn2("snail_ignore1", "snail_ignore2", "Toggle ignore")
        self.tb_ignore.clicked.connect(self.show_ignore)
        self.ui.hl_2.addWidget(self.tb_ignore)
        self.tb_delete = Snail_IconBtn("COMMON_delete", "Delete")
        self.tb_delete.clicked.connect(self.del_items)
        self.ui.hl_2.addWidget(self.tb_delete)
        self.tb_fav = Snail_IconBtn2("snail_fav1", "snail_fav2", "Solo fav")
        self.tb_fav.clicked.connect(self.solo_fav)
        self.ui.hl_2.addWidget(self.tb_fav)
        self.tb_size = Snail_IconBtn("snail_w", "toggle thumbnail size")
        self.tb_size.clicked.connect(self.change_thumb_size)
        self.ui.hl_2.addWidget(self.tb_size)
        self.tb_aspect = Snail_IconBtn("snail_wh", "Aspect ratio")
        self.tb_aspect.clicked.connect(self.change_group_wh)
        self.ui.hl_2.addWidget(self.tb_aspect)
        self.tb_flip = Snail_IconBtn2("snail_info_flip1", "snail_info_flip2", "Flip info")
        self.tb_flip.clicked.connect(self.flip_info)
        self.ui.hl_2.addWidget(self.tb_flip)

        self.ui.lw_menu1.itemClicked.connect(self.menu_toggle)
        self.ui.lw_view.itemClicked.connect(self.click_item)
        self.ui.lw_view.itemDoubleClicked.connect(self.double_click_item)
        self.ui.lw_view.verticalScrollBar().valueChanged.connect(self.on_scroll)
        self.ui.lw_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.lw_view.customContextMenuRequested.connect(self.rightClickContext)

    def init_data(self):
        self.load_language()
        self.updateMenu()
        self.change_lib()
        if MYSET.lib_list:
            t1 = threading.Thread(target=self.auto_update)
            t1.start()

    def change_lib(self, init_group=True):
        if self.lib:
            self.lib.update_lib_item()

        if init_group:
            self.group_index = 0
        self.filter_items = {}
        self.lib = Lib(self, self.lib_index)
        self.refresh()

    def auto_update(self):
        for index, lib in enumerate(MYSET.lib_list):
            if "auto_update" in lib and lib["auto_update"]:
                MYSET.gen_lib_json(index, 1)
                lib_name = lib["name"]
                self.display_status(f"Snail_error_ht: {lib_name} Update finished")

    def refresh(self):
        self.select_item_id = 0
        self.item_start = 0
        self.refresh_groups()
        self.refresh_option_level()
        self.refresh_option_node()
        self.refresh_btnItems()
        self.refresh_thumb_viewer()
        self.refresh_info()
        self.refresh_title()

    def refresh_title(self):
        self.l_title.setText(self.lib.lib_name)

    def refresh_groups(self):
        self.cb_group.clear()
        groups = self.lib.groups
        for group in groups:
            self.cb_group.addItem(group)

        group2 = groups[self.group_index]
        self.lib.get_group_filter_items(group2)
        self.cb_group.setCurrentIndex(self.group_index)

    def refresh_option_level(self):
        self.cb_group_level.clear()
        self.cb_group_level.addItem("Default")
        for option in self.lib.options:
            self.cb_group_level.addItem(option)
        current_option = self.lib.current_group_level
        if current_option:
            self.cb_group_level.setCurrentText(current_option)

    def refresh_option_node(self):
        self.cb_group_node.clear()
        for option in MYSET.option_nodes:
            self.cb_group_node.addItem(option)
        current_option = self.lib.current_group_node
        if current_option:
            self.cb_group_node.setCurrentText(current_option)

    def on_scroll(self, value):
        index = self.item_start + self.add_num
        item_widget = self.ui.lw_view.item(index)
        item_rect = self.ui.lw_view.visualItemRect(item_widget)
        lw_h = self.ui.lw_view.size().height()
        pos_y = item_rect.y()
        if pos_y < lw_h + 0:
            self.item_start += self.add_num
            self.refresh_btnItems()

    def refresh_btnItems(self):
        start = self.item_start
        if not start:
            self.get_filter_items()
            self.ui.lw_view.clear()
        i = 0
        end = start + self.add_num
        for id, item in self.filter_items.items():
            try:
                if i < start:
                    i += 1
                    continue
                thumbnail_btn = item.get_thumbnail_btn()
                btnItem = QListWidgetItem()
                btnItem.setSizeHint(item.thumbnail_size)
                btnItem.setData(QtCore.Qt.UserRole, id)
                self.ui.lw_view.addItem(btnItem)
                self.ui.lw_view.setItemWidget(btnItem, thumbnail_btn)
                i += 1
                if i > end:
                    break
            except Exception as e:
                display_status(f"Snail_error_ht: refresh_btnItems {id} _ {e}")
        if not start:
            self.on_scroll(0)

    def refresh_info(self):
        self.lw_info.clear()
        item = self.filter_items.get(self.current_id)
        if not item:
            return
        info_dict = item.file_dict_p
        for key, value in info_dict.items():
            item = QListWidgetItem(value)
            item.setToolTip(key)
            self.lw_info.addItem(item)

    def refresh_thumb_viewer(self):
        item = self.filter_items.get(self.current_id)
        if item:
            img = item.abs_thumb
        else:
            img = None
        self.thumb_viewer.update_img(img)

    def get_filter_items(self):
        group_items = self.lib.group_filter_items
        ignore_active = self.tb_ignore.isChecked()
        fav_active = self.tb_fav.isChecked()
        ignore_group = 1 if self.cb_group.currentText() == "Ignore items" else 0
        new_items = {}
        current_level = self.lib.current_group_level
        for id, item in group_items.items():
            if item.ignore and not ignore_active and not ignore_group:
                continue
            elif not item.fav and fav_active:
                continue
            elif current_level != "Default" and current_level not in item.option:
                continue
            else:
                new_items[id] = item
        self.filter_items = new_items

    def current_items(func):
        def wrapper(self, *args, **kwargs):
            sel_btnItems = self.ui.lw_view.selectedItems()
            if not sel_btnItems:
                msg = "请选择一个资产" if ALLSET.language else "Please select one item"
                hou.ui.displayMessage(msg)
                return
            ids = [btnItem.data(QtCore.Qt.UserRole) for btnItem in sel_btnItems]
            return func(self, ids, *args, **kwargs)

        return wrapper

    @current_items
    def click_item(self, ids, btn_item):
        id = ids[-1]
        self.current_id = id
        self.refresh_thumb_viewer()
        self.refresh_info()

    @current_items
    def double_click_item(self, ids):
        id = ids[-1]
        item = self.filter_items[id]
        item.set_tex()

    @current_items
    def create_thumbnail_force(self, ids):
        self.create_thumbnail(ids)

    @current_items
    def set_Tex(self, ids):
        id = ids[-1]
        item = self.filter_items[id]
        item.set_tex()

    @current_items
    def add_nodes(self, ids):
        for id in ids:
            item = self.filter_items[id]
            item.add_node()

    @current_items
    def show_img(self, ids):
        id = ids[-1]
        path = self.filter_items[id].abs_path
        self.lib.show_img(path)

    @current_items
    def del_items(self, ids):
        if ALLSET.language:
            msg = "请确认是否删除资产?"
        else:
            msg = "Please confirm to delete the asset?"
        btn_index = hou.ui.displayMessage(
            msg, buttons=("Delete", "Don't delete", "Cancel"), close_choice=2, default_choice=1
        )
        if btn_index == 2:
            return
        self.lib.del_items(ids, btn_index)
        self.refresh()

    @current_items
    def ignore_item(self, ids):
        for id in ids:
            item = self.filter_items[id]
            item.set_ignore()
        self.refresh()

    @current_items
    def open_folder(self, ids):
        id = ids[-1]
        item = self.filter_items[id]
        item.open_file_explorer()

    def menu_toggle(self):
        item = self.ui.lw_menu1.currentItem()
        index = item.data(QtCore.Qt.UserRole)
        if index == -1:
            self.ui_set.main_show()
            self.ui_set.stw.setCurrentIndex(1)
            return
        if index == self.lib_index:
            self.refresh()
            return
        else:
            self.lib_index = index
            self.change_lib()

    def create_thumbnail(self, ids):
        max = len(ids)
        if max > 1:
            self.ui.pb_progress.setHidden(0)
        self.ui.pb_progress.setMaximum(max)
        i = 1
        for id in ids:
            item = self.filter_items[id]
            item.create_thumbnail()
            self.ui.pb_progress.setValue(i)
            QApplication.processEvents()
            i += 1
        time.sleep(1)
        self.ui.pb_progress.setHidden(1)

    def create_thumbnail_smart(self):
        ids = [id for id, item in self.filter_items.items() if not item.abs_thumb]
        self.create_thumbnail(ids)

    def show_ignore(self):
        self.item_start = 0
        self.refresh_btnItems()

    def solo_fav(self):
        self.item_start = 0
        self.refresh_btnItems()

    def change_groups(self):
        self.group_index = self.cb_group.currentIndex()
        self.refresh()

    def change_group_level(self):
        group_level = self.cb_group_level.currentText()
        self.lib.reset_group_preset("level", group_level)
        self.refresh()

    def change_group_node(self):
        group_node = self.cb_group_node.currentText()
        self.lib.reset_group_preset("node", group_node)

    def change_group_wh(self):
        msg = (
            "请输入预览图宽高比"
            if ALLSET.language
            else "Please enter the width/height ratio of thumbnail"
        )
        msg2 = f"{msg}\n 1:1  2:1  1:2  3:2  4:3  5:4  ..."
        button_idx, values = hou.ui.readMultiInput(
            msg2,
            ("W", "H"),
            initial_contents=("1", "1"),
            title="Set Hight/Width",
            buttons=("OK", "Cancel"),
            default_choice=0,
            close_choice=1,
        )
        if button_idx == 1:
            return
        try:
            ratio = float(values[0]) / float(values[1])
            group_ratio = round(ratio, 2)
            self.lib.reset_group_preset("ratio", group_ratio)
            self.refresh()
        except:
            if ALLSET.language:
                msg3 = "请输入正确的宽高比数字"
            else:
                msg3 = "Please enter the correct width/height digit"
            hou.ui.displayMessage(msg3)

    def go_set(self):
        self.ui_set.main_show()

    def change_thumb_size(self):
        if MYSET.asset_width == 256:
            MYSET.asset_width = 128
        else:
            MYSET.asset_width += 32
        self.change_lib(False)

    def stop_flipMove(self):
        if self.info_flip_index:
            self.ui.splitter_v.setSizes([100, 0])
        else:
            self.ui.splitter_h.setSizes([100, 0])

    def flip_info(self):
        try:
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
            display_status(f"Snail_error_ht: flip_info _ {e}")

    def updateMenu(self):

        assetsList = MYSET.lib_list

        self.ui.lw_menu1.clear()
        if not assetsList:
            self.lib_index = -1
            icon = QtGui.QIcon(f"{ALLSET.sbox_path}/file/icon02/10042.svg")
            item = QListWidgetItem(icon, "")
            item.setSizeHint(QtCore.QSize(70, 60))
            item.setText("Add lib")
            item.setData(QtCore.Qt.UserRole, -1)
            self.ui.lw_menu1.addItem(item)
            return
        for index in range(len(assetsList)):
            try:
                icon_num = assetsList[index]["icon"]
                name = assetsList[index]["name"]
                icon = QtGui.QIcon(f"{ALLSET.sbox_path}/file/icon02/{icon_num}.svg")
                item = QListWidgetItem(icon, "")
                item.setSizeHint(QtCore.QSize(70, 60))
                item.setText(name)
                item.setData(QtCore.Qt.UserRole, index)
                index += 1
                self.ui.lw_menu1.addItem(item)
            except Exception as e:
                display_status(f"Snail_error_ht: updateMenu _ {e}")
        if self.lib_index in range(len(assetsList)):
            self.ui.lw_menu1.setCurrentRow(self.lib_index)
        else:
            self.lib_index = 0
            self.ui.lw_menu1.setCurrentRow(0)

    def rightClickContext(self, position=None):
        menu = Snail_Menu()
        idx = self.ui.lw_view.selectedItems()
        if idx:
            menu.addAction(self.tr_createThumb, self.create_thumbnail_force)
            menu.addAction(self.tr_setTex, self.set_Tex)
            menu.addAction(self.tr_addTexNode, self.add_nodes)
            menu.addAction(self.tr_zoomView, self.show_img)
            menu.addAction(self.tr_assetFolder, self.open_folder)
            menu.addAction(self.tr_delItem, self.del_items)
            menu.addAction(self.tr_ignoreItem, self.ignore_item)
        else:
            menu.addAction(self.tr_refresh, self.init_data)
            menu.addAction(self.updateThumb, self.create_thumbnail_smart)
        menu.exec_(self.ui.lw_view.viewport().mapToGlobal(position))

    def toggle_language(self):
        ALLSET.toggle_language()
        self.load_language()

    def load_language(self):
        try:
            if ALLSET.language:
                self.translator.load(f"{ALLSET.sbox_path}/scripts/python/hdrTex/tr_zh.pm")
            else:
                self.translator.load(f"{ALLSET.sbox_path}/scripts/python/hdrTex/tr_en.pm")
            self.retranslateUi()
            self.tb_bz.toggle_language(ALLSET.language)
        except:
            hou.ui.displayMessage("Can't find language file")

    def retranslateUi(self):
        try:
            self.tb_set.setToolTip(self.tr("Settings"))
            self.tb_help.setToolTip(self.tr("Online document"))
            self.tb_language.setToolTip(self.tr("Toggle language"))
            self.btn_refresh.setText(self.tr("Refresh"))
            self.btn_createImg.setText(self.tr("Create thumbnail"))
            self.tb_addTexNode.setToolTip(self.tr("Add node and set texture"))
            self.tb_setTex.setToolTip(self.tr("Set texture"))
            self.tb_bigView.setToolTip(self.tr("Zoom view"))
            self.tb_folder.setToolTip(self.tr("Asset folder"))
            self.tb_ignore.setToolTip(self.tr("Toggle show ignore"))
            self.tb_delete.setToolTip(self.tr("Delete item"))
            self.tb_fav.setToolTip(self.tr("Solo fav"))
            self.tb_aspect.setToolTip(self.tr("Aspect ratio"))
            self.tb_flip.setToolTip(self.tr("Flip info"))

            self.tr_createThumb = self.tr("Create thumb")
            self.tr_setTex = self.tr("Set texture")
            self.tr_addTexNode = self.tr("Texture node")
            self.tr_zoomView = self.tr("Zoom view")
            self.tr_assetFolder = self.tr("Asset folder")
            self.tr_delItem = self.tr("Delete")
            self.tr_ignoreItem = self.tr("Toggle ignore")
            self.tr_refresh = self.tr("Refresh")
            self.updateThumb = self.tr("Update thumb")

        except Exception as e:
            display_status(f"Snail_error_ht: retranslateUi _ {e}")

    def closeEvent(self, event):
        try:
            self.ui_set.close()
            self.lib.update_lib_item()
            houMainWindow = hou.qt.mainWindow()
            getChildWin = houMainWindow.findChild(QGraphicsView, "Snail_imgViewer")
            if getChildWin:
                getChildWin.setVisible(False)
            super.closeEvent(event)
        except:
            super().closeEvent(event)


def main_show():
    try:
        houMainWindow = hou.qt.mainWindow()
        getChildWin = houMainWindow.findChild(QWidget, "Snail_ht")
        getChildWin.close()
        getChildWin.deleteLater()
    except:
        pass

    ALLSET.verify_sig("ht")
    mywin2 = HT_Win()
    mywin2.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    mywin2.show()


def callInterface():
    panel = None
    pane_name = "SnailBox_hdrTex"
    ALLSET.verify_sig("ht")
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

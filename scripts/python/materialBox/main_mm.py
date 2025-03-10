import time
import hou
from utils.imgViewer import ImgViewer
from .module import *


class MM_Win(QWidget):
    def __init__(self):
        super(MM_Win, self).__init__()
        self.lib_name = "Project"
        self.lib = None
        self.filter_items = {}
        self.group_index = 0
        self.current_id = 0
        self.info_flip_index = 0
        self.show_menu = False
        self.last_index = 0
        self.translator = QtCore.QTranslator()
        QApplication.installTranslator(self.translator)

        self.init_ui()
        self.init_data()

    def init_ui(self):
        self.ui = Ui_Snail_MM()
        self.ui.setupUi(self.ui)
        self.setStyleSheet("*{background-color: rgb(35, 35, 39);}")
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui_set = Ui_Dialog(self)

        mainlayout = QVBoxLayout()
        mainlayout.setSpacing(0)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.addWidget(self.ui)
        self.setLayout(mainlayout)
        self.resize(780, 650)
        self.setWindowTitle("Snail Material Manger")
        self.setWindowIcon(QtGui.QIcon(ALLSET.sbox_path + "/icons/SnailBox.svg"))
        self.ui.lw_view.setStyleSheet(
            "QListWidget::item:hover{background-color:rgba(0, 0, 0, 0);}"
            "QListWidget::item:selected{border: 2px solid rgb(255,163,32);}"
        )
        self.ui.lw_menu1.setStyleSheet(
            "QListWidget::item:selected {background-color:rgb(35, 35, 39); border-left: 6px solid rgb(255,163,32);}"
        )
        self.ui.splitter_h.splitterMoved.connect(self.stop_flipMove)
        self.ui.splitter_v.splitterMoved.connect(self.stop_flipMove)

        self.timer_enter = QtCore.QTimer(self)
        self.enter = 1
        self.timer_enter.timeout.connect(self.stop_timer)
        self.ui.pb_progress.setHidden(True)

        self.updateMenu()
        self.img_viewer = ImgViewer()
        self.assetsViewer = Snail_assetsViewer()
        self.assetsViewer.lw_assets.itemClicked.connect(self.refresh_info2)
        self.assetsViewer.tb_bigView.clicked.connect(self.show_img)
        self.ui.layout_asset.addWidget(self.assetsViewer)

        self.lw_info = Snail_List(self)
        self.lw_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lw_info.itemChanged.connect(self.item_rename)
        self.lw_info.itemDoubleClicked.connect(self.info_doubleClicked)
        self.ui.layout_info.addWidget(self.lw_info)

        self.tb_bz = Snail_IconBtn_bz()
        self.tb_help = Snail_IconBtn_help()
        self.tb_language = Snail_IconBtn("snail_language", "Toggle language")
        self.tb_language.clicked.connect(self.toggle_language)
        self.tb_set = Snail_IconBtn("snail_set", "Settings")
        self.tb_set.clicked.connect(self.go_set)
        self.btn_refresh = Snail_Btn("刷新")
        self.btn_createImg = Snail_Btn("创建预览图")
        self.btn_refresh.clicked.connect(self.init_data)
        self.btn_createImg.clicked.connect(self.create_thumbnail_smart)
        self.ui.layout_bottom.addWidget(self.tb_set)
        self.ui.layout_bottom.addWidget(self.tb_bz)
        self.ui.layout_bottom.addWidget(self.tb_help)
        self.ui.layout_bottom.addWidget(self.tb_language)

        self.ui.layout_bottom.addWidget(self.btn_createImg)
        self.ui.layout_bottom.addWidget(self.btn_refresh)

        self.l_title = Snail_LabelB("Project", 14)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ui.layout_top.insertWidget(0, self.l_title)
        self.ui.layout_top.insertItem(1, spacer)
        self.cb_group = Snail_ComboBox()
        self.cb_group.setFixedWidth(200)
        self.ui.layout_top.addWidget(self.cb_group)

        self.tb_auto = Snail_IconBtn("snail_matThumb1", "Thumb with auto create")
        self.tb_auto.clicked.connect(self.create_thumbnail_force)
        self.ui.hl_2.addWidget(self.tb_auto)
        self.tb_capture = Snail_IconBtn("snail_matThumb2", "Thumb with capture")
        self.tb_capture.clicked.connect(self.item_capture_thumbnail)
        self.ui.hl_2.addWidget(self.tb_capture)
        self.tb_custom = Snail_IconBtn("snail_matThumb3", "Thumb with custom")
        self.tb_custom.clicked.connect(self.item_custom_thumbnail)
        self.ui.hl_2.addWidget(self.tb_custom)
        self.tb_folder = Snail_IconBtn("BUTTONS_folder", "Asset folder")
        self.tb_folder.clicked.connect(self.item_open_folder)
        self.ui.hl_2.addWidget(self.tb_folder)
        self.tb_delete = Snail_IconBtn("COMMON_delete", "Delete")
        self.tb_delete.clicked.connect(self.items_del)
        self.ui.hl_2.addWidget(self.tb_delete)
        self.tb_clear = Snail_IconBtn("BUTTONS_clear", "Clear unused Materials")
        self.tb_clear.clicked.connect(self.del_unused)
        self.ui.hl_2.addWidget(self.tb_clear)
        self.tb_fav = Snail_IconBtn2("snail_fav1", "snail_fav2", "Solo fav")
        self.tb_fav.clicked.connect(self.solo_fav)
        self.ui.hl_2.addWidget(self.tb_fav)
        self.tb_ignore = Snail_IconBtn2("snail_ignore1", "snail_ignore2", "Toggle ignore")
        self.tb_ignore.clicked.connect(self.show_ignore)
        self.ui.hl_2.addWidget(self.tb_ignore)
        self.tb_flip = Snail_IconBtn2("snail_info_flip1", "snail_info_flip2", "Flip info")
        self.tb_flip.clicked.connect(self.flip_info)
        self.ui.hl_2.addWidget(self.tb_flip)

        self.cb_group.activated.connect(self.change_groups)
        self.ui.lw_menu1.itemClicked.connect(self.menu_toggle)
        self.ui.lw_view.itemClicked.connect(self.item_click)
        self.ui.lw_view.itemDoubleClicked.connect(self.item_double_click)
        self.ui.lw_view.verticalScrollBar().valueChanged.connect(self.on_scroll)
        self.ui.lw_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.lw_view.customContextMenuRequested.connect(self.rightClickContext)

    def init_data(self):
        if not self.lib_name or self.lib_name == "Project":
            self.lib = ProjectMats()
            self.tb_clear.setDisabled(False)
        else:
            self.lib = LibMats(self.lib_name)
            self.tb_clear.setDisabled(True)
        self.load_language()
        self.group_index = 0
        self.l_title.setText(self.lib.lib_name)
        self.refresh()

    def refresh(self):
        self.current_id = 0
        self.refresh_groups()
        self.refresh_btnItems()
        self.refresh_info()
        self.refresh_assets()

    def refresh_groups(self):
        self.cb_group.clear()
        groups = self.lib.groups
        for group in groups:
            self.cb_group.addItem(group)

        self.cb_group.setCurrentIndex(self.group_index)

    def on_scroll(self):
        if self.last_index < 1:
            return
        all_num = len(self.filter_items)
        current_num = self.last_index + 1

        if current_num >= all_num:
            return
        index = self.last_index
        last_item_widget = self.ui.lw_view.item(index)
        item_rect = self.ui.lw_view.visualItemRect(last_item_widget)
        lw_h = self.ui.lw_view.size().height()
        pos_y = item_rect.y()

        if pos_y < lw_h and pos_y > 20:
            self.refresh_btnItems(current_num)

    def refresh_btnItems(self, start=0):
        addnum = 10
        if not start:
            self.get_filter_items()
            self.last_index = 0
            self.ui.lw_view.clear()
        i = 0
        end = start + addnum
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
                if i == end:
                    break
            except Exception as e:
                display_status(f"Snail_error_mm: refresh_btnItems {id} _ {e}")
        self.last_index = i - 1

        self.on_scroll()

    def refresh_info(self):
        self.lw_info.clear()
        mat = self.filter_items.get(self.current_id)
        if not mat:
            return
        info_dict = mat.get_info_dict()
        for key, value in info_dict.items():
            value2 = value.get("value")
            item = QListWidgetItem(value2)
            tip = value.get("tip")
            item.setToolTip(tip)
            if key == "name":
                item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
            if key == "update_time":
                color = value.get("color")
                if color:
                    qcolor = QtGui.QColor(*color)
                item.setTextColor(qcolor)
            fun = value.get("fun")
            if fun:
                item.setData(QtCore.Qt.UserRole, fun)
            self.lw_info.addItem(item)

    def refresh_info2(self):
        current_info = self.assetsViewer.get_current_info()
        self.lw_info.clear()
        if not current_info:
            return
        for key, value in current_info.items():
            item = QListWidgetItem(value)
            item.setToolTip(key)
            self.lw_info.addItem(item)

    def refresh_assets(self):
        self.assetsViewer.update()
        mat = self.filter_items.get(self.current_id)
        if not mat:
            return
        thumb_dir = mat.assets_thumb_dir
        assets = mat.get_assets()
        imgs = assets if assets else []
        self.assetsViewer.update(imgs, thumb_dir)

    def get_filter_items(self):
        group_filter_items = self.lib.group_filter_items
        ignore_active = self.tb_ignore.isChecked()
        fav_active = self.tb_fav.isChecked()
        ignore_group = 1 if self.cb_group.currentText() == "Ignore group" else 0
        filter_items = {}
        for id, item in group_filter_items.items():
            if item.ignore and not ignore_active and not ignore_group:
                continue
            elif not item.fav and fav_active:
                continue
            else:
                filter_items[id] = item
        self.filter_items = filter_items

    def menu_toggle(self):
        old_lib_name = self.lib_name
        item = self.ui.lw_menu1.currentItem()
        lib_name = item.data(QtCore.Qt.UserRole)
        if lib_name == "Add lib":
            self.ui_set.main_show()
            self.ui_set.stw.setCurrentIndex(1)
            return
        self.lib_name = lib_name
        if lib_name != old_lib_name:
            self.lib.update_lib_item()
        self.init_data()

    def check_mats_changed(self):
        self.lib.get_all_matNodes()
        if self.lib.is_updated:
            self.init_data()
            self.refresh()

    def current_ids(func):
        def wrapper(self, *args, **kwargs):
            sel_btnItems = self.ui.lw_view.selectedItems()
            if not sel_btnItems:
                msg = "请选择一个资产" if ALLSET.language else "Please select one item"
                hou.ui.displayMessage(msg)
                return
            ids = [btnItem.data(QtCore.Qt.UserRole) for btnItem in sel_btnItems]
            return func(self, ids, *args, **kwargs)

        return wrapper

    def current_item(func):
        def wrapper(self, *args, **kwargs):
            sel_btnItems = self.ui.lw_view.selectedItems()
            if not sel_btnItems:
                msg = "请选择一个资产" if ALLSET.language else "Please select one item"
                hou.ui.displayMessage(msg)
                return
            id = sel_btnItems[-1].data(QtCore.Qt.UserRole)
            item = self.filter_items.get(id)
            if not item:
                return
            return func(self, item, *args, **kwargs)

        return wrapper

    @current_item
    def item_click(self, item, btn_item):
        self.current_id = item.id
        self.refresh_info()
        self.refresh_assets()

    @current_item
    def item_double_click(self, item, btn_item):
        self.lib.item_duoble_click(item)

    def create_thumbnail(self, items=[]):
        if not items:
            return
        max = len(items)
        if max > 1:
            self.ui.pb_progress.setHidden(0)
            if hou.hipFile.hasUnsavedChanges():
                if hou.ui.displayMessage("防止意外,请保存工程?", buttons=("Yes", "No")) == 0:
                    hou.hipFile.save()
        self.ui.pb_progress.setMaximum(max)
        i = 1
        unsupported = []
        for mat in items:
            if mat.supported == 0:
                unsupported.append(mat)
                continue
            mat.create_thumbnail()
            self.ui.pb_progress.setValue(i)
            self.refresh_btnItems()
            QApplication.processEvents()
            i += 1
        time.sleep(1)
        self.ui.pb_progress.setHidden(1)
        if unsupported:
            hou.ui.displayMessage("有些材质暂不支持预览图生成", buttons=("OK",))

    def create_thumbnail_smart(self):
        mats = [item for item in self.filter_items.values() if item.thumbnail_status != 1]
        self.create_thumbnail(mats)

    @current_ids
    def create_thumbnail_force(self, ids):
        items = [self.filter_items.get(id) for id in ids if self.filter_items.get(id)]
        self.create_thumbnail(items)

    @current_item
    def item_custom_thumbnail(self, item):
        item.custom_thumbnail()

    @current_item
    def item_capture_thumbnail(self, item):
        item.capture_thumbnail()

    @current_ids
    def items_create_mat(self, ids):
        self.lib.items_create_mat(ids)

    @current_item
    def item_go_node(self, item):
        item.go_node()

    @current_ids
    def items_modify_mode(self, ids, index):
        self.lib.items_modify_mode(ids, index)
        self.refresh()

    @current_ids
    def items_modify_group(self, ids, group):
        current_group = self.cb_group.currentText()
        groups = self.lib.groups
        if group == None and current_group == groups[0]:
            return
        elif group == None and current_group == groups[-1]:
            self.lib.items_ignore(ids)
        else:
            self.lib.items_modify_group(ids, group)
        self.refresh()

    @current_ids
    def items_add_group(self, ids):

        result = hou.ui.readInput("新组名:", buttons=("OK", "Cancel"))
        if not result:
            return
        group = result[1]
        self.lib.items_modify_group(ids, group)
        self.refresh()

    @current_ids
    def items_del(self, ids):
        self.lib.items_del(ids)
        self.current_id = 0
        self.refresh()

    @current_ids
    def items_ignore(self, ids):
        self.lib.items_ignore(ids)
        self.refresh()

    @current_item
    def item_open_folder(self, item):
        item.open_folder()

    @current_ids
    def items_collect(self, ids, lib_name=None):
        self.lib.items_collect(ids, lib_name)

    @current_item
    def item_rename(self, item, btn_item):
        new_name = btn_item.text()
        if self.lib.lib_type == "Custom lib":
            item.rename(new_name)

    def show_ignore(self):
        self.current_id = 0
        self.refresh_btnItems()
        self.refresh_info()

    def solo_fav(self):
        self.current_id = 0
        self.refresh_btnItems()
        self.refresh_info()

    def go_obj_node(self):
        selItems = self.ui.lw_view.selectedItems()
        item = selItems[0]
        index = self.ui.lw_view.row(item)
        used_obj_list = self.mats[index].get_used_obj()
        if used_obj_list:
            level, node_path = used_obj_list[0]
            node = hou.node(node_path)
            node.setCurrent(True, clear_all_selected=True)

    def show_img(self):
        ex_path = self.assetsViewer.current_ex_path
        if not ex_path:
            return
        if self.img_viewer.isHidden():
            self.img_viewer.show()
        right_x = self.geometry().x() + self.width()
        right_y = self.geometry().y()
        height = self.height()
        self.img_viewer.setGeometry(right_x, right_y, height, height)
        self.img_viewer.refresh(ex_path)
        self.img_viewer.raise_()

    def del_unused(self):
        self.lib.del_unused()
        self.init_data()

    def info_doubleClicked(self):
        items = self.lw_info.selectedItems()
        if not items:
            return
        fun = items[0].data(QtCore.Qt.UserRole)
        if fun and hasattr(self, fun):
            getattr(self, fun)()

    def go_set(self):
        self.ui_set.main_show()

    def change_groups(self):
        self.group_index = self.cb_group.currentIndex()
        group = self.cb_group.currentText()
        self.lib.current_group = group
        self.refresh()

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
            display_status(f"Snail_error_mm: flip_info _ {e}")

    def updateMenu(self):

        self.ui.lw_menu1.clear()
        self.ui.lw_menu1.setIconSize(QtCore.QSize(40, 40))
        self.ui.lw_menu1.setGridSize(QtCore.QSize(70, 72))
        all_libs = {"Project": MYSET.lib_pj, **MYSET.libs}
        index = 0
        for one in all_libs.values():
            icon_num = one.get("icon")
            name = one.get("name")
            icon = QtGui.QIcon(f"{ALLSET.sbox_path}/file/icon02/{icon_num}.svg")
            item = QListWidgetItem(icon, "")
            item.setSizeHint(QtCore.QSize(70, 60))
            item.setText(name)
            item.setData(QtCore.Qt.UserRole, name)
            index += 1

            self.ui.lw_menu1.addItem(item)
        if len(all_libs) == 1:
            icon = QtGui.QIcon(f"{ALLSET.sbox_path}/file/icon02/10042.svg")
            item = QListWidgetItem(icon, "")
            item.setSizeHint(QtCore.QSize(70, 60))
            item.setText("Add lib")
            item.setData(QtCore.Qt.UserRole, "Add lib")
            self.ui.lw_menu1.addItem(item)
        self.ui.lw_menu1.setCurrentRow(0)

    def rightClickContext(self, position=None):
        menu = Snail_Menu()
        menu.aboutToHide.connect(self.start_timer)
        idx = self.ui.lw_view.selectedItems()
        if idx:
            if self.lib.lib_type != "GSG materials":
                submenu = Snail_Menu(self.tr_changeGroup)
                submenu.addAction(self.tr_addGroup, self.items_add_group)
                submenu.addAction(self.tr_removeGroup, lambda: self.items_modify_group(None))
                groups = self.lib.custom_groups[::-1]
                for group in groups:
                    submenu.addAction(
                        " " + group, lambda group=group: self.items_modify_group(group)
                    )
            else:
                submenu = None

            submenu2 = Snail_Menu(self.tr_mode)
            modes = [
                self.tr_modeA,
                self.tr_modeB,
                self.tr_modeC,
                self.tr_modeG,
                self.tr_modeL,
                self.tr_modeF,
                self.tr_modeAuto,
            ]

            for index, mode in enumerate(modes):
                submenu2.addAction(" " + mode, lambda index=index: self.items_modify_mode(index))

            submenu3 = Snail_Menu(self.tr_collect)
            libs = [name for name, lib in MYSET.libs.items() if lib.get("type") == "Custom lib"]

            for index, lib in enumerate(libs):
                submenu3.addAction(" " + lib, lambda index=index: self.items_collect(index))

            menu.addAction(self.tr_auto, self.create_thumbnail_force)
            menu.addAction(self.tr_capture, self.item_capture_thumbnail)
            menu.addAction(self.tr_custom, self.item_custom_thumbnail)
            menu.addMenu(submenu2)
            if submenu:
                menu.addMenu(submenu)
            if self.lib_name == "Project":
                menu.addAction(self.tr_goNode, self.item_go_node)
                menu.addAction(self.tr_usedObj, self.go_obj_node)
                menu.addMenu(submenu3)
            else:
                menu.addAction(self.tr_assetFolder, self.item_open_folder)
                menu.addAction(self.tr_createMat, self.items_create_mat)
            menu.addAction(self.tr_delItem, self.items_del)
            menu.addAction(self.tr_ignoreItem, self.items_ignore)
        else:
            menu.addAction(self.tr_refresh, self.init_data)
            menu.addAction(self.tr_createThumb, self.create_thumbnail_smart)
        menu.exec_(self.ui.lw_view.viewport().mapToGlobal(position))

    def toggle_language(self):
        ALLSET.toggle_language()
        self.load_language()

    def load_language(self):
        try:
            if ALLSET.language:
                self.translator.load(f"{ALLSET.sbox_path}/scripts/python/materialBox/tr_zh.pm")
            else:
                self.translator.load(f"{ALLSET.sbox_path}/scripts/python/materialBox/tr_en.pm")
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
            self.tb_folder.setToolTip(self.tr("Material folder"))
            self.tb_ignore.setToolTip(self.tr("Toggle show ignore"))
            self.tb_delete.setToolTip(self.tr("Delete item"))
            self.tb_fav.setToolTip(self.tr("Solo fav"))
            self.tb_flip.setToolTip(self.tr("Flip info"))
            self.tb_auto.setToolTip(self.tr("Auto create thumb"))
            self.tb_capture.setToolTip(self.tr("Capture thumb"))
            self.tb_custom.setToolTip(self.tr("Custom thumb"))
            self.tb_clear.setToolTip(self.tr("Clear unused material"))
            self.assetsViewer.tb_bigView.setToolTip(self.tr("Big view"))
            self.assetsViewer.tb_folder.setToolTip(self.tr("Assets folder"))

            self.tr_createThumb = self.tr("Create thumb")
            self.tr_assetFolder = self.tr("Assets folder")
            self.tr_delItem = self.tr("Delete")
            self.tr_ignoreItem = self.tr("Toggle ignore")
            self.tr_refresh = self.tr("Refresh")
            self.tr_createMat = self.tr("Create mat")
            self.tr_usedObj = self.tr("Go Used obj")
            self.tr_goNode = self.tr("Go mat node")
            self.tr_custom = self.tr("Custom thumb")
            self.tr_capture = self.tr("Capture thumb")
            self.tr_auto = self.tr("Auto thumb")
            self.tr_collect = self.tr("Collect to lib")
            self.tr_mode = self.tr("Thumb mode")
            self.tr_addGroup = self.tr("Add new group")
            self.tr_removeGroup = self.tr("Remove from group")
            self.tr_changeGroup = " " + self.tr("Change group")
            self.tr_modeA = self.tr("Half ball")
            self.tr_modeB = self.tr("All ball")
            self.tr_modeC = self.tr("Simple half")
            self.tr_modeG = self.tr("Glass")
            self.tr_modeL = self.tr("Liquid")
            self.tr_modeF = self.tr("Fabric")
            self.tr_modeAuto = self.tr("Auto")

        except Exception as e:
            display_status(f"Snail_error_mm: retranslateUi _ {e}")

    def start_timer(self):
        self.enter = 0
        self.timer_enter.start(1000)

    def stop_timer(self):
        self.enter = 1
        self.timer_enter.stop()

    def closeEvent(self, event):
        try:
            self.lib.update_lib_item()
            houMainWindow = hou.qt.mainWindow()
            getChildWin = houMainWindow.findChild(QGraphicsView, "Snail_imgViewer")
            if getChildWin:
                getChildWin.setVisible(False)
                super.closeEvent(event)
        except:
            super().closeEvent(event)

    def enterEvent(self, event):
        if self.enter and self.lib_name == "Project":
            self.check_mats_changed()
        super().enterEvent(event)


def main_show():
    try:
        houMainWindow = hou.qt.mainWindow()
        getChildWin = houMainWindow.findChild(QWidget, "Snail_MM")
        getChildWin.parent().close()
        getChildWin.parent().deleteLater()
    except:
        pass
    if not ALLSET.verify_sig("mm"):
        return
    MYSET.init_data()
    mywin2 = MM_Win()
    mywin2.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    mywin2.show()


def callInterface():
    panel = None
    pane_name = "SnailBox_materialManger"
    if not ALLSET.verify_sig("mm"):
        return
    MYSET.init_data()
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

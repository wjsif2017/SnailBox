import hou
from utils import *


class Ui_Main(QWidget):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self._manager = manager
        self._setup_ui()

    def _setup_ui(self):
        self.layout_main = QVBoxLayout(self)
        self.layout_main.setSpacing(0)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_main)

        self._create_settings_area()
        self._create_tool_bar()
        self._create_items_area()
        self._create_buttons_area()

        self._connect_internal_signals()
        self.refresh()

    def _create_settings_area(self):
        self.layout_settings = QHBoxLayout()
        self.layout_settings.setContentsMargins(4, 4, 4, 4)
        self.layout_settings.setSpacing(8)

        layout_settings_left = self._create_settings_controls()
        self.layout_settings.addLayout(layout_settings_left)

        self.layout_drop_zone = self._create_drop_zone()
        self.layout_settings.addLayout(self.layout_drop_zone)

        self.layout_main.addLayout(self.layout_settings)

    def _create_settings_controls(self):
        layout = QVBoxLayout()
        layout.setSpacing(2)

        self.label_comp_name = Snail_LabelA("C name")
        self.line_comp_name = Snail_LineEdit()
        self.label_comp_name.set_radius("left")
        self.line_comp_name.set_radius("right")
        layout_row1 = QHBoxLayout()
        layout_row1.addWidget(self.label_comp_name)
        layout_row1.addWidget(self.line_comp_name)
        layout.addLayout(layout_row1)

        self.label_res = Snail_LabelA("C size")
        self.line_res_x = Snail_IntLine()
        self.line_res_y = Snail_IntLine()
        self.label_res.set_radius("left")
        self.line_res_x.set_radius("none")
        self.line_res_y.set_radius("right")
        layout_row2 = QHBoxLayout()
        layout_row2.addWidget(self.label_res)
        layout_row2.addWidget(self.line_res_x)
        layout_row2.addWidget(self.line_res_y)
        layout.addLayout(layout_row2)

        self.label_f_range = Snail_LabelA("F range")
        self.line_f_start = Snail_IntLine()
        self.line_f_end = Snail_IntLine()
        self.label_f_range.set_radius("left")
        self.line_f_start.set_radius("none")
        self.line_f_end.set_radius("right")
        layout_row3 = QHBoxLayout()
        layout_row3.addWidget(self.label_f_range)
        layout_row3.addWidget(self.line_f_start)
        layout_row3.addWidget(self.line_f_end)
        layout.addLayout(layout_row3)

        layout_row4 = QHBoxLayout()

        self.label_fps = Snail_LabelA("F rate")
        self.line_fps = Snail_IntLine()
        self.line_fps.setDisabled(True)
        self.label_fps.set_radius("left")
        self.line_fps.set_radius("right")
        layout_row4.addWidget(self.label_fps)
        layout_row4.addWidget(self.line_fps)

        self.label_current = Snail_LabelA("Frame")
        self.line_f_current = Snail_LineEdit()
        self.label_current.set_radius("left")
        self.line_f_current.set_radius("right")
        layout_row4.addWidget(self.label_current)
        layout_row4.addWidget(self.line_f_current)

        layout.addLayout(layout_row4)

        return layout

    def _create_drop_zone(self):
        self.label_drop = Snail_DropLabel2(
            "Drag node here", self, "Drag node here", "node"
        )
        self.label_drop.setFixedWidth(140)
        self.label_drop.setFixedHeight(112)

        layout = QVBoxLayout()
        layout.addWidget(self.label_drop)
        layout.addStretch()

        return layout

    def _create_tool_bar(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(4, 0, 4, 4)
        layout.setSpacing(5)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self._create_tool_buttons()

        layout.addItem(spacer)
        layout.addWidget(self.tb_flipbook)
        self.layout_main.addLayout(layout)

    def _create_tool_buttons(self):
        self.tb_flipbook = Snail_IconBtn("snail_seq", "Export Flipbook")

    def _create_items_area(self):
        self.list_items = QListWidget(self)
        self.list_items.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.list_items.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        scrollbar = self.list_items.verticalScrollBar()
        scrollbar.setSingleStep(10)
        self.list_items.setSpacing(4)
        self.list_items.setStyleSheet(
            "QListWidget::Item {border: 2px solid rgb(30, 30, 30);border-radius: 5px;background-color: rgb(40, 40, 40);}"
            "QListWidget::Item:hover {background-color: rgb(100,100,100);}"
            "QListWidget::Item:selected {border: 1px solid rgb(255, 163, 32);}"
        )
        self.layout_main.addWidget(self.list_items, 1)

    def _create_buttons_area(self):
        self.layout_buttons_bar = QHBoxLayout()
        self.layout_buttons_bar.setContentsMargins(4, 4, 4, 4)

        self.tb_bz = Snail_IconBtn_bz()
        self.tb_help = Snail_IconBtn_help()
        self.layout_buttons_bar.addWidget(self.tb_bz)
        self.layout_buttons_bar.addWidget(self.tb_help)

        self.bt_refresh = Snail_Btn("Refresh")
        self.bt_to_ae = Snail_Btn("To Ae")
        self.bt_add_nodes = Snail_Btn("Add Nodes")
        self.layout_buttons_bar.addWidget(self.bt_refresh)
        self.layout_buttons_bar.addWidget(self.bt_to_ae)
        self.layout_buttons_bar.addWidget(self.bt_add_nodes)

        self.layout_main.addLayout(self.layout_buttons_bar)
        self.layout_main.addStretch(0)

    def refresh(self):
        self.line_comp_name.setText(self._manager.comp_name)
        self.line_res_x.setText(str(self._manager.res_x))
        self.line_res_y.setText(str(self._manager.res_y))
        self.line_f_start.setText(str(self._manager.f_start))
        self.line_f_end.setText(str(self._manager.f_end))
        self.line_f_current.setText(str(self._manager.f_current))
        self.line_fps.setText(str(self._manager.fps))

    def clear_item_list(self):
        if self.list_items:
            self.list_items.clear()

    def add_item_widget(self, widget):
        if not self.list_items:
            return

        item = QListWidgetItem("")
        item.setSizeHint(widget.sizeHint())
        self.list_items.addItem(item)
        self.list_items.setItemWidget(item, widget)

    def _connect_internal_signals(self):
        self.line_comp_name.editingFinished.connect(self._on_comp_name_changed)
        self.line_res_x.editingFinished.connect(self._on_res_x_changed)
        self.line_res_y.editingFinished.connect(self._on_res_y_changed)
        self.line_f_start.editingFinished.connect(self._on_f_start_changed)
        self.line_f_end.editingFinished.connect(self._on_f_end_changed)
        self.line_f_current.editingFinished.connect(self._on_f_current_changed)

        self.tb_flipbook.clicked.connect(self._on_flipbook_clicked)
        self.bt_add_nodes.clicked.connect(self._on_add_nodes_clicked)
        self.bt_to_ae.clicked.connect(self._on_to_ae_clicked)
        self.bt_refresh.clicked.connect(self._on_refresh_clicked)
        self.label_drop.dropped.connect(self._on_node_dropped)

    def _safe_int_update(self, line_edit, attr_name):
        try:
            value = int(line_edit.text())
            self._manager.update_config(**{attr_name: value})
        except ValueError:
            pass

    def _on_comp_name_changed(self):
        self._manager.update_config(comp_name=self.line_comp_name.text())

    def _on_res_x_changed(self):
        self._safe_int_update(self.line_res_x, "res_x")

    def _on_res_y_changed(self):
        self._safe_int_update(self.line_res_y, "res_y")

    def _on_f_start_changed(self):
        self._safe_int_update(self.line_f_start, "f_start")

    def _on_f_end_changed(self):
        self._safe_int_update(self.line_f_end, "f_end")

    def _on_f_current_changed(self):
        self._safe_int_update(self.line_f_current, "f_current")

    def _on_flipbook_clicked(self):
        self._manager.to_ae_preview()

    def _on_to_ae_clicked(self):
        self._manager.all_to_ae()

    def _on_refresh_clicked(self):
        self.parent.on_refresh_clicked()

    def _on_node_dropped(self, parm_path, node_path):
        self.parent.on_node_dropped(parm_path, node_path)

    def _on_add_nodes_clicked(self):
        selected_nodes = hou.selectedNodes()
        path_list = [node.path() for node in selected_nodes]
        self.parent.add_items(path_list)


class ItemWidget(QWidget):
    def __init__(self, item, parent=None):
        super().__init__(parent)
        self._item_id = item.id
        self._main_window = parent
        self._setup_ui()

    @property
    def item(self):
        return self._main_window.manager.get_item(self._item_id)

    def _setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(4)

        layout.addLayout(self._create_header())

        layout.addLayout(self._create_options())

        self.setLayout(layout)

        self.btn_close.clicked.connect(self._on_close_clicked)
        self.btn_toae.clicked.connect(self._on_toae_clicked)
        self.cb_static.toggled.connect(self._on_static_toggled)

    def _on_toae_clicked(self):
        self.item.to_ae()

    def _on_close_clicked(self):
        if self._main_window and hasattr(self._main_window, 'delete_item'):
            self._main_window.delete_item(self._item_id)

    def _on_static_toggled(self, checked):
        self.item.is_static = checked

    def _create_header(self):
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)

        label_name = Snail_LabelA("Node")
        label_name.set_radius("left")
        node_path = Snail_Btn2(self.item.node.type().icon(),self.item.node_path)
        node_path.set_radius("right")
        self.btn_toae = Snail_IconBtn("SnailAE")
        self.btn_close = Snail_IconBtn("BUTTONS_close")

        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(label_name)
        layout.addWidget(node_path)
        layout.addItem(spacer)
        layout.addWidget(self.btn_toae)
        layout.addWidget(self.btn_close)

        return layout

    def _create_options(self):
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        label_options = Snail_LabelA("Options")
        self.cb_static = Snail_CheckBox("Static")
        self.cb_static.set_radius("right")
        self.cb_static.setChecked(self.item.is_static)

        layout = QHBoxLayout()
        layout.addWidget(label_options)
        layout.addWidget(self.cb_static)
        layout.addItem(spacer)

        return layout

    def sizeHint(self):
        return QtCore.QSize(100, 66)


class ObjCamItemWidget(ItemWidget):
    def _setup_ui(self):
        self._create_components()

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(4, 4, 4, 4)
        layout_main.setSpacing(4)
        layout_main.addLayout(self._create_header())
        layout_main.addLayout(self._create_options_row_1())
        self._update_from_item()
        self.btn_close.clicked.connect(self._on_close_clicked)
        self.btn_toae.clicked.connect(self._on_toae_clicked)
        self.cb_static.toggled.connect(self._on_static_toggled)

        self.setLayout(layout_main)
        self._update_manager_resolution()

    def _update_manager_resolution(self):
        manager = self._main_window.manager
        if self.item.res_x != manager.res_x or self.item.res_y != manager.res_y:
            manager.update_config(res_x=self.item.res_x, res_y=self.item.res_y)
            self._main_window.ui.refresh()

    def _create_components(self):
        self.label_options = Snail_LabelA("Options")
        self.label_options.set_radius("left")

        self.cb_static = Snail_CheckBox("Static")
        self.cb_static.set_radius("right")


    def _update_from_item(self):
        item = self.item
        self.cb_static.setChecked(item.is_static)

    def _create_options_row_1(self):
        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(self.label_options)
        layout.addWidget(self.cb_static)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addItem(spacer)
        return layout

    def sizeHint(self):
        return QtCore.QSize(100, 66)


class ObjLightItemWidget(ItemWidget):
    def _setup_ui(self):
        self._create_components()

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(4, 4, 4, 4)
        layout_main.setSpacing(4)
        layout_main.addLayout(self._create_header())
        layout_main.addLayout(self._create_options())
        self._update_from_item()
        self._connect_signals()
        self.setLayout(layout_main)

    def _create_components(self):
        self.cb_static = Snail_CheckBox("Static")
        self.cb_static.set_radius("right")

        self.label_lightType = Snail_LabelA("Type", width=50)
        self.ra_point = Snail_RadioButton("Point")
        self.ra_point.set_radius("none")
        self.ra_spot = Snail_RadioButton("Spot")
        self.ra_spot.set_radius("none")
        self.ra_parallel = Snail_RadioButton("Parallel")
        self.ra_parallel.set_radius("right")

        self._button_group = QButtonGroup(self)
        self._button_group.addButton(self.ra_point)
        self._button_group.addButton(self.ra_spot)
        self._button_group.addButton(self.ra_parallel)

    def _update_from_item(self):
        self.cb_static.setChecked(self.item.is_static)
        if self.item.light_type == "OMNI":
            self.ra_point.setChecked(True)
        elif self.item.light_type == "SPOT":
            self.ra_spot.setChecked(True)
        else:
            self.ra_parallel.setChecked(True)

    def _connect_signals(self):
        self.btn_close.clicked.connect(self._on_close_clicked)
        self.btn_toae.clicked.connect(self._on_toae_clicked)
        self.cb_static.toggled.connect(self._on_static_toggled)
        self._button_group.buttonClicked.connect(self._on_light_type_changed)

    def _create_options(self):
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        label_options = Snail_LabelA("Options")
        label_options.set_radius("left")

        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(label_options)
        layout.addWidget(self.cb_static)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addItem(spacer)
        layout.addWidget(self.label_lightType)
        layout.addWidget(self.ra_point)
        layout.addWidget(self.ra_spot)
        layout.addWidget(self.ra_parallel)

        return layout

    def _on_light_type_changed(self, button):
        if button == self.ra_point:
            self.item.light_type = "OMNI"
        elif button == self.ra_spot:
            self.item.light_type = "SPOT"
        else:
            self.item.light_type = "PAR"

    def sizeHint(self):
        return QtCore.QSize(100, 66)


class ObjNullItemWidget(ItemWidget):
    def _setup_ui(self):
        self._create_components()

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(4, 4, 4, 4)
        layout_main.setSpacing(4)
        layout_main.addLayout(self._create_header())
        layout_main.addLayout(self._create_options_row_1())
        layout_main.addLayout(self._create_options_row_2())
        self._update_from_item()
        self._connect_signals()
        self._update_ui()
        self.setLayout(layout_main)

    def _create_components(self):
        self.cb_static = Snail_CheckBox("Static")
        self.cb_static.set_radius("right")

        self.label_layerType = Snail_LabelA("Type", width=50)
        self.ra_null = Snail_RadioButton("Null")
        self.ra_null.set_radius("none")
        self.ra_solid = Snail_RadioButton("Solid")
        self.ra_solid.set_radius("right")

        self._layer_type_group = QButtonGroup(self)
        self._layer_type_group.addButton(self.ra_null)
        self._layer_type_group.addButton(self.ra_solid)

        self.label_color = Snail_LabelA("Solid color", width=90)
        self.bt_color = Snail_ColorBtn()
        self.bt_color.set_radius("right")

        self.label_size = Snail_LabelA("Solid size")
        self.spin_sx = Snail_SpinBox("X  ", None, 0, 10000, 100)
        self.spin_sx.set_radius("none")
        self.spin_sx.setSingleStep(100)
        self.spin_sy = Snail_SpinBox("Y  ", None, 0, 10000, 100)
        self.spin_sy.set_radius("right")
        self.spin_sy.setSingleStep(100)

    def _update_from_item(self):
        self.cb_static.setChecked(self.item.is_static)
        if self.item.is_null:
            self.ra_null.setChecked(True)
        else:
            self.ra_solid.setChecked(True)

        c = self.item.color
        self.bt_color.changeColor([int(c[0]*255), int(c[1]*255), int(c[2]*255)])
        self.spin_sx.setValue(self.item.size_x)
        self.spin_sy.setValue(self.item.size_y)

    def _connect_signals(self):
        self.btn_close.clicked.connect(self._on_close_clicked)
        self.btn_toae.clicked.connect(self._on_toae_clicked)
        self.cb_static.toggled.connect(self._on_static_toggled)
        self._layer_type_group.buttonClicked.connect(self._on_layer_type_changed)
        self.bt_color.clicked.connect(self._on_color_clicked)
        self.spin_sx.valueChanged.connect(self._on_size_x_changed)
        self.spin_sy.valueChanged.connect(self._on_size_y_changed)

    def _update_ui(self):
        is_null = self.is_null_selected
        self.bt_color.setDisabled(is_null)
        self.spin_sx.setDisabled(is_null)
        self.spin_sy.setDisabled(is_null)

    def _create_options_row_1(self):
        label_options = Snail_LabelA("Options")
        label_options.set_radius("left")

        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(label_options)
        layout.addWidget(self.cb_static)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addWidget(self.label_layerType)
        layout.addWidget(self.ra_null)
        layout.addWidget(self.ra_solid)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addWidget(self.label_color)
        layout.addWidget(self.bt_color)


        return layout

    def _create_options_row_2(self):
        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(self.label_size)
        self.label_size.set_radius("left")
        layout.addWidget(self.spin_sx)
        self.spin_sx.set_radius("none")
        layout.addWidget(self.spin_sy)
        self.spin_sy.set_radius("right")
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        return layout

    def _on_layer_type_changed(self, button):
        is_null = (button == self.ra_null)
        self.item.is_null = is_null
        self._update_ui()

    def _on_color_clicked(self):
        rgb_255 = self.bt_color.changeColor(None)
        if rgb_255 is None:
            return
        self.item.color = [rgb_255[0] / 255.0, rgb_255[1] / 255.0, rgb_255[2] / 255.0]

    def _on_size_x_changed(self, value):
        self.item.size_x = value

    def _on_size_y_changed(self, value):
        self.item.size_y = value

    @property
    def is_null_selected(self):
        return self.ra_null.isChecked()

    def sizeHint(self):
        return QtCore.QSize(100,94)


class SopNullItemWidget(ItemWidget):
    def _setup_ui(self):
        self._create_components()

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(4, 4, 4, 4)
        layout_main.setSpacing(4)
        layout_main.addLayout(self._create_header())
        layout_main.addLayout(self._create_options_row_1())
        layout_main.addLayout(self._create_options_row_2())
        layout_main.addLayout(self._create_options_row_3())
        self._update_from_item()
        self._connect_signals()
        self._update_ui()
        self.setLayout(layout_main)

    def _get_max_index(self):
        try:
            node_path = self.item.node_path
            if not node_path:
                return 0
            geo = hou.node(node_path).geometry()
            prim_cont = geo.primCount()-1
            return prim_cont
        except:
            return 10000


    def _create_components(self):
        self.label_options = Snail_LabelA("Options")
        self.label_options.set_radius("left")

        self.cb_static = Snail_CheckBox("Static")
        self.cb_static.set_radius("right")

        self.label_class = Snail_LabelA("Class",width=50)
        self.ra_prim = Snail_RadioButton("Prim")
        self.ra_prim.set_radius("right")

        self.class_group = QButtonGroup(self)
        self.class_group.addButton(self.ra_prim,1)

        self.label_index = Snail_LabelA("Index", width=50)
        max_index = self._get_max_index()
        self.spin_index = Snail_SpinBox(None, None, 0, max_index, 60)
        self.spin_index.setValue(0)
        self.spin_index.set_radius("none")
        self.cb_all_index = Snail_CheckBox("All")
        self.cb_all_index.set_radius("right")
        self.cb_all_index.setChecked(True)

        self.label_layerType = Snail_LabelA("Type")
        self.ra_null = Snail_RadioButton("Null")
        self.ra_null.set_radius("none")
        self.ra_solid = Snail_RadioButton("Solid")
        self.ra_solid.set_radius("none")
        self.ra_mask = Snail_RadioButton("Mask")
        self.ra_mask.set_radius("right")

        self.layer_type_group = QButtonGroup(self)
        self.layer_type_group.addButton(self.ra_null,0)
        self.layer_type_group.addButton(self.ra_solid,1)
        self.layer_type_group.addButton(self.ra_mask,2)

        self.label_color = Snail_LabelA("Color", width=50)
        self.bt_color = Snail_ColorBtn()
        self.bt_color.set_radius("none")
        self.cb_random_color = Snail_CheckBox("Random")
        self.cb_random_color.set_radius("right")

        self.label_size = Snail_LabelA("Solid size")
        self.label_size.set_radius("left")
        self.spin_sx = Snail_SpinBox("X  ", None, 0, 10000, 100)
        self.spin_sx.set_radius("none")
        self.spin_sx.setSingleStep(100)
        self.spin_sy = Snail_SpinBox("Y  ", None, 0, 10000, 100)
        self.spin_sy.set_radius("none")
        self.spin_sy.setSingleStep(100)
        self.cb_auto_size = Snail_CheckBox("Auto")
        self.cb_auto_size.set_radius("right")

    def _connect_signals(self):
        self.btn_close.clicked.connect(self._on_close_clicked)
        self.btn_toae.clicked.connect(self._on_toae_clicked)
        self.cb_static.toggled.connect(self._on_static_toggled)
        self.bt_color.clicked.connect(self._on_color_clicked)
        self.layer_type_group.buttonClicked.connect(self._on_layer_type_changed)
        self.class_group.buttonClicked.connect(self._on_class_changed)
        self.cb_all_index.toggled.connect(self._on_all_index_toggled)
        self.cb_random_color.toggled.connect(self._on_random_color_toggled)
        self.cb_auto_size.toggled.connect(self._on_auto_size_toggled)
        self.spin_index.valueChanged.connect(self._on_index_changed)
        self.spin_sx.valueChanged.connect(self._on_size_x_changed)
        self.spin_sy.valueChanged.connect(self._on_size_y_changed)

    def _update_from_item(self):
        item = self.item
        self.cb_static.setChecked(item.is_static)
        class_index = item.SOP_CLASSES.index(item.sop_class)
        self.class_group.button(class_index).setChecked(True)
        layer_type_index = item.LAYER_TYPES.index(item.layer_type)
        self.layer_type_group.button(layer_type_index).setChecked(True)
        self.cb_all_index.setChecked(item.is_all_index)
        self.spin_index.setValue(item.index_value)
        c = item.color
        self.bt_color.changeColor([int(c[0]*255), int(c[1]*255), int(c[2]*255)])
        self.cb_random_color.setChecked(item.is_random_color)
        self.spin_sx.setValue(item.size_x)
        self.spin_sy.setValue(item.size_y)
        self.cb_auto_size.setChecked(item.is_auto_size)

    def _update_ui(self):
        is_null = self.ra_null.isChecked()
        is_mask = self.ra_mask.isChecked()
        is_all_index = self.cb_all_index.isChecked()
        is_random_color = self.cb_random_color.isChecked()
        is_auto_size = self.cb_auto_size.isChecked()

        self.bt_color.setDisabled(is_null or is_random_color)
        self.cb_random_color.setDisabled(is_null)
        self.cb_auto_size.setDisabled(is_null or is_mask)
        self.spin_index.setDisabled(is_all_index)
        self.spin_sx.setDisabled(is_auto_size)
        self.spin_sy.setDisabled(is_auto_size)

        if is_null:
            self.cb_random_color.setChecked(True)
            self.cb_auto_size.setChecked(True)
        elif is_mask:
            self.cb_auto_size.setChecked(True)

    def _create_options_row_1(self):


        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(self.label_options)
        layout.addWidget(self.cb_static)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addWidget(self.label_class)
        layout.addWidget(self.ra_prim)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addWidget(self.label_index)
        layout.addWidget(self.spin_index)
        layout.addWidget(self.cb_all_index)

        return layout

    def _create_options_row_2(self):
        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(self.label_layerType)
        layout.addWidget(self.ra_null)
        layout.addWidget(self.ra_solid)
        layout.addWidget(self.ra_mask)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addWidget(self.label_color)
        layout.addWidget(self.bt_color)
        layout.addWidget(self.cb_random_color)

        return layout

    def _create_options_row_3(self):
        layout = QHBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(self.label_size)
        layout.addWidget(self.spin_sx)
        layout.addWidget(self.spin_sy)
        layout.addWidget(self.cb_auto_size)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        return layout

    def _on_layer_type_changed(self, button):
        index = self.layer_type_group.checkedId()
        self.item.update_layer_type(index)
        self._update_ui()

    def _on_class_changed(self, button):
        index = self.class_group.checkedId()
        self.item.update_sop_class(index)

    def _on_all_index_toggled(self, checked):
        self.item.is_all_index = checked
        self._update_ui()

    def _on_random_color_toggled(self, checked):
        self.item.is_random_color = checked
        self._update_ui()

    def _on_auto_size_toggled(self, checked):
        self.item.is_auto_size = checked
        self._update_ui()

    def _on_index_changed(self, value):
        self.item.index_value = value

    def _on_size_x_changed(self, value):
        self.item.size_x = value

    def _on_size_y_changed(self, value):
        self.item.size_y = value

    def _on_color_clicked(self):
        rgb_255 = self.bt_color.changeColor(None)
        if rgb_255 is None:
            return

        self.item.color = [rgb_255[0] / 255.0, rgb_255[1] / 255.0, rgb_255[2] / 255.0]

    def sizeHint(self):
        return QtCore.QSize(100, 124)

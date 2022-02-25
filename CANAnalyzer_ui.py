# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CANAnalyzer_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 545)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 520))
        self.centralwidget.setMaximumSize(QtCore.QSize(3000, 1500))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CAN = QtWidgets.QTabWidget(self.centralwidget)
        self.CAN.setEnabled(True)
        self.CAN.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CAN.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.CAN.setAcceptDrops(False)
        self.CAN.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.CAN.setIconSize(QtCore.QSize(20, 20))
        self.CAN.setElideMode(QtCore.Qt.ElideRight)
        self.CAN.setObjectName("CAN")
        self.VMU = QtWidgets.QWidget()
        self.VMU.setObjectName("VMU")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.VMU)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.VMU_params_tab = QtWidgets.QTabWidget(self.VMU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VMU_params_tab.sizePolicy().hasHeightForWidth())
        self.VMU_params_tab.setSizePolicy(sizePolicy)
        self.VMU_params_tab.setObjectName("VMU_params_tab")
        self.often_used = QtWidgets.QWidget()
        self.often_used.setObjectName("often_used")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.often_used)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.vmu_param_table = QtWidgets.QTableWidget(self.often_used)
        self.vmu_param_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.vmu_param_table.setObjectName("vmu_param_table")
        self.vmu_param_table.setColumnCount(5)
        self.vmu_param_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.vmu_param_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vmu_param_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.vmu_param_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.vmu_param_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.vmu_param_table.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_11.addWidget(self.vmu_param_table)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.connect_vmu_btn = QtWidgets.QPushButton(self.often_used)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.connect_vmu_btn.setFont(font)
        self.connect_vmu_btn.setObjectName("connect_vmu_btn")
        self.verticalLayout_10.addWidget(self.connect_vmu_btn)
        self.constantly_req_vmu_params = QtWidgets.QCheckBox(self.often_used)
        self.constantly_req_vmu_params.setEnabled(False)
        self.constantly_req_vmu_params.setObjectName("constantly_req_vmu_params")
        self.verticalLayout_10.addWidget(self.constantly_req_vmu_params)
        self.label = QtWidgets.QLabel(self.often_used)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.response_time_edit = QtWidgets.QLineEdit(self.often_used)
        self.response_time_edit.setInputMask("")
        self.response_time_edit.setObjectName("response_time_edit")
        self.verticalLayout_10.addWidget(self.response_time_edit)
        self.start_record = QtWidgets.QPushButton(self.often_used)
        self.start_record.setEnabled(False)
        self.start_record.setObjectName("start_record")
        self.verticalLayout_10.addWidget(self.start_record)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.select_file_vmu_params = QtWidgets.QPushButton(self.often_used)
        self.select_file_vmu_params.setAcceptDrops(False)
        self.select_file_vmu_params.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.select_file_vmu_params.setCheckable(False)
        self.select_file_vmu_params.setAutoExclusive(False)
        self.select_file_vmu_params.setFlat(False)
        self.select_file_vmu_params.setObjectName("select_file_vmu_params")
        self.verticalLayout_10.addWidget(self.select_file_vmu_params)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.VMU_params_tab.addTab(self.often_used, "")
        self.verticalLayout_9.addWidget(self.VMU_params_tab)
        self.CAN.addTab(self.VMU, "")
        self.burr30 = QtWidgets.QWidget()
        self.burr30.setObjectName("burr30")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.burr30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tab_burr = QtWidgets.QTabWidget(self.burr30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_burr.sizePolicy().hasHeightForWidth())
        self.tab_burr.setSizePolicy(sizePolicy)
        self.tab_burr.setObjectName("tab_burr")
        self.all_params = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_params.sizePolicy().hasHeightForWidth())
        self.all_params.setSizePolicy(sizePolicy)
        self.all_params.setObjectName("all_params")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.all_params)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list_bookmark = QtWidgets.QListWidget(self.all_params)
        self.list_bookmark.setObjectName("list_bookmark")
        self.horizontalLayout.addWidget(self.list_bookmark)
        self.params_table = QtWidgets.QTableWidget(self.all_params)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.params_table.sizePolicy().hasHeightForWidth())
        self.params_table.setSizePolicy(sizePolicy)
        self.params_table.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.params_table.setGridStyle(QtCore.Qt.SolidLine)
        self.params_table.setColumnCount(5)
        self.params_table.setObjectName("params_table")
        self.params_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Name")
        item.setBackground(QtGui.QColor(245, 245, 245))
        self.params_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(245, 245, 245))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.params_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.params_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.params_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(245, 245, 245))
        self.params_table.setHorizontalHeaderItem(4, item)
        self.horizontalLayout.addWidget(self.params_table)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.tab_burr.addTab(self.all_params, "")
        self.editable_params = QtWidgets.QWidget()
        self.editable_params.setObjectName("editable_params")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.editable_params)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.load_file_button = QtWidgets.QPushButton(self.editable_params)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.load_file_button.setFont(font)
        self.load_file_button.setObjectName("load_file_button")
        self.horizontalLayout_4.addWidget(self.load_file_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.load_to_device_button = QtWidgets.QPushButton(self.editable_params)
        self.load_to_device_button.setEnabled(False)
        self.load_to_device_button.setObjectName("load_to_device_button")
        self.horizontalLayout_4.addWidget(self.load_to_device_button)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.params_table_2 = QtWidgets.QTableWidget(self.editable_params)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.params_table_2.sizePolicy().hasHeightForWidth())
        self.params_table_2.setSizePolicy(sizePolicy)
        self.params_table_2.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.params_table_2.setGridStyle(QtCore.Qt.SolidLine)
        self.params_table_2.setColumnCount(6)
        self.params_table_2.setObjectName("params_table_2")
        self.params_table_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Name")
        item.setBackground(QtGui.QColor(245, 245, 245))
        self.params_table_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(245, 245, 245))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.params_table_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.params_table_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.params_table_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.params_table_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(245, 245, 245))
        self.params_table_2.setHorizontalHeaderItem(5, item)
        self.verticalLayout_8.addWidget(self.params_table_2)
        self.verticalLayout_8.setStretch(1, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.tab_burr.addTab(self.editable_params, "")
        self.often_used_params = QtWidgets.QWidget()
        self.often_used_params.setObjectName("often_used_params")
        self.gridLayout = QtWidgets.QGridLayout(self.often_used_params)
        self.gridLayout.setObjectName("gridLayout")
        self.byte_order = QtWidgets.QGroupBox(self.often_used_params)
        self.byte_order.setEnabled(False)
        self.byte_order.setObjectName("byte_order")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.byte_order)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.rb_big_endian = QtWidgets.QRadioButton(self.byte_order)
        self.rb_big_endian.setChecked(True)
        self.rb_big_endian.setObjectName("rb_big_endian")
        self.verticalLayout_6.addWidget(self.rb_big_endian)
        self.rb_little_endian = QtWidgets.QRadioButton(self.byte_order)
        self.rb_little_endian.setObjectName("rb_little_endian")
        self.verticalLayout_6.addWidget(self.rb_little_endian)
        self.gridLayout.addWidget(self.byte_order, 2, 0, 1, 1)
        self.set_current_wheel = QtWidgets.QGroupBox(self.often_used_params)
        self.set_current_wheel.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.set_current_wheel.setFont(font)
        self.set_current_wheel.setObjectName("set_current_wheel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.set_current_wheel)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.factory_settings_rb = QtWidgets.QRadioButton(self.set_current_wheel)
        self.factory_settings_rb.setCheckable(True)
        self.factory_settings_rb.setChecked(True)
        self.factory_settings_rb.setAutoExclusive(False)
        self.factory_settings_rb.setObjectName("factory_settings_rb")
        self.verticalLayout_5.addWidget(self.factory_settings_rb)
        self.set_front_wheel_rb = QtWidgets.QRadioButton(self.set_current_wheel)
        self.set_front_wheel_rb.setChecked(False)
        self.set_front_wheel_rb.setObjectName("set_front_wheel_rb")
        self.verticalLayout_5.addWidget(self.set_front_wheel_rb)
        self.set_rear_wheel_rb = QtWidgets.QRadioButton(self.set_current_wheel)
        self.set_rear_wheel_rb.setChecked(False)
        self.set_rear_wheel_rb.setObjectName("set_rear_wheel_rb")
        self.verticalLayout_5.addWidget(self.set_rear_wheel_rb)
        self.gridLayout.addWidget(self.set_current_wheel, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        self.lb_soft_version = QtWidgets.QLabel(self.often_used_params)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_soft_version.setFont(font)
        self.lb_soft_version.setTextFormat(QtCore.Qt.RichText)
        self.lb_soft_version.setObjectName("lb_soft_version")
        self.gridLayout.addWidget(self.lb_soft_version, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.often_used_params)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.warn_temp = QtWidgets.QGroupBox(self.groupBox_4)
        self.warn_temp.setObjectName("warn_temp")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.warn_temp)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.warning_temperature = QtWidgets.QSlider(self.warn_temp)
        self.warning_temperature.setMinimum(20)
        self.warning_temperature.setMaximum(90)
        self.warning_temperature.setOrientation(QtCore.Qt.Horizontal)
        self.warning_temperature.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.warning_temperature.setObjectName("warning_temperature")
        self.horizontalLayout_9.addWidget(self.warning_temperature)
        self.lab_warning_temperature = QtWidgets.QLabel(self.warn_temp)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_warning_temperature.setFont(font)
        self.lab_warning_temperature.setText("")
        self.lab_warning_temperature.setObjectName("lab_warning_temperature")
        self.horizontalLayout_9.addWidget(self.lab_warning_temperature)
        self.verticalLayout_7.addWidget(self.warn_temp)
        self.zone = QtWidgets.QGroupBox(self.groupBox_4)
        self.zone.setObjectName("zone")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.zone)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.zone_of_insensitivity = QtWidgets.QSlider(self.zone)
        self.zone_of_insensitivity.setMinimum(1)
        self.zone_of_insensitivity.setMaximum(500)
        self.zone_of_insensitivity.setSingleStep(1)
        self.zone_of_insensitivity.setProperty("value", 1)
        self.zone_of_insensitivity.setOrientation(QtCore.Qt.Horizontal)
        self.zone_of_insensitivity.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.zone_of_insensitivity.setObjectName("zone_of_insensitivity")
        self.horizontalLayout_8.addWidget(self.zone_of_insensitivity)
        self.lab_zone_of_insensitivity = QtWidgets.QLabel(self.zone)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_zone_of_insensitivity.setFont(font)
        self.lab_zone_of_insensitivity.setText("")
        self.lab_zone_of_insensitivity.setObjectName("lab_zone_of_insensitivity")
        self.horizontalLayout_8.addWidget(self.lab_zone_of_insensitivity)
        self.verticalLayout_7.addWidget(self.zone)
        self.warn_curr = QtWidgets.QGroupBox(self.groupBox_4)
        self.warn_curr.setObjectName("warn_curr")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.warn_curr)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.warning_current = QtWidgets.QSlider(self.warn_curr)
        self.warning_current.setMinimum(10)
        self.warning_current.setMaximum(50)
        self.warning_current.setOrientation(QtCore.Qt.Horizontal)
        self.warning_current.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.warning_current.setTickInterval(1)
        self.warning_current.setObjectName("warning_current")
        self.horizontalLayout_7.addWidget(self.warning_current)
        self.lab_warning_current = QtWidgets.QLabel(self.warn_curr)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_warning_current.setFont(font)
        self.lab_warning_current.setText("")
        self.lab_warning_current.setObjectName("lab_warning_current")
        self.horizontalLayout_7.addWidget(self.lab_warning_current)
        self.verticalLayout_7.addWidget(self.warn_curr)
        self.cutoff = QtWidgets.QGroupBox(self.groupBox_4)
        self.cutoff.setObjectName("cutoff")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.cutoff)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cut_off_current = QtWidgets.QSlider(self.cutoff)
        self.cut_off_current.setMinimum(30)
        self.cut_off_current.setMaximum(70)
        self.cut_off_current.setOrientation(QtCore.Qt.Horizontal)
        self.cut_off_current.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.cut_off_current.setTickInterval(1)
        self.cut_off_current.setObjectName("cut_off_current")
        self.horizontalLayout_6.addWidget(self.cut_off_current)
        self.lab_cut_off_current = QtWidgets.QLabel(self.cutoff)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_cut_off_current.setFont(font)
        self.lab_cut_off_current.setText("")
        self.lab_cut_off_current.setObjectName("lab_cut_off_current")
        self.horizontalLayout_6.addWidget(self.lab_cut_off_current)
        self.verticalLayout_7.addWidget(self.cutoff)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 2, 1)
        self.lb_errors = QtWidgets.QLabel(self.often_used_params)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_errors.setFont(font)
        self.lb_errors.setObjectName("lb_errors")
        self.gridLayout.addWidget(self.lb_errors, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 5, 2, 2, 1)
        self.tb_errors = QtWidgets.QTextBrowser(self.often_used_params)
        self.tb_errors.setObjectName("tb_errors")
        self.gridLayout.addWidget(self.tb_errors, 1, 2, 3, 1)
        self.erase_err_btn = QtWidgets.QPushButton(self.often_used_params)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.erase_err_btn.setFont(font)
        self.erase_err_btn.setObjectName("erase_err_btn")
        self.gridLayout.addWidget(self.erase_err_btn, 4, 2, 1, 1)
        self.tab_burr.addTab(self.often_used_params, "")
        self.horizontalLayout_2.addWidget(self.tab_burr)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.burr30)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.burr30)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.groupBox = QtWidgets.QGroupBox(self.burr30)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 10)
        self.CAN.addTab(self.burr30, "")
        self.Wait_for_read = QtWidgets.QWidget()
        self.Wait_for_read.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Wait_for_read.sizePolicy().hasHeightForWidth())
        self.Wait_for_read.setSizePolicy(sizePolicy)
        self.Wait_for_read.setAutoFillBackground(False)
        self.Wait_for_read.setObjectName("Wait_for_read")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Wait_for_read)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.Wait_for_read)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.Wait_for_read)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.progressBar = QtWidgets.QProgressBar(self.Wait_for_read)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.CAN.addTab(self.Wait_for_read, "")
        self.gridLayout_2.addWidget(self.CAN, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.CAN.setCurrentIndex(1)
        self.VMU_params_tab.setCurrentIndex(0)
        self.tab_burr.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Настройка БУРР-30"))
        item = self.vmu_param_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Параметр"))
        item = self.vmu_param_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.vmu_param_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Адрес"))
        item = self.vmu_param_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Значение"))
        item = self.vmu_param_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Размерность"))
        self.connect_vmu_btn.setText(_translate("MainWindow", "Подключиться"))
        self.constantly_req_vmu_params.setText(_translate("MainWindow", "Постоянно"))
        self.label.setText(_translate("MainWindow", "Время опроса, мс"))
        self.start_record.setText(_translate("MainWindow", "Запись"))
        self.select_file_vmu_params.setText(_translate("MainWindow", "Выбрать файл  \n"
" с параметрами для записи"))
        self.VMU_params_tab.setTabText(self.VMU_params_tab.indexOf(self.often_used), _translate("MainWindow", "Для записи"))
        self.CAN.setTabText(self.CAN.indexOf(self.VMU), _translate("MainWindow", "VMU"))
        item = self.params_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.params_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.params_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Value"))
        item = self.params_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Unit"))
        self.tab_burr.setTabText(self.tab_burr.indexOf(self.all_params), _translate("MainWindow", "По разделам"))
        self.load_file_button.setText(_translate("MainWindow", "Загрузить файл с настройками"))
        self.load_to_device_button.setText(_translate("MainWindow", "Загрузить настройки в устройство"))
        item = self.params_table_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.params_table_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Adress"))
        item = self.params_table_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Value from device"))
        item = self.params_table_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Value from file"))
        item = self.params_table_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Unit"))
        self.tab_burr.setTabText(self.tab_burr.indexOf(self.editable_params), _translate("MainWindow", "Настраиваемые"))
        self.byte_order.setTitle(_translate("MainWindow", "Порядок байт"))
        self.rb_big_endian.setText(_translate("MainWindow", "big-endian \n"
" прямой"))
        self.rb_little_endian.setText(_translate("MainWindow", "little-endian\n"
"обратный"))
        self.set_current_wheel.setTitle(_translate("MainWindow", "Установить ось"))
        self.factory_settings_rb.setText(_translate("MainWindow", "Заводская\n"
"настройка"))
        self.set_front_wheel_rb.setText(_translate("MainWindow", "Передняя"))
        self.set_rear_wheel_rb.setText(_translate("MainWindow", "Задняя"))
        self.lb_soft_version.setText(_translate("MainWindow", "Версия ПО БУРР"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Частые настройки"))
        self.warn_temp.setTitle(_translate("MainWindow", "Температура предупреждения - Аварийная"))
        self.zone.setTitle(_translate("MainWindow", "Зона нечувствительности рейки"))
        self.warn_curr.setTitle(_translate("MainWindow", "Ток предупреждения - Аварийный"))
        self.cutoff.setTitle(_translate("MainWindow", "Ток отсечки"))
        self.lb_errors.setText(_translate("MainWindow", "Ошибки"))
        self.erase_err_btn.setText(_translate("MainWindow", "Сбросить ошибки"))
        self.tab_burr.setTabText(self.tab_burr.indexOf(self.often_used_params), _translate("MainWindow", "Часто используемые"))
        self.pushButton_2.setText(_translate("MainWindow", "Подключиться"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить \n"
"  из БУРР-30\n"
" в файл"))
        self.groupBox.setTitle(_translate("MainWindow", "Ось"))
        self.radioButton_2.setText(_translate("MainWindow", "Задняя"))
        self.radioButton.setText(_translate("MainWindow", "Передняя"))
        self.CAN.setTabText(self.CAN.indexOf(self.burr30), _translate("MainWindow", "БУРР-30"))
        self.label_2.setText(_translate("MainWindow", "Немного терпения"))
        self.label_3.setText(_translate("MainWindow", "Скоро всё загрузится"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 819)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.pushButton_editUserInfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_editUserInfo.setObjectName("pushButton_editUserInfo")
        self.gridLayout_5.addWidget(self.pushButton_editUserInfo, 0, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 7, 1, 1)
        self.pushButton_editSampleInfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_editSampleInfo.setObjectName("pushButton_editSampleInfo")
        self.gridLayout_5.addWidget(self.pushButton_editSampleInfo, 0, 9, 1, 1)
        self.dev_meas_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.dev_meas_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.dev_meas_splitter.setObjectName("dev_meas_splitter")
        self.devices_main_widget = QtWidgets.QWidget(self.dev_meas_splitter)
        self.devices_main_widget.setObjectName("devices_main_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.devices_main_widget)
        self.gridLayout.setContentsMargins(9, 0, 9, 9)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.devices_main_widget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 2)
        self.devices_widget = QtWidgets.QWidget(self.devices_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.devices_widget.sizePolicy().hasHeightForWidth())
        self.devices_widget.setSizePolicy(sizePolicy)
        self.devices_widget.setMinimumSize(QtCore.QSize(0, 300))
        self.devices_widget.setObjectName("devices_widget")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.devices_widget)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.devices_splitter = QtWidgets.QSplitter(self.devices_widget)
        self.devices_splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.devices_splitter.setLineWidth(8)
        self.devices_splitter.setMidLineWidth(8)
        self.devices_splitter.setOrientation(QtCore.Qt.Vertical)
        self.devices_splitter.setOpaqueResize(True)
        self.devices_splitter.setHandleWidth(5)
        self.devices_splitter.setObjectName("devices_splitter")
        self.device_list_widget = QtWidgets.QWidget(self.devices_splitter)
        self.device_list_widget.setMinimumSize(QtCore.QSize(0, 200))
        self.device_list_widget.setObjectName("device_list_widget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.device_list_widget)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_add_device = QtWidgets.QPushButton(self.device_list_widget)
        self.pushButton_add_device.setMinimumSize(QtCore.QSize(30, 23))
        self.pushButton_add_device.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_add_device.setObjectName("pushButton_add_device")
        self.gridLayout_11.addWidget(self.pushButton_add_device, 0, 1, 1, 1)
        self.lineEdit_device_search = QtWidgets.QLineEdit(self.device_list_widget)
        self.lineEdit_device_search.setObjectName("lineEdit_device_search")
        self.gridLayout_11.addWidget(self.lineEdit_device_search, 0, 0, 1, 1)
        self.pushButton_remove_device = QtWidgets.QPushButton(self.device_list_widget)
        self.pushButton_remove_device.setMinimumSize(QtCore.QSize(30, 23))
        self.pushButton_remove_device.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_remove_device.setObjectName("pushButton_remove_device")
        self.gridLayout_11.addWidget(self.pushButton_remove_device, 0, 2, 1, 1)
        self.treeView_devices = QtWidgets.QTreeView(self.device_list_widget)
        self.treeView_devices.setObjectName("treeView_devices")
        self.gridLayout_11.addWidget(self.treeView_devices, 3, 0, 2, 3)
        self.device_epics_widget = QtWidgets.QWidget(self.devices_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_epics_widget.sizePolicy().hasHeightForWidth())
        self.device_epics_widget.setSizePolicy(sizePolicy)
        self.device_epics_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.device_epics_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.device_epics_widget.setObjectName("device_epics_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.device_epics_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_make_EPICS_environment = QtWidgets.QPushButton(self.device_epics_widget)
        self.pushButton_make_EPICS_environment.setObjectName("pushButton_make_EPICS_environment")
        self.gridLayout_2.addWidget(self.pushButton_make_EPICS_environment, 0, 0, 1, 1)
        self.textEdit_console_output = QtWidgets.QTextEdit(self.device_epics_widget)
        self.textEdit_console_output.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_console_output.setObjectName("textEdit_console_output")
        self.gridLayout_2.addWidget(self.textEdit_console_output, 5, 0, 1, 3)
        self.pushButton_run_ioc = QtWidgets.QPushButton(self.device_epics_widget)
        self.pushButton_run_ioc.setObjectName("pushButton_run_ioc")
        self.gridLayout_2.addWidget(self.pushButton_run_ioc, 1, 0, 1, 1)
        self.progressBar_devices = QtWidgets.QProgressBar(self.device_epics_widget)
        self.progressBar_devices.setEnabled(True)
        self.progressBar_devices.setProperty("value", 0)
        self.progressBar_devices.setObjectName("progressBar_devices")
        self.gridLayout_2.addWidget(self.progressBar_devices, 0, 1, 1, 1)
        self.checkBox_ioc_running = QtWidgets.QCheckBox(self.device_epics_widget)
        self.checkBox_ioc_running.setEnabled(False)
        self.checkBox_ioc_running.setCheckable(True)
        self.checkBox_ioc_running.setObjectName("checkBox_ioc_running")
        self.gridLayout_2.addWidget(self.checkBox_ioc_running, 1, 1, 1, 1)
        self.lineEdit_send_to_IOC = QtWidgets.QLineEdit(self.device_epics_widget)
        self.lineEdit_send_to_IOC.setEnabled(False)
        self.lineEdit_send_to_IOC.setObjectName("lineEdit_send_to_IOC")
        self.gridLayout_2.addWidget(self.lineEdit_send_to_IOC, 3, 0, 1, 1)
        self.pushButton_write_to_console = QtWidgets.QPushButton(self.device_epics_widget)
        self.pushButton_write_to_console.setEnabled(False)
        self.pushButton_write_to_console.setObjectName("pushButton_write_to_console")
        self.gridLayout_2.addWidget(self.pushButton_write_to_console, 3, 1, 1, 1)
        self.pushButton_show_console_output = QtWidgets.QPushButton(self.device_epics_widget)
        self.pushButton_show_console_output.setObjectName("pushButton_show_console_output")
        self.gridLayout_2.addWidget(self.pushButton_show_console_output, 2, 0, 1, 1)
        self.pushButton_clear_EPICS_output = QtWidgets.QPushButton(self.device_epics_widget)
        self.pushButton_clear_EPICS_output.setObjectName("pushButton_clear_EPICS_output")
        self.gridLayout_2.addWidget(self.pushButton_clear_EPICS_output, 2, 1, 1, 1)
        self.device_config_widget = QtWidgets.QWidget(self.devices_splitter)
        self.device_config_widget.setObjectName("device_config_widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.device_config_widget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_12.addWidget(self.devices_splitter, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.devices_widget, 2, 0, 1, 2)
        self.meas_main_widget = QtWidgets.QWidget(self.dev_meas_splitter)
        self.meas_main_widget.setObjectName("meas_main_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.meas_main_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.meas_widget = QtWidgets.QWidget(self.meas_main_widget)
        self.meas_widget.setObjectName("meas_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.meas_widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.meas_splitter = QtWidgets.QSplitter(self.meas_widget)
        self.meas_splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.meas_splitter.setLineWidth(10)
        self.meas_splitter.setMidLineWidth(10)
        self.meas_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.meas_splitter.setObjectName("meas_splitter")
        self.protocols_main_widget = QtWidgets.QWidget(self.meas_splitter)
        self.protocols_main_widget.setObjectName("protocols_main_widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.protocols_main_widget)
        self.gridLayout_6.setContentsMargins(9, 0, 9, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.protocols_widget = QtWidgets.QWidget(self.protocols_main_widget)
        self.protocols_widget.setObjectName("protocols_widget")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.protocols_widget)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.protocols_splitter = QtWidgets.QSplitter(self.protocols_widget)
        self.protocols_splitter.setOrientation(QtCore.Qt.Vertical)
        self.protocols_splitter.setObjectName("protocols_splitter")
        self.protocols_list_widget = QtWidgets.QWidget(self.protocols_splitter)
        self.protocols_list_widget.setObjectName("protocols_list_widget")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.protocols_list_widget)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.pushButton_add_protocol = QtWidgets.QPushButton(self.protocols_list_widget)
        self.pushButton_add_protocol.setMinimumSize(QtCore.QSize(30, 23))
        self.pushButton_add_protocol.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_add_protocol.setObjectName("pushButton_add_protocol")
        self.gridLayout_13.addWidget(self.pushButton_add_protocol, 0, 1, 1, 1)
        self.pushButton_remove_protocol = QtWidgets.QPushButton(self.protocols_list_widget)
        self.pushButton_remove_protocol.setMinimumSize(QtCore.QSize(30, 23))
        self.pushButton_remove_protocol.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_remove_protocol.setObjectName("pushButton_remove_protocol")
        self.gridLayout_13.addWidget(self.pushButton_remove_protocol, 0, 2, 1, 1)
        self.lineEdit_protocol_search = QtWidgets.QLineEdit(self.protocols_list_widget)
        self.lineEdit_protocol_search.setObjectName("lineEdit_protocol_search")
        self.gridLayout_13.addWidget(self.lineEdit_protocol_search, 0, 0, 1, 1)
        self.listView_protocols = QtWidgets.QListView(self.protocols_list_widget)
        self.listView_protocols.setObjectName("listView_protocols")
        self.gridLayout_13.addWidget(self.listView_protocols, 1, 0, 1, 3)
        self.protocols_build_widget = QtWidgets.QWidget(self.protocols_splitter)
        self.protocols_build_widget.setObjectName("protocols_build_widget")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.protocols_build_widget)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.pushButton_build_protocol = QtWidgets.QPushButton(self.protocols_build_widget)
        self.pushButton_build_protocol.setObjectName("pushButton_build_protocol")
        self.gridLayout_14.addWidget(self.pushButton_build_protocol, 0, 0, 1, 1)
        self.pushButton_show_output_meas = QtWidgets.QPushButton(self.protocols_build_widget)
        self.pushButton_show_output_meas.setObjectName("pushButton_show_output_meas")
        self.gridLayout_14.addWidget(self.pushButton_show_output_meas, 2, 0, 1, 1)
        self.progressBar_protocols = QtWidgets.QProgressBar(self.protocols_build_widget)
        self.progressBar_protocols.setProperty("value", 0)
        self.progressBar_protocols.setObjectName("progressBar_protocols")
        self.gridLayout_14.addWidget(self.progressBar_protocols, 1, 0, 1, 2)
        self.pushButton_open_protocol_external = QtWidgets.QPushButton(self.protocols_build_widget)
        self.pushButton_open_protocol_external.setObjectName("pushButton_open_protocol_external")
        self.gridLayout_14.addWidget(self.pushButton_open_protocol_external, 0, 1, 1, 1)
        self.pushButton_clear_output_meas = QtWidgets.QPushButton(self.protocols_build_widget)
        self.pushButton_clear_output_meas.setObjectName("pushButton_clear_output_meas")
        self.gridLayout_14.addWidget(self.pushButton_clear_output_meas, 2, 1, 1, 1)
        self.textEdit_console_output_meas = QtWidgets.QTextEdit(self.protocols_build_widget)
        self.textEdit_console_output_meas.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_console_output_meas.setObjectName("textEdit_console_output_meas")
        self.gridLayout_14.addWidget(self.textEdit_console_output_meas, 3, 0, 1, 2)
        self.gridLayout_15.addWidget(self.protocols_splitter, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.protocols_widget, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.protocols_main_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton_run_protocol = QtWidgets.QPushButton(self.protocols_main_widget)
        self.pushButton_run_protocol.setObjectName("pushButton_run_protocol")
        self.gridLayout_6.addWidget(self.pushButton_run_protocol, 1, 0, 1, 1)
        self.sequence_main_widget = QtWidgets.QWidget(self.meas_splitter)
        self.sequence_main_widget.setObjectName("sequence_main_widget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.sequence_main_widget)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_move_step_out = QtWidgets.QPushButton(self.sequence_main_widget)
        self.pushButton_move_step_out.setObjectName("pushButton_move_step_out")
        self.gridLayout_8.addWidget(self.pushButton_move_step_out, 4, 1, 1, 1)
        self.pushButton_move_step_in = QtWidgets.QPushButton(self.sequence_main_widget)
        self.pushButton_move_step_in.setObjectName("pushButton_move_step_in")
        self.gridLayout_8.addWidget(self.pushButton_move_step_in, 3, 1, 1, 1)
        self.pushButton_move_step_up = QtWidgets.QPushButton(self.sequence_main_widget)
        self.pushButton_move_step_up.setObjectName("pushButton_move_step_up")
        self.gridLayout_8.addWidget(self.pushButton_move_step_up, 3, 0, 1, 1)
        self.pushButton_move_step_down = QtWidgets.QPushButton(self.sequence_main_widget)
        self.pushButton_move_step_down.setObjectName("pushButton_move_step_down")
        self.gridLayout_8.addWidget(self.pushButton_move_step_down, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.sequence_main_widget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)
        self.treeView_protocol_sequence = QtWidgets.QTreeView(self.sequence_main_widget)
        self.treeView_protocol_sequence.setObjectName("treeView_protocol_sequence")
        self.gridLayout_8.addWidget(self.treeView_protocol_sequence, 6, 0, 1, 3)
        self.pushButton_show_protocol_settings = QtWidgets.QPushButton(self.sequence_main_widget)
        self.pushButton_show_protocol_settings.setObjectName("pushButton_show_protocol_settings")
        self.gridLayout_8.addWidget(self.pushButton_show_protocol_settings, 1, 0, 1, 3)
        self.toolButton_add_step = QtWidgets.QToolButton(self.sequence_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_add_step.sizePolicy().hasHeightForWidth())
        self.toolButton_add_step.setSizePolicy(sizePolicy)
        self.toolButton_add_step.setMinimumSize(QtCore.QSize(30, 23))
        self.toolButton_add_step.setMaximumSize(QtCore.QSize(30, 16777215))
        self.toolButton_add_step.setObjectName("toolButton_add_step")
        self.gridLayout_8.addWidget(self.toolButton_add_step, 3, 2, 1, 1)
        self.pushButton_remove_step = QtWidgets.QPushButton(self.sequence_main_widget)
        self.pushButton_remove_step.setMinimumSize(QtCore.QSize(30, 23))
        self.pushButton_remove_step.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_remove_step.setObjectName("pushButton_remove_step")
        self.gridLayout_8.addWidget(self.pushButton_remove_step, 4, 2, 1, 1)
        self.configuration_main_widget = QtWidgets.QWidget(self.meas_splitter)
        self.configuration_main_widget.setObjectName("configuration_main_widget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.configuration_main_widget)
        self.gridLayout_9.setContentsMargins(0, 0, 9, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_5 = QtWidgets.QLabel(self.configuration_main_widget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)
        self.loopstep_configuration_widget = QtWidgets.QWidget(self.configuration_main_widget)
        self.loopstep_configuration_widget.setObjectName("loopstep_configuration_widget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.loopstep_configuration_widget)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9.addWidget(self.loopstep_configuration_widget, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.meas_splitter, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.meas_widget, 0, 0, 1, 2)
        self.gridLayout_5.addWidget(self.dev_meas_splitter, 1, 0, 1, 10)
        self.comboBox_sample = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_sample.setObjectName("comboBox_sample")
        self.gridLayout_5.addWidget(self.comboBox_sample, 0, 8, 1, 1)
        self.comboBox_user = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_user.setObjectName("comboBox_user")
        self.gridLayout_5.addWidget(self.comboBox_user, 0, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 0, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 3, 1, 1)
        self.comboBox_preset = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_preset.setObjectName("comboBox_preset")
        self.gridLayout_5.addWidget(self.comboBox_preset, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPresets = QtWidgets.QAction(MainWindow)
        self.actionPresets.setObjectName("actionPresets")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionSave_Device_Preset_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Device_Preset_As.setObjectName("actionSave_Device_Preset_As")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionMeasurement_Presets = QtWidgets.QAction(MainWindow)
        self.actionMeasurement_Presets.setObjectName("actionMeasurement_Presets")
        self.actionSave_Preset = QtWidgets.QAction(MainWindow)
        self.actionSave_Preset.setObjectName("actionSave_Preset")
        self.actionOpen_Backup_Device_Preset = QtWidgets.QAction(MainWindow)
        self.actionOpen_Backup_Device_Preset.setObjectName("actionOpen_Backup_Device_Preset")
        self.actionLoad_Backup_Preset = QtWidgets.QAction(MainWindow)
        self.actionLoad_Backup_Preset.setObjectName("actionLoad_Backup_Preset")
        self.actionAutosave_on_closing = QtWidgets.QAction(MainWindow)
        self.actionAutosave_on_closing.setCheckable(True)
        self.actionAutosave_on_closing.setObjectName("actionAutosave_on_closing")
        self.actionDevice_Driver_Builder = QtWidgets.QAction(MainWindow)
        self.actionDevice_Driver_Builder.setObjectName("actionDevice_Driver_Builder")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setCheckable(True)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionIOC_Builder = QtWidgets.QAction(MainWindow)
        self.actionIOC_Builder.setObjectName("actionIOC_Builder")
        self.actionNew_Device_Preset_2 = QtWidgets.QAction(MainWindow)
        self.actionNew_Device_Preset_2.setObjectName("actionNew_Device_Preset_2")
        self.actionSave_Device_Preset = QtWidgets.QAction(MainWindow)
        self.actionSave_Device_Preset.setObjectName("actionSave_Device_Preset")
        self.actionSave_Preset_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Preset_As.setObjectName("actionSave_Preset_As")
        self.actionNew_Preset = QtWidgets.QAction(MainWindow)
        self.actionNew_Preset.setObjectName("actionNew_Preset")
        self.actionNew_Device_Preset = QtWidgets.QAction(MainWindow)
        self.actionNew_Device_Preset.setObjectName("actionNew_Device_Preset")
        self.menuFile.addAction(self.actionNew_Preset)
        self.menuFile.addAction(self.actionSave_Preset)
        self.menuFile.addAction(self.actionSave_Preset_As)
        self.menuFile.addAction(self.actionLoad_Backup_Preset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuPreferences.addAction(self.actionUndo)
        self.menuPreferences.addAction(self.actionRedo)
        self.menuPreferences.addSeparator()
        self.menuTools.addAction(self.actionDevice_Driver_Builder)
        self.menuTools.addAction(self.actionIOC_Builder)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_device_search, self.pushButton_add_device)
        MainWindow.setTabOrder(self.pushButton_add_device, self.pushButton_remove_device)
        MainWindow.setTabOrder(self.pushButton_remove_device, self.treeView_devices)
        MainWindow.setTabOrder(self.treeView_devices, self.pushButton_make_EPICS_environment)
        MainWindow.setTabOrder(self.pushButton_make_EPICS_environment, self.textEdit_console_output)
        MainWindow.setTabOrder(self.textEdit_console_output, self.pushButton_run_protocol)
        MainWindow.setTabOrder(self.pushButton_run_protocol, self.lineEdit_protocol_search)
        MainWindow.setTabOrder(self.lineEdit_protocol_search, self.pushButton_add_protocol)
        MainWindow.setTabOrder(self.pushButton_add_protocol, self.pushButton_remove_protocol)
        MainWindow.setTabOrder(self.pushButton_remove_protocol, self.listView_protocols)
        MainWindow.setTabOrder(self.listView_protocols, self.pushButton_build_protocol)
        MainWindow.setTabOrder(self.pushButton_build_protocol, self.textEdit_console_output_meas)
        MainWindow.setTabOrder(self.textEdit_console_output_meas, self.pushButton_show_protocol_settings)
        MainWindow.setTabOrder(self.pushButton_show_protocol_settings, self.pushButton_move_step_up)
        MainWindow.setTabOrder(self.pushButton_move_step_up, self.pushButton_move_step_in)
        MainWindow.setTabOrder(self.pushButton_move_step_in, self.pushButton_move_step_down)
        MainWindow.setTabOrder(self.pushButton_move_step_down, self.pushButton_move_step_out)
        MainWindow.setTabOrder(self.pushButton_move_step_out, self.toolButton_add_step)
        MainWindow.setTabOrder(self.toolButton_add_step, self.pushButton_remove_step)
        MainWindow.setTabOrder(self.pushButton_remove_step, self.treeView_protocol_sequence)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Preset:"))
        self.pushButton_editUserInfo.setText(_translate("MainWindow", "Edit User-Information"))
        self.label_8.setText(_translate("MainWindow", "Sample:"))
        self.pushButton_editSampleInfo.setText(_translate("MainWindow", "Edit Sample-Information"))
        self.label_6.setText(_translate("MainWindow", "Devices"))
        self.pushButton_add_device.setText(_translate("MainWindow", "+"))
        self.lineEdit_device_search.setPlaceholderText(_translate("MainWindow", "Search"))
        self.pushButton_remove_device.setText(_translate("MainWindow", "-"))
        self.pushButton_make_EPICS_environment.setText(_translate("MainWindow", "Make EPICS IOC"))
        self.pushButton_run_ioc.setText(_translate("MainWindow", "Run IOC"))
        self.checkBox_ioc_running.setText(_translate("MainWindow", "not running"))
        self.pushButton_write_to_console.setText(_translate("MainWindow", "Write to console"))
        self.pushButton_show_console_output.setText(_translate("MainWindow", "Hide output"))
        self.pushButton_clear_EPICS_output.setText(_translate("MainWindow", "Clear output"))
        self.pushButton_add_protocol.setText(_translate("MainWindow", "+"))
        self.pushButton_remove_protocol.setText(_translate("MainWindow", "-"))
        self.lineEdit_protocol_search.setPlaceholderText(_translate("MainWindow", "Search"))
        self.pushButton_build_protocol.setText(_translate("MainWindow", "Build Protocol"))
        self.pushButton_show_output_meas.setText(_translate("MainWindow", "Hide output"))
        self.pushButton_open_protocol_external.setText(_translate("MainWindow", "Open Protocol externally"))
        self.pushButton_clear_output_meas.setText(_translate("MainWindow", "Clear output"))
        self.label_3.setText(_translate("MainWindow", "Protocols"))
        self.pushButton_run_protocol.setText(_translate("MainWindow", "Build and run selected protocol"))
        self.pushButton_move_step_out.setText(_translate("MainWindow", "move out"))
        self.pushButton_move_step_in.setText(_translate("MainWindow", "move in"))
        self.pushButton_move_step_up.setText(_translate("MainWindow", "move up"))
        self.pushButton_move_step_down.setText(_translate("MainWindow", "move down"))
        self.label_4.setText(_translate("MainWindow", "Sequence"))
        self.pushButton_show_protocol_settings.setText(_translate("MainWindow", "Protocol Configuration"))
        self.toolButton_add_step.setText(_translate("MainWindow", "+"))
        self.pushButton_remove_step.setText(_translate("MainWindow", "-"))
        self.label_5.setText(_translate("MainWindow", "Configuration"))
        self.label.setText(_translate("MainWindow", "User:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionPresets.setText(_translate("MainWindow", "Device-Presets"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionSave_Device_Preset_As.setText(_translate("MainWindow", "Save Device Preset As"))
        self.actionLoad.setText(_translate("MainWindow", "Open"))
        self.actionMeasurement_Presets.setText(_translate("MainWindow", "Measurement-Presets"))
        self.actionSave_Preset.setText(_translate("MainWindow", "Save Preset"))
        self.actionOpen_Backup_Device_Preset.setText(_translate("MainWindow", "Load Backup Device Preset"))
        self.actionLoad_Backup_Preset.setText(_translate("MainWindow", "Load Backup Preset"))
        self.actionAutosave_on_closing.setText(_translate("MainWindow", "Autosave on closing"))
        self.actionDevice_Driver_Builder.setText(_translate("MainWindow", "Device Driver Builder"))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionUndo.setText(_translate("MainWindow", "Undo (ctrl + z)"))
        self.actionRedo.setText(_translate("MainWindow", "Redo (ctrl + y)"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionIOC_Builder.setText(_translate("MainWindow", "IOC-Builder"))
        self.actionNew_Device_Preset_2.setText(_translate("MainWindow", "New Device Preset"))
        self.actionSave_Device_Preset.setText(_translate("MainWindow", "Save Device Preset"))
        self.actionSave_Preset_As.setText(_translate("MainWindow", "Save Preset As"))
        self.actionNew_Preset.setText(_translate("MainWindow", "New Preset"))
        self.actionNew_Device_Preset.setText(_translate("MainWindow", "New Device Preset"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_window(object):
    def setupUi(self, settings_window):
        settings_window.setObjectName("settings_window")
        settings_window.resize(549, 482)
        self.gridLayout = QtWidgets.QGridLayout(settings_window)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(settings_window)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 5, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(settings_window)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 3)
        self.radioButton_plain_numbers = QtWidgets.QRadioButton(settings_window)
        self.radioButton_plain_numbers.setCheckable(True)
        self.radioButton_plain_numbers.setChecked(True)
        self.radioButton_plain_numbers.setObjectName("radioButton_plain_numbers")
        self.gridLayout.addWidget(self.radioButton_plain_numbers, 8, 1, 1, 1)
        self.lineEdit_catalog_name = QtWidgets.QLineEdit(settings_window)
        self.lineEdit_catalog_name.setObjectName("lineEdit_catalog_name")
        self.gridLayout.addWidget(self.lineEdit_catalog_name, 17, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(settings_window)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 1, 1, 1)
        self.radioButton_scientific = QtWidgets.QRadioButton(settings_window)
        self.radioButton_scientific.setObjectName("radioButton_scientific")
        self.gridLayout.addWidget(self.radioButton_scientific, 8, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(settings_window)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 12, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(settings_window)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 1, 1, 1)
        self.radioButton_mixed = QtWidgets.QRadioButton(settings_window)
        self.radioButton_mixed.setObjectName("radioButton_mixed")
        self.gridLayout.addWidget(self.radioButton_mixed, 8, 3, 1, 1)
        self.line = QtWidgets.QFrame(settings_window)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 1, 1, 3)
        self.spinBox_scientific_from = QtWidgets.QSpinBox(settings_window)
        self.spinBox_scientific_from.setProperty("value", 3)
        self.spinBox_scientific_from.setObjectName("spinBox_scientific_from")
        self.gridLayout.addWidget(self.spinBox_scientific_from, 9, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(settings_window)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 11, 1, 1, 3)
        self.spinBox_n_decimals = QtWidgets.QSpinBox(settings_window)
        self.spinBox_n_decimals.setProperty("value", 2)
        self.spinBox_n_decimals.setObjectName("spinBox_n_decimals")
        self.gridLayout.addWidget(self.spinBox_n_decimals, 10, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(settings_window)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 16, 1, 1, 1)
        self.checkBox_autosave = QtWidgets.QCheckBox(settings_window)
        self.checkBox_autosave.setObjectName("checkBox_autosave")
        self.gridLayout.addWidget(self.checkBox_autosave, 1, 1, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(settings_window)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 26, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(settings_window)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 3)
        self.comboBox_theme = QtWidgets.QComboBox(settings_window)
        self.comboBox_theme.setObjectName("comboBox_theme")
        self.gridLayout.addWidget(self.comboBox_theme, 4, 1, 1, 3)
        self.label_10 = QtWidgets.QLabel(settings_window)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 17, 1, 1, 1)
        self.label = QtWidgets.QLabel(settings_window)
        self.label.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 3)
        self.line_5 = QtWidgets.QFrame(settings_window)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_5.setLineWidth(5)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 23, 1, 1, 3)
        self.label_11 = QtWidgets.QLabel(settings_window)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 24, 1, 1, 1)
        self.checkBox_play_camel_on_error = QtWidgets.QCheckBox(settings_window)
        self.checkBox_play_camel_on_error.setObjectName("checkBox_play_camel_on_error")
        self.gridLayout.addWidget(self.checkBox_play_camel_on_error, 25, 1, 1, 3)
        self.lineEdit_branch = QtWidgets.QLineEdit(settings_window)
        self.lineEdit_branch.setObjectName("lineEdit_branch")
        self.gridLayout.addWidget(self.lineEdit_branch, 21, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(settings_window)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 20, 1, 1, 1)
        self.pathButton_device_path = Path_Button_Edit(settings_window)
        self.pathButton_device_path.setObjectName("pathButton_device_path")
        self.gridLayout.addWidget(self.pathButton_device_path, 22, 2, 1, 2)
        self.label_14 = QtWidgets.QLabel(settings_window)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 21, 1, 1, 1)
        self.pathButton_py_files = Path_Button_Edit(settings_window)
        self.pathButton_py_files.setObjectName("pathButton_py_files")
        self.gridLayout.addWidget(self.pathButton_py_files, 13, 2, 1, 2)
        self.pathButton_meas_files = Path_Button_Edit(settings_window)
        self.pathButton_meas_files.setObjectName("pathButton_meas_files")
        self.gridLayout.addWidget(self.pathButton_meas_files, 16, 2, 1, 2)
        self.lineEdit_repo = QtWidgets.QLineEdit(settings_window)
        self.lineEdit_repo.setObjectName("lineEdit_repo")
        self.gridLayout.addWidget(self.lineEdit_repo, 20, 2, 1, 2)
        self.line_6 = QtWidgets.QFrame(settings_window)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_6.setLineWidth(5)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 18, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(settings_window)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 22, 1, 1, 1)
        self.lineEdit_directory = QtWidgets.QLineEdit(settings_window)
        self.lineEdit_directory.setObjectName("lineEdit_directory")
        self.gridLayout.addWidget(self.lineEdit_directory, 21, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(settings_window)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 19, 1, 1, 1)

        self.retranslateUi(settings_window)
        self.buttonBox.accepted.connect(settings_window.accept) # type: ignore
        self.buttonBox.rejected.connect(settings_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(settings_window)

    def retranslateUi(self, settings_window):
        _translate = QtCore.QCoreApplication.translate
        settings_window.setWindowTitle(_translate("settings_window", "Dialog"))
        self.label_2.setText(_translate("settings_window", "Theme"))
        self.radioButton_plain_numbers.setText(_translate("settings_window", "Plain"))
        self.label_6.setText(_translate("settings_window", "Python-Files Path"))
        self.radioButton_scientific.setText(_translate("settings_window", "Scientific"))
        self.label_5.setText(_translate("settings_window", "Files"))
        self.label_4.setText(_translate("settings_window", "# decimals:"))
        self.radioButton_mixed.setText(_translate("settings_window", "Scientific from 1e..."))
        self.label_7.setText(_translate("settings_window", "Measurement-Data Path"))
        self.checkBox_autosave.setText(_translate("settings_window", "Autosave on closing"))
        self.label_3.setText(_translate("settings_window", "Number-Formatting"))
        self.label_10.setText(_translate("settings_window", "Databroker catalog-name"))
        self.label.setText(_translate("settings_window", "Saving"))
        self.label_11.setText(_translate("settings_window", "Sounds"))
        self.checkBox_play_camel_on_error.setText(_translate("settings_window", "Play Camel-Roar on error"))
        self.lineEdit_branch.setPlaceholderText(_translate("settings_window", "branch"))
        self.label_12.setText(_translate("settings_window", "Driver Repository URL"))
        self.label_14.setText(_translate("settings_window", "Branch / Directory"))
        self.label_8.setText(_translate("settings_window", "Local drivers path"))
        self.lineEdit_directory.setPlaceholderText(_translate("settings_window", "directory"))
        self.label_13.setText(_translate("settings_window", "Drivers"))
from CAMELS.ui_widgets.path_button_edit import Path_Button_Edit
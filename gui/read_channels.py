# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_channels.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_read_channels_config(object):
    def setupUi(self, read_channels_config):
        read_channels_config.setObjectName("read_channels_config")
        read_channels_config.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(read_channels_config)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(read_channels_config)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox_plot = QtWidgets.QCheckBox(read_channels_config)
        self.checkBox_plot.setChecked(True)
        self.checkBox_plot.setObjectName("checkBox_plot")
        self.gridLayout.addWidget(self.checkBox_plot, 0, 2, 1, 1)
        self.checkBox_save = QtWidgets.QCheckBox(read_channels_config)
        self.checkBox_save.setChecked(True)
        self.checkBox_save.setObjectName("checkBox_save")
        self.gridLayout.addWidget(self.checkBox_save, 1, 2, 1, 1)
        self.checkBox_use_set = QtWidgets.QCheckBox(read_channels_config)
        self.checkBox_use_set.setObjectName("checkBox_use_set")
        self.gridLayout.addWidget(self.checkBox_use_set, 2, 2, 1, 1)
        self.tableWidget_channels = QtWidgets.QTableWidget(read_channels_config)
        self.tableWidget_channels.setObjectName("tableWidget_channels")
        self.tableWidget_channels.setColumnCount(0)
        self.tableWidget_channels.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_channels, 3, 0, 1, 3)
        self.comboBox_readType = QtWidgets.QComboBox(read_channels_config)
        self.comboBox_readType.setObjectName("comboBox_readType")
        self.gridLayout.addWidget(self.comboBox_readType, 1, 0, 1, 2)

        self.retranslateUi(read_channels_config)
        QtCore.QMetaObject.connectSlotsByName(read_channels_config)

    def retranslateUi(self, read_channels_config):
        _translate = QtCore.QCoreApplication.translate
        read_channels_config.setWindowTitle(_translate("read_channels_config", "Form"))
        self.label.setText(_translate("read_channels_config", "Read-Type:"))
        self.checkBox_plot.setText(_translate("read_channels_config", "Plot Data"))
        self.checkBox_save.setText(_translate("read_channels_config", "Save Data"))
        self.checkBox_use_set.setText(_translate("read_channels_config", "Use Set-Value for outputs"))


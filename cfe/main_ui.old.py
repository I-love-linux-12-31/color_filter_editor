# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setObjectName("background")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.background)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.background)
        self.widget.setMinimumSize(QtCore.QSize(80, 256))
        self.widget.setMaximumSize(QtCore.QSize(80, 16777215))
        self.widget.setStyleSheet("background-color: rgb(248, 228, 92);")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(32)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.tabWidget = QtWidgets.QTabWidget(self.background)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.sys_info = QtWidgets.QWidget()
        self.sys_info.setObjectName("sys_info")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sys_info)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_0 = QtWidgets.QLabel(self.sys_info)
        self.label_0.setMinimumSize(QtCore.QSize(0, 24))
        self.label_0.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_0.setObjectName("label_0")
        self.verticalLayout.addWidget(self.label_0)
        self.label_1 = QtWidgets.QLabel(self.sys_info)
        self.label_1.setMinimumSize(QtCore.QSize(0, 24))
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.sys_info)
        self.label_2.setMinimumSize(QtCore.QSize(0, 24))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.sys_info)
        self.label_3.setMinimumSize(QtCore.QSize(0, 24))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.sys_info)
        self.label_4.setMinimumSize(QtCore.QSize(0, 24))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.sys_info)
        self.label_5.setMinimumSize(QtCore.QSize(0, 24))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.widget_3 = QtWidgets.QWidget(self.sys_info)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.tabWidget.addTab(self.sys_info, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_0.setText(_translate("MainWindow", "system"))
        self.label_1.setText(_translate("MainWindow", "cpu:"))
        self.label_2.setText(_translate("MainWindow", "memory:"))
        self.label_3.setText(_translate("MainWindow", "gpu_1"))
        self.label_4.setText(_translate("MainWindow", "gpu_2"))
        self.label_5.setText(_translate("MainWindow", "gpu_3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sys_info), _translate("MainWindow", "Sys info"))

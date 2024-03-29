from PyQt6 import QtCore, QtGui, QtWidgets
from debug_imgs_widget import DebugImagesWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 581)
        icon = QtGui.QIcon.fromTheme("user-desktop")
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
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
        self.tabWidget = QtWidgets.QTabWidget(self.background)
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.sys_info = QtWidgets.QWidget()
        self.sys_info.setObjectName("sys_info")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sys_info)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_sys = QtWidgets.QLabel(self.sys_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sys.sizePolicy().hasHeightForWidth())
        self.label_sys.setSizePolicy(sizePolicy)
        self.label_sys.setMinimumSize(QtCore.QSize(0, 24))
        self.label_sys.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_sys.setObjectName("label_sys")
        self.verticalLayout.addWidget(self.label_sys)
        self.label_cpu = QtWidgets.QLabel(self.sys_info)
        self.label_cpu.setMinimumSize(QtCore.QSize(0, 24))
        self.label_cpu.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_cpu.setObjectName("label_cpu")
        self.verticalLayout.addWidget(self.label_cpu)
        self.label_mem = QtWidgets.QLabel(self.sys_info)
        self.label_mem.setMinimumSize(QtCore.QSize(0, 24))
        self.label_mem.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_mem.setObjectName("label_mem")
        self.verticalLayout.addWidget(self.label_mem)
        self.label_gpu = QtWidgets.QLabel(self.sys_info)
        self.label_gpu.setMinimumSize(QtCore.QSize(0, 24))
        self.label_gpu.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_gpu.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.label_gpu.setObjectName("label_gpu")
        self.verticalLayout.addWidget(self.label_gpu)
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

        # self.test_image = QtWidgets.QLabel()
        # self.test_image.setSizePolicy(sizePolicy)
        # self.label_sys.setMinimumSize(QtCore.QSize(0, 24))
        # self.label_sys.setMaximumSize(QtCore.QSize(16777215, 32))
        # self.label_sys.setObjectName("label_sys")
        # self.verticalLayout.addWidget(self.label_sys)

        self.debug_images_widget = DebugImagesWindow()

        self.debug_images_widget_button = QtWidgets.QPushButton(self.sys_info)
        self.debug_images_widget_button.setText("Show debug image")
        self.debug_images_widget_button.clicked.connect(lambda: self.debug_images_widget.show())
        self.verticalLayout.addWidget(self.debug_images_widget_button)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ColorFilterEditor"))
        self.label_sys.setText(_translate("MainWindow", "system:"))
        self.label_cpu.setText(_translate("MainWindow", "cpu:"))
        self.label_mem.setText(_translate("MainWindow", "memory:"))
        self.label_gpu.setText(_translate("MainWindow", "gpu_1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sys_info), _translate("MainWindow", "Sys info"))

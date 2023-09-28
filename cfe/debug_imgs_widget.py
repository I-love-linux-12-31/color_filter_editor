from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QWidget, QGridLayout


class DebugImagesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 300)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self)
        self.label.setObjectName(u"gradient_img")
        self.label.setMinimumSize(512, 64)

        pixmap = QPixmap("gradient_test.jpg")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"color_img")
        self.label_2.setMinimumSize(256, 256)
        self.label_2.setMaximumSize(512, 512)
        self.label_2.setScaledContents(True)

        pixmap2 = QPixmap("color_debug.jpg")
        self.label_2.setPixmap(pixmap2)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.setWindowTitle("Debug images")
        self.resize(800, 300)

    def show(self):
        super().show()
        print(self.width(), self.height())

import os
import sys
import psutil

from PyQt6.QtWidgets import QWidget, QMainWindow, QMessageBox
from main_ui import *
from monitor_widget_ui import Ui_Form as MonitorConfigWidgetUI


class MainWindow(QMainWindow, Ui_MainWindow):
    pass


class MonitorConfigWidget(QWidget, MonitorConfigWidgetUI):
    def __init__(self, port: str, modes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.label.setText(port)

        self.interface = port

        for interface, size, frequencies in modes:
            if interface != port:
                continue
            for freq in frequencies:
                w, h = size[0], size[1]
                self.comboBox.addItem(f"{w}x{h}\t\t{freq} Hz")

        self.pushButton.clicked.connect(self.apply_changes)

    def apply_changes(self):
        gamma = tuple(map(lambda a: round(a, 3), (self.gamma_r.value(), self.gamma_g.value(), self.gamma_b.value())))
        brightness = self.brightness.value()
        current_mode_text = self.comboBox.currentText().split()
        # current_size = tuple(map(int, current_mode_text[0].split("x")))
        current_size = current_mode_text[0]
        freq = float(current_mode_text[1])
        print(gamma, brightness)
        print(current_size, freq)

        command = f"xrandr" \
                  f" --output {self.interface}" \
                  f" --mode {current_size}" \
                  f" --gamma {':'.join(map(str, gamma))}" \
                  f" --brightness {brightness}" \
                  f" --rate {freq}"
        print(command)
        if sum(gamma) / 3 < 0.3 or sum(gamma) / 3 > 1.6 or brightness < 0.2:
            if QMessageBox.warning(
                    None, "Are you sure?", "Are you sure?", QMessageBox.Cancel | QMessageBox.Ok
            ) == QMessageBox.Cancel:
                print("Canceled.")
                return

        os.system(command)

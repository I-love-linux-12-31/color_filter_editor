from PyQt6.QtWidgets import QWidget, QMainWindow, QMessageBox

from core import load_from_config, save_to_file, apply_config
from main_ui import *  # noqa: F403
from monitor_widget_ui import Ui_Form as MonitorConfigWidgetUI


class MainWindow(QMainWindow, Ui_MainWindow):  # noqa: F405
    pass


class MonitorConfigWidget(QWidget, MonitorConfigWidgetUI):
    def __init__(self, port: str, modes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.output_port.setText(port)

        self.interface = port

        for interface, size, frequencies in modes:
            if interface != port:
                continue
            for freq in frequencies:
                w, h = size[0], size[1]
                self.comboBox.addItem(f"{w}x{h}\t\t{freq} Hz")

        self.btn_apply.clicked.connect(self.apply_changes)
        self.btn_load.clicked.connect(self.load_config)
        self.btn_save.clicked.connect(self.save_config)

        self.load_config()

    def apply_changes(self):
        info = self.take_info()
        gamma = info["gamma"]
        brightness = info["brightness"]
        if sum(gamma) / 3 < 0.3 or sum(gamma) / 3 > 1.6 or brightness < 0.2:
            if QMessageBox.warning(
                    None, "Are you sure?", "Are you sure?",
                    QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok,
            ) == QMessageBox.StandardButton.Cancel:
                print("Canceled.")
                return

        apply_config(**info)

    def load_config(self):
        config = load_from_config().get(self.interface, dict())
        gamma = config.get("gamma", (1.0, 1.0, 1.0))
        self.gamma_r.setValue(gamma[0])
        self.gamma_g.setValue(gamma[1])
        self.gamma_b.setValue(gamma[2])

        self.brightness.setValue(config.get("brightness", 1.0))

        screen_mode = F"{config.get('display_resolution', None)} {config.get('freq', None)}"
        if "None" not in screen_mode:
            self.comboBox.setCurrentText(screen_mode)

    def take_info(self) -> dict:
        gamma = tuple(map(lambda a: round(a, 3), (self.gamma_r.value(), self.gamma_g.value(), self.gamma_b.value())))
        brightness = self.brightness.value()
        current_mode_text = self.comboBox.currentText().split()
        # display_resolution = tuple(map(int, current_mode_text[0].split("x")))
        display_resolution = current_mode_text[0]
        freq = float(current_mode_text[1])
        return {
            "interface": self.interface,
            "gamma": gamma,
            "brightness": brightness,
            "display_resolution": display_resolution,
            "freq": freq,
        }

    def save_config(self):
        save_to_file(**self.take_info())

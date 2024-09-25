from dependencies_checker import check_dependencies
from PyQt6 import QtCore

check_dependencies()

import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication

from windows import MainWindow, MonitorConfigWidget

from get_pc_info import get_pc_info
from get_pc_info import init as get_pc_info_init

import sys_info_graber as sys_info


def main():
    get_pc_info_init()
    pc_info = get_pc_info()
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setupUi(main_window)

    main_window.label_sys.setText(f"System : {sys_info.get_system_info()}")
    if sys_info.get_total_ram_size_in_gb() > 2:
        main_window.label_mem.setText("RAM : " + str(sys_info.get_total_ram_size_in_gb()) + " GB")
    else:
        main_window.label_mem.setText("RAM : " + str(sys_info.get_total_ram_size_in_mb) + " MB")

    if not sys_info.get_gpus_names():
        main_window.label_gpu.setText("GPUS: NO")
    else:
        gpus = sys_info.get_gpus_names()
        if len(gpus) > 1:  # 2
            main_window.label_gpu.setMinimumSize(QtCore.QSize(0, 52))
        if len(gpus) > 2:  # > 2
            main_window.label_gpu.setMinimumSize(QtCore.QSize(0, 128))

        main_window.label_gpu.setText("GPUS:\n" + "\n".join(gpus))
    main_window.label_cpu.setText("CPU:\n" + "\n".join(sys_info.get_cpus_names()))

    for interface in pc_info["active_ports"]:
        main_window.tabWidget.addTab(MonitorConfigWidget(interface, pc_info["screen_modes"]), interface)
        print(interface)
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

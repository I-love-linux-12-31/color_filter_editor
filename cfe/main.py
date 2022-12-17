from dependencies_checker import check_dependencies
check_dependencies()

import sys
import PyQt5
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QWidget, QLabel

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

    main_window.label_gpu.setText("GPUS:\n" + "\n".join(sys_info.get_gpus_names()))
    main_window.label_cpu.setText("CPUS:\n" + "\n".join(sys_info.get_cpus_names()))

    for interface in pc_info["active_ports"]:
        main_window.tabWidget.addTab(MonitorConfigWidget(interface, pc_info["screen_modes"]), interface)
        print(interface)
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

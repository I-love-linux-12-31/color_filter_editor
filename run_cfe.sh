#!/bin/bash

((lscpu && lspci && cat --version && xrandr --version && clear && (python3 /opt/color_filter_editor/cfe/main.py || python3 ./cfe/main.py)) || python3 /opt/color_filter_editor/cfe/main.py || echo -e "\033[31mSome of dependencies not found!\033[0m" ) >> /mnt/cfe.log

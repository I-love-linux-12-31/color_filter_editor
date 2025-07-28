# A simple program for setting up color correction in X11

[README на русском (RU)](https://github.com/I-love-linux-12-31/color_filter_editor/blob/master/README_RU.md)


This program allows to change the brightness of the display and the intensity of individual colors
in systems with the X11 graphics server for each video output separately.

> [!WARNING]
> Wayland not supported

Source code repos:
1. https://bitbucket.org/i-love-linux-12-31/colorfiltereditor/
2. https://github.com/I-love-linux-12-31/color_filter_editor


## Dependencies:
The following utilities must be installed on your system for the program to work correctly:
* bash
* lspci
* xrandr
* python3

Python libraries:
* PyQt6
* psutil

## Launching app:
<pre>$ ./run_cfe.sh</pre>

## Installing app:
<pre># ./install.sh</pre> or <pre>$ sudo ./install.sh</pre>


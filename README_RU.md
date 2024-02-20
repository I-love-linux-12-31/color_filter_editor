# Простая программа для настройки коррекции цвета в X11

[RU] README_RU.md<br>
[EN] README.md

Данная программа позволяет изменить яркость дисплея и интенсивность отдельных цветов
в системах с графическим сервером X11 для каждого видео-выхода отдельно.

### ! Wayland не поддерживается !

Исходный код:
1. https://bitbucket.org/i-love-linux-12-31/colorfiltereditor/
2. https://github.com/I-love-linux-12-31/color_filter_editor


## Зависимости:
Для работы программы в вашей системе должны быть установленны следующие утилиты:
* bash
* lspci
* xrandr
* python3

А также python библиотеки:
* PyQt6
* psutil

## Запуск:
<pre>$ ./run_cfe.sh</pre>

## Установка:
<pre># ./install.sh</pre> или <pre>$ sudo ./install.sh</pre>

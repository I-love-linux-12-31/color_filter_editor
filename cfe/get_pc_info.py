import sys
import os
import subprocess


from string import punctuation


pc_info = dict()
__inited = False


def __update_devices():
    result = subprocess.run(
        ["xrandr", "--listproviders"], capture_output=True, text=True
    )
    if bool(result.stderr):
        print("[Err] (get pc info): Subprocess end with errors")
        raise SystemError()
    lines = result.stdout.strip().split("\n")
    devices_count = int(lines[0].strip().split()[-1])
    devices = []
    for i in range(devices_count):
        device = dict()
        line_raw = lines[1 + i].strip()
        line = line_raw.split()
        device["id"] = int(line[1][:-1])
        device["outputs_count"] = line[17]
        name = line_raw[line_raw.find("name") + 5:line_raw.rfind("@") - 1]
        device["name"] = name.strip()
        devices.append(device)
    pc_info["devices"] = devices


def __update_displays():
    result = subprocess.run(
        ["xrandr", ], capture_output=True, text=True
    )
    if bool(result.stderr):
        print("[Err] (get pc info): Subprocess end with errors")
        raise SystemError()
    lines = result.stdout.strip().split("\n")
    lines_2 = lines[1:]
    data_raw = []
    last_header = lines_2.pop(0)
    mode_info_lines = []
    while lines_2:
        i = lines_2.pop(0)
        if i[0] == " ":
            mode_info_lines.append(i)
        else:
            data_raw.append((last_header, mode_info_lines.copy()))
            mode_info_lines.clear()
            last_header = i
    data_raw.append((last_header, mode_info_lines.copy()))

    modes = []
    active_ports = []
    for header, data in data_raw:
        # print(">>", header, data)
        interface = header.split()[0]
        if interface not in active_ports and data:
            active_ports.append(interface)
        for block in data:
            temp = block.strip().split()
            size = tuple(map(int, temp.pop(0).split("x")))
            frequencies = []
            for j in temp:
                for n in punctuation:
                    if n in j and n != ".":
                        j = j.replace(n, "")
                frequencies.append(j)
            modes.append((interface, size, frequencies))
    pc_info["screen_modes"] = modes
    pc_info["active_ports"] = active_ports


def __get_info():
    result = subprocess.run(
        ["xrandr", "--listproviders"], capture_output=True, text=True
    )
    if bool(result.stderr):
        print("[Err] (get pc info): Subprocess end with errors")
        raise SystemError()

    for line in result.stdout.strip().split("\n"):
        print(">>", line)


def init():
    global __inited
    __update_devices()
    __update_displays()
    __inited = True


def is_inited() -> bool:
    if not pc_info:
        return False
    if not pc_info["screen_modes"]:
        return False
    return __inited


def get_pc_info() -> dict:
    if is_inited():
        return pc_info
    raise RuntimeError("Module not inited")


if __name__ == '__main__':
    init()
    print(get_pc_info())

import os
import subprocess
import sys

import psutil


def get_gpus_names() -> []:
    result = subprocess.run(
        ["lspci", ], capture_output=True, text=True
    )
    if bool(result.stderr):
        print("[Err] (get pc info): Subprocess end with errors")
        raise SystemError()
    lines = result.stdout.strip().split("\n")

    return [" ".join(i.strip().split()[1:]) for i in lines if "VGA" in i]


def get_cpus_names() -> []:
    result = subprocess.run(
        ["cat", "/proc/cpuinfo"], capture_output=True, text=True
    )
    if bool(result.stderr):
        print("[Err] (get pc info): Subprocess end with errors")
        raise SystemError()
    lines = result.stdout.strip().split("\n")
    temp = [i.strip().split(":")[1].strip() for i in lines if "model name" in i]
    temp = [i + "\tx" + str(temp.count(i)) for i in temp]
    return [" ".join(list(set(temp)))]


def get_total_ram_size_in_mb():
    return round(psutil.virtual_memory().total / 1024 / 1024, 1)


def get_total_ram_size_in_gb():
    return round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 2)


def get_system_info():
    if sys.platform != "linux":
        return sys.platform
    result = subprocess.run(
        ["cat", "/proc/version"], capture_output=True, text=True
    )
    if bool(result.stderr):
        print("[Err] (get pc info): Subprocess end with errors")
        raise SystemError()
    return result.stdout.strip()

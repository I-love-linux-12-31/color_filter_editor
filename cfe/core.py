import os
import shutil
import json

INTERFACES_CONFIG_PATH = os.path.expanduser("~/.config/color_filter_editor/interfaces_config.json")


def _create_dir_if_not_exists(_path):
    path = os.path.expanduser(_path)
    if not os.path.exists(path):
        os.mkdir(path)


def apply_config(
        interface: str,
        display_resolution: str,
        brightness: float or int,
        freq: float,
        gamma: (float, float, float),
        show_cmd=True,
):

    command = f"xrandr" \
              f" --output {interface}" \
              f" --mode {display_resolution}" \
              f" --gamma {':'.join(map(str, gamma))}" \
              f" --brightness {brightness}" \
              f" --rate {freq}"
    if show_cmd: print(command)
    os.system(command)

def save_to_file(**params):
    _create_dir_if_not_exists("~/.config")
    _create_dir_if_not_exists("~/.config/color_filter_editor")

    config = dict()

    if os.path.exists(INTERFACES_CONFIG_PATH):
        try:
            with open(INTERFACES_CONFIG_PATH, "rt") as f:
                config = json.load(f)
        except json.decoder.JSONDecodeError:
            pass

    config[params["interface"]] = params

    with open(INTERFACES_CONFIG_PATH, "wt") as f:
        json.dump(config, f)

def load_from_config() -> dict:
    try:
        if os.path.exists(INTERFACES_CONFIG_PATH):
            with open(INTERFACES_CONFIG_PATH, "rt") as f:
               return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass
    return dict()

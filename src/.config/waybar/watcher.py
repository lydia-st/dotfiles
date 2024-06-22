#!/usr/bin/env python3

# this exists as my ide does not support syntax highlighting
# for .jsonc. when i save the .json file, this script will
# copy the file to a .jsonc file.

# it also exists because i am lazy and don't want to manually
# kill and restart waybar every time i make a change to the css.

import os
import time
import shutil

def restart_waybar():
    os.system("killall -SIGUSR2 waybar")
    print(f"Reloaded Waybar Config")

def reload_waybar_css():
    os.system("killall -SIGUSR2 waybar")
    print("Reloaded Waybar CSS")

def watch_files(file_actions, interval=1):
    last_modified_times = {file: os.path.getmtime(file) for file in file_actions if os.path.isfile(file)}

    while True:
        try:
            for file, actions in file_actions.items():
                if os.path.isfile(file):
                    current_modified_time = os.path.getmtime(file)
                    if current_modified_time != last_modified_times[file]:
                        for action in actions:
                            action(file)
                        last_modified_times[file] = current_modified_time
            time.sleep(interval)
        except KeyboardInterrupt:
            print("Stopping the file watcher.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    file_actions = {
        "config.jsonc": [lambda file: restart_waybar()],
        "style.css": [lambda file: reload_waybar_css()],
    }
    watch_interval = 1  # Check every 1 second
    watch_files(file_actions, watch_interval)

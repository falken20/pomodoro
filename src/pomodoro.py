# by Richi Rod AKA @richionline / falken20

import os
import time
import tkinter as tk
from click import command  # Include Themed widgets

from logger import Log, console
from components import *
from db import update_summary, get_summary, cursor, init_cycles_count

console.rule("Pomodoro")

SOUND_FILE = './docs/static/sounds/sound.mp3'


def index(message=""):
    Log.info("Method to show index page...")


def set_handlers():
    btn_focus.config(command=handle_btn_focus)
    btn_pause.config(command=handle_btn_pause)
    btn_config.config(command=handle_btn_config)


def handle_keypress(event):
    # Log.info(f"Key pressed: {event.char}")
    pass


def handle_btn_focus():
    try:
        Log.info(f"Button FOCUS pressed")

        seconds = 3

        lbl_time.config(text=f"{seconds // 60:02d}:{seconds % 60:02d}")
        window_pomodoro.update()

        while seconds > 0:
            time.sleep(1)
            seconds -= 1
            lbl_time.config(text=f"{seconds // 60:02d}:{seconds % 60:02d}")
            window_pomodoro.update()

        # Play sound in Mac with native player
        os.system("afplay " + SOUND_FILE)

        Log.info("Pomodoro time finished. Updating DB nd get data for labels...")

        update_summary()
        data = get_summary()
        update_panels(
            pomodoro_count=data[1], cycles_count=data[2], total_cycles_count=data[3])
        Log.info("Data and panels succesfully updated")

    except Exception as err:
        Log.error("Error in Focus button", err, sys)


def handle_btn_pause():
    Log.info(f"Button PAUSE pressed")


def handle_btn_config():
    Log.info(f"Button CONFIG pressed")


def set_panel_values():
    Log.info("Setting values for panel info")
    init_cycles_count()
    data = get_summary()
    update_panels(
        pomodoro_count=data[1], cycles_count=data[2], total_cycles_count=data[3])


if __name__ == "__main__":
    Log.info("Starting pomodoro app")

    set_window()
    set_styles()
    set_frame_top()
    set_frame_time()
    set_frame_panel()
    set_handlers()
    set_panel_values()

    # Bind keypress event to handle_keypress()
    window_pomodoro.bind("<Key>", handle_keypress)

    window_pomodoro.mainloop()  # Runs the Tkinter events loop

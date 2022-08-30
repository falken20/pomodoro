# by Richi Rod AKA @richionline / falken20

import os
import time
import sqlite3
import tkinter as tk
from click import command  # Include Themed widgets

from logger import Log, console
from components import *

console.rule("Primazon")

DATABASE_SQLLITE = "pomodoro.db"
SOUND_FILE = './docs/static/sounds/sound.mp3'


# Set the database params for SQLAlchemy ORM library. This is due to a change in the sqlalchemy
# library. It was an announced deprecation in the changing of name postgres to postgresql.
# In Heroku you cant change the value of this environment var to postgresql
db = os.getenv('DATABASE_URL', None)
if db is None:
    db = sqlite3.connect(DATABASE_SQLLITE)
else:
    pass


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
    Log.info(f"Button FOCUS pressed")

    lbl_time.config(text="15:00")
    window_pomodoro.update()

    seconds = 5
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
        lbl_time.config(text=f"{seconds // 60:02d}:{seconds % 60:02d}")
        window_pomodoro.update()

        Log.info(f"{seconds=}")

    # Play sound in Mac with native player
    os.system("afplay " + SOUND_FILE)

def handle_btn_pause():
    Log.info(f"Button PAUSE pressed")


def handle_btn_config():
    Log.info(f"Button CONFIG pressed")


if __name__ == "__main__":
    Log.info("Starting pomodoro app")

    set_window()
    set_styles()
    set_frame_top()
    set_frame_time()
    set_frame_panel()
    set_handlers()

    # Bind keypress event to handle_keypress()
    window_pomodoro.bind("<Key>", handle_keypress)

    window_pomodoro.mainloop()  # Runs the Tkinter events loop

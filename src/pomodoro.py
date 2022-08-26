# by Richi Rod AKA @richionline / falken20

import os
import sqlite3
import tkinter as tk
from turtle import bgcolor

from click import command  # Include Themed widgets

from logger import Log, console
from components import *

console.rule("Primazon")

DATABASE_SQLLITE = "pomodoro.db"


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


def set_frame_time():
    """ Create the time panel in the left side of the screen """

    frm_time.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    lbl_time.pack(side=tk.TOP)
    lbl_time.config(font=(FONT_TYPE, 60))
    btn_config.pack(side=tk.BOTTOM)
    btn_config.config(command=handle_btn_config)
    btn_focus.pack(side=tk.BOTTOM)
    btn_focus.config(command=handle_btn_focus)
    btn_pause.pack()
    btn_restart.pack()


def set_frame_panel():
    """ Create the result panel in the right side of the screen """

    frm_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    lbl_pomodoro.pack(side=tk.TOP)
    lbl_count_pomodoro.pack()
    lbl_cycles.pack(side=tk.TOP)
    lbl_count_cycles.pack()
    lbl_total.pack(side=tk.TOP)
    lbl_total_cycles.pack()


def set_styles():
    s = ttk.Style()
    # Create style used by default for all Frames
    s.configure('TFrame', background='green')

    # Setting a specific style
    s.configure("FrameTime.TFrame", background="red")
    s.configure("FramePanel.TFrame", background="yellow")


def handle_keypress(event):
    # Log.info(f"Key pressed: {event.char}")
    pass


def handle_btn_focus():
    Log.info(f"Button Focus pressed")

    lbl_time.config(text="15:00")


def handle_btn_config(event):
    Log.info(f"Button Config pressed")


if __name__ == "__main__":
    Log.info("Starting pomodoro app")

    window_pomodoro.title("Pomodoro")
    window_pomodoro.geometry('350x150')
    window_pomodoro.config(bg='red')
    window_pomodoro.resizable(0, 0)

    set_styles()
    set_frame_time()
    set_frame_panel()

    # Bind keypress event to handle_keypress()
    window_pomodoro.bind("<Key>", handle_keypress)

    window_pomodoro.mainloop()  # Runs the Tkinter events loop

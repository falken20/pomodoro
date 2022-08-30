# by Richi Rod AKA @richionline / falken20

import os
import time
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


def set_frame_top():
    """ Create the panel for logo app """
    frm_logo.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    lbl_logo.pack()


def set_frame_time():
    """ Create the time panel in the left side of the screen """

    frm_time.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    lbl_time.pack(side=tk.TOP)
    lbl_time.config(font=(FONT_TYPE, 60))
    lbl_time.grid(column=0, row=0, padx=1, pady=1, columnspan=2)

    btn_focus.config(command=handle_btn_focus)
    btn_focus.grid(column=0, row=1, sticky=tk.NS, padx=1, pady=1)

    btn_pause.config(command=handle_btn_pause)
    btn_pause.grid(column=1, row=1, sticky=tk.NS, padx=1, pady=1)

    btn_restart.config(command=handle_btn_restart)
    btn_restart.grid(column=0, row=2, sticky=tk.NS, padx=1, pady=1)

    btn_config.config(command=handle_btn_config)
    btn_config.grid(column=1, row=2, sticky=tk.NS, padx=1, pady=1)


def set_frame_panel():
    """ Create the result panel in the right side of the screen """

    frm_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    lbl_pomodoro.grid(column=1, row=0, sticky=tk.NS, padx=1, pady=1)
    lbl_pomodoro.config(font=(FONT_TYPE, 14, 'bold'))
    lbl_count_pomodoro.grid(column=1, row=1, sticky=tk.NS, padx=1, pady=1)

    lbl_cycles.grid(column=1, row=2, sticky=tk.NS, padx=1, pady=1)
    lbl_count_cycles.grid(column=1, row=3, sticky=tk.NS, padx=1, pady=1)

    lbl_total.grid(column=1, row=4, sticky=tk.NS, padx=1, pady=1)
    lbl_total_cycles.grid(column=1, row=5, sticky=tk.NS, padx=1, pady=1)


def set_styles():
    s = ttk.Style()
    # Create style used by default for all Frames
    s.configure('TFrame', background='green')

    # Setting a specific style
    s.configure("FrameTime.TFrame", background="red")
    s.configure("FramePanel.TFrame", background="yellow")


def set_window():
    """ Set the styles for main window """
    window_pomodoro.title("Pomodoro")
    # window_pomodoro.geometry('350x150')
    window_pomodoro.config(bg='red')
    window_pomodoro.resizable(0, 0)

    # Set the column weight
    window_pomodoro.columnconfigure(0, weight=2)
    window_pomodoro.columnconfigure(1, weight=1)


def handle_keypress(event):
    # Log.info(f"Key pressed: {event.char}")
    pass


def handle_btn_focus():
    Log.info(f"Button FOCUS pressed")

    lbl_time.config(text="15:00")

    seconds = 900
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
        lbl_time.config(text=f"{seconds // 60}:{seconds % 60}")
        window_pomodoro.update()

        Log.info(f"{seconds=}")


def handle_btn_pause():
    Log.info(f"Button PAUSE pressed")


def handle_btn_restart():
    Log.info(f"Button RESTART pressed")


def handle_btn_config():
    Log.info(f"Button CONFIG pressed")


if __name__ == "__main__":
    Log.info("Starting pomodoro app")

    set_window()
    set_styles()
    set_frame_top()
    set_frame_time()
    set_frame_panel()

    # Bind keypress event to handle_keypress()
    window_pomodoro.bind("<Key>", handle_keypress)

    window_pomodoro.mainloop()  # Runs the Tkinter events loop

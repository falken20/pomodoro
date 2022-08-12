# by Richi Rod AKA @richionline / falken20

from cProfile import label
from cgitb import text
import sys
import os
import sqlite3
import tkinter as tk       # Include classic widgets
import tkinter.ttk as ttk
from turtle import bgcolor  # Include Themed widgets

from logger import Log, console

console.rule("Primazon")

DATABASE_SQLLITE = "pomodoro.db"
BORDER_WIDTH = 5  # Border width of the frames


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


def create_widget_time(window):
    """ Create the time panel in the left side of the screen """
    frame_time = ttk.Frame(master=window, relief=tk.RIDGE,
                           borderwidth=BORDER_WIDTH)
    frame_time.pack(side=tk.LEFT)

    label_time = ttk.Label(master=frame_time, text="00:00")
    label_time.pack(side=tk.TOP)

    button_config = ttk.Button(master=frame_time, text="Config")
    button_config.pack(side=tk.BOTTOM)

    button_focus = ttk.Button(master=frame_time, text="Start Focus")
    button_focus.pack(side=tk.BOTTOM)


def create_widget_panel(window):
    """ Create the result panel in the right side of the screen """
    frame_panel = ttk.Frame(master=window, relief=tk.RIDGE,
                            borderwidth=BORDER_WIDTH)
    frame_panel.pack(side=tk.RIGHT)

    label_pomodoro = ttk.Label(master=frame_panel, text="Count Pomodoro")
    label_pomodoro.pack(side=tk.TOP)
    label_count_pomodoro = ttk.Label(master=frame_panel, text="0")
    label_count_pomodoro.pack()

    label_cycles = ttk.Label(master=frame_panel, text="Count Cycles")
    label_cycles.pack(side=tk.TOP)
    label_count_cycles = ttk.Label(master=frame_panel, text="0")
    label_count_cycles.pack()

    label_total = ttk.Label(master=frame_panel, text="Total Cycles")
    label_total.pack(side=tk.TOP)
    label_total_cycles = ttk.Label(master=frame_panel, text="0")
    label_total_cycles.pack()


if __name__ == "__main__":
    Log.info("Starting pomodoro app")

    window_pomodoro = tk.Tk(screenName="Pomodoro")

    create_widget_time(window=window_pomodoro)
    create_widget_panel(window=window_pomodoro)

    window_pomodoro.mainloop()  # Runs the Tkinter events loop

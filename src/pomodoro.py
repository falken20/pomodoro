# by Richi Rod AKA @richionline / falken20

from cProfile import label
from cgitb import text
from distutils.command.config import config
import sys
import os
import sqlite3
import tkinter as tk
from tkinter import font       # Include classic widgets
import tkinter.ttk as ttk
from turtle import bgcolor  # Include Themed widgets

from logger import Log, console

console.rule("Primazon")

DATABASE_SQLLITE = "pomodoro.db"
BORDER_WIDTH = 5  # Border width of the frames
FONT_TYPE = "Helvatical bold"


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


def create_frame_time(window):
    """ Create the time panel in the left side of the screen """
    frm_time = ttk.Frame(master=window, relief=tk.RIDGE,
                         borderwidth=BORDER_WIDTH,
                         style="FrameTime.TFrame")
    frm_time.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    lbl_time = ttk.Label(master=frm_time, text="00:00")
    lbl_time.pack(side=tk.TOP)
    lbl_time.config(font=(FONT_TYPE, 60))

    btn_config = ttk.Button(master=frm_time, text="Config")
    btn_config.pack(side=tk.BOTTOM)

    btn_focus = ttk.Button(master=frm_time, text="Start Focus")
    btn_focus.pack(side=tk.BOTTOM)


def create_frame_panel(window):
    """ Create the result panel in the right side of the screen """
    frm_panel = ttk.Frame(master=window, relief=tk.RIDGE,
                          borderwidth=BORDER_WIDTH,
                          style="FrameRed.TFrame")
    frm_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    lbl_pomodoro = ttk.Label(master=frm_panel, text="Count Pomodoro")
    lbl_pomodoro.pack(side=tk.TOP)
    lbl_count_pomodoro = ttk.Label(master=frm_panel, text="0")
    lbl_count_pomodoro.pack()

    lbl_cycles = ttk.Label(master=frm_panel, text="Count Cycles")
    lbl_cycles.pack(side=tk.TOP)
    lbl_count_cycles = ttk.Label(master=frm_panel, text="0")
    lbl_count_cycles.pack()

    lbl_total = ttk.Label(master=frm_panel, text="Total Cycles")
    lbl_total.pack(side=tk.TOP)
    lbl_total_cycles = ttk.Label(master=frm_panel, text="0")
    lbl_total_cycles.pack()


def set_styles():
    s = ttk.Style()
    # Create style used by default for all Frames
    s.configure('TFrame', background='green')

    # Setting a specific style
    s.configure("FrameTime.TFrame", background="red")
    s.configure("FramePanel.TFrame", background="yellow")


if __name__ == "__main__":
    Log.info("Starting pomodoro app")

    window_pomodoro = tk.Tk(screenName="Pomodoro")
    window_pomodoro.title("Pomodoro")
    window_pomodoro.geometry('350x150')
    # window_pomodoro.config(bg='red')

    set_styles()
    create_frame_time(window=window_pomodoro)
    create_frame_panel(window=window_pomodoro)

    window_pomodoro.mainloop()  # Runs the Tkinter events loop

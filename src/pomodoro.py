# by Richi Rod AKA @richionline / falken20

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


if __name__ == "__main__":
    Log.info("Starting pomodoro app")

    window = tk.Tk(screenName="Pomodoro")

    greeting = tk.Label(text="TKinter label")
    greeting.pack() # Add widget to window

    new_greting = ttk.Label(text="Tkinter.ttk label")
    new_greting.pack()

    button_start = tk.Button(text="Start Focus", width=15, height=5, bg="blue")
    button_start.pack()

    button_config = ttk.Button(text="Config", width=15)
    button_config.pack()

    frame_test = ttk.Frame(name="frameTest")
    frame_test.pack()

    label_frame = ttk.Label(master=frame_test, text="Label in frame")
    label_frame.pack()

    window.mainloop() # Runs the Tkinter events loop

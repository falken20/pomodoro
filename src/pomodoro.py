# by Richi Rod AKA @richionline / falken20

import sys
import os
from flask import Flask, render_template, url_for, request, redirect
import sqlite3
import tkinter as tk 

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

    return render_template('base.html', message=message)


if __name__ == "__main__":
    Log.info("Starting pomodoro app")

    window = tk.Tk(screenName="Pomodoro")

    greeting = tk.Label(text="TKinter label")
    greeting.pack() # Add widget to window

    window.mainloop() # Runs the Tkinter events loop

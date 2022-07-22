# by Richi Rod AKA @richionline / falken20

import sys
import os
from flask import Flask, render_template, url_for, request, redirect
import sqlite3

from src.logger import Log, console

console.rule("Primazon")

DATABASE_SQLLITE = "pomodoro.db"

app = Flask(__name__, template_folder='../docs/templates',
            static_folder='../docs/static')
# Set this var to True to be able to make any web change and take the changes with refresh
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Set the database params for SQLAlchemy ORM library. This is due to a change in the sqlalchemy
# library. It was an announced deprecation in the changing of name postgres to postgresql.
# In Heroku you cant change the value of this environment var to postgresql
db = os.getenv('DATABASE_URL', None)
if db is None:
    db = sqlite3.connect(DATABASE_SQLLITE)
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = db.replace("://", "ql://", 1)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Secret key for creating session coockie. It has to be different for each user
app.secret_key = os.urandom(24)

# db.init_app(app)


@app.route('/')
@app.route('/home')
@app.route('/<message>')
@app.route('/home/<message>')
def index(message=""):
    Log.info("Method to show index page...")

    return render_template('base.html', message=message)
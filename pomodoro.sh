#!/bin/sh

echo "Create virtual environment..."
#viertualenv -p python3 venv

echo "Access to virtual environment..."
source ./venv/bin/activate

echo "Executing app..."
python ./src/pomodoro.py

echo "Deactivate virtual environment..."
deactivate
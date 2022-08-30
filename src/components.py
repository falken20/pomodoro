from distutils.command.config import config
import tkinter as tk
from tkinter import font
from tkinter.font import BOLD
import tkinter.ttk as ttk
from turtle import bgcolor

from click import style

BORDER_WIDTH = 5  # Border width of the frames
FONT_TYPE = "Arial"
FONT_SIZE = 14
PADDINGS = {'padx': 1, 'pady': 1}
LOGO = './docs/static/img/logo_app.png'


# TKinter main window
window_pomodoro = tk.Tk(screenName="Pomodoro")

# TKinter top frame
frm_logo = ttk.Frame(master=window_pomodoro, relief=tk.RIDGE,
                     borderwidth=BORDER_WIDTH)
photo = tk.PhotoImage(file=LOGO)
lbl_logo = ttk.Label(master=frm_logo, image=photo)

# TKinter components left side
frm_time = ttk.Frame(master=window_pomodoro, relief=tk.RIDGE,
                     borderwidth=BORDER_WIDTH,
                     style="FrameTime.TFrame")
lbl_time = ttk.Label(master=frm_time, text="00:00")
btn_focus = ttk.Button(master=frm_time, text="Start Focus", style="Button.TButton")
btn_pause = ttk.Button(master=frm_time, text="Pause", style="Button.TButton")
btn_config = ttk.Button(master=frm_time, text="Config", style="Button.TButton")


# TKinter components left side
frm_panel = ttk.Frame(master=window_pomodoro, relief=tk.RIDGE,
                      borderwidth=BORDER_WIDTH,
                      style="FramePanel.TFrame")
lbl_pomodoro = ttk.Label(master=frm_panel, text="Count Pomodoro")
lbl_count_pomodoro = ttk.Label(master=frm_panel, text="0")

lbl_cycles = ttk.Label(master=frm_panel, text="Count Cycles")
lbl_count_cycles = ttk.Label(master=frm_panel, text="0")

lbl_total = ttk.Label(master=frm_panel, text="Total Cycles")
lbl_total_cycles = ttk.Label(master=frm_panel, text="0")


def set_frame_top():
    """ Create the panel for logo app """
    frm_logo.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    lbl_logo.pack()


def set_frame_time():
    """ Create the time panel in the left side of the screen """

    frm_time.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    lbl_time.pack(side=tk.TOP)
    lbl_time.grid(column=0, row=0, padx=1, pady=1, columnspan=2)

    btn_focus.grid(column=0, row=1, sticky=tk.NS, **PADDINGS)
    btn_pause.grid(column=1, row=1, sticky=tk.NS, **PADDINGS)
    btn_config.grid(column=0, row=2, sticky=tk.NS, **PADDINGS, columnspan=2)


def set_frame_panel():
    """ Create the result panel in the right side of the screen """

    frm_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    lbl_pomodoro.grid(column=1, row=0, sticky=tk.NS, **PADDINGS)
    lbl_count_pomodoro.grid(column=1, row=1, sticky=tk.NS, **PADDINGS)

    lbl_cycles.grid(column=1, row=2, sticky=tk.NS, **PADDINGS)
    lbl_count_cycles.grid(column=1, row=3, sticky=tk.NS, **PADDINGS)

    lbl_total.grid(column=1, row=4, sticky=tk.NS, **PADDINGS)
    lbl_total_cycles.grid(column=1, row=5, sticky=tk.NS, **PADDINGS)


def set_styles():
    style = ttk.Style()
    # Create generic styles
    style.configure('TFrame', background='green')
    style.configure('TLabel', font=(FONT_TYPE, FONT_SIZE))
    style.configure('TButton', font=(FONT_TYPE, FONT_SIZE))

    # Setting a specific style
    style.configure("FrameTime.TFrame", background="red")
    style.configure("FramePanel.TFrame", background="yellow")

    style.map('Button.TButton',
        foreground = [('pressed','red'),('active','blue')],
        background = [('pressed','!disabled','black'),('active','white')],
        relief=[('pressed', 'sunken'),('!pressed', 'raised')]
    )

    # Individual styles
    lbl_time.config(font=(FONT_TYPE, 80, BOLD))
    lbl_count_pomodoro.config(font=(FONT_TYPE, 24, BOLD))
    lbl_count_cycles.config(font=(FONT_TYPE, 24, BOLD))
    lbl_total_cycles.config(font=(FONT_TYPE, 24, BOLD))


def set_window():
    """ Set the styles for main window """
    window_pomodoro.title("Pomodoro")
    # window_pomodoro.geometry('350x150')
    window_pomodoro.config(bg='red')
    window_pomodoro.resizable(0, 0)

    # Set the column weight
    window_pomodoro.columnconfigure(0, weight=2)
    window_pomodoro.columnconfigure(1, weight=1)

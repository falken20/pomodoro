from cgi import test
import tkinter as tk
import tkinter.ttk as ttk

BORDER_WIDTH = 5  # Border width of the frames
FONT_TYPE = "Helvatical bold"

# TKinter main window
window_pomodoro = tk.Tk(screenName="Pomodoro")


# TKinter components left side
frm_time = ttk.Frame(master=window_pomodoro, relief=tk.RIDGE,
                     borderwidth=BORDER_WIDTH,
                     style="FrameTime.TFrame")
lbl_time = ttk.Label(master=frm_time, text="00:00")
btn_config = ttk.Button(master=frm_time, text="Config")
btn_focus = ttk.Button(master=frm_time, text="Start Focus")
btn_pause = ttk.Button(master=frm_time, text="Pause")
btn_restart = ttk.Button(master=frm_time, text="Restart")


# TKinter components left side
frm_panel = ttk.Frame(master=window_pomodoro, relief=tk.RIDGE,
                      borderwidth=BORDER_WIDTH,
                      style="FrameRed.TFrame")
lbl_pomodoro = ttk.Label(master=frm_panel, text="Count Pomodoro")
lbl_count_pomodoro = ttk.Label(master=frm_panel, text="0")

lbl_cycles = ttk.Label(master=frm_panel, text="Count Cycles")
lbl_count_cycles = ttk.Label(master=frm_panel, text="0")

lbl_total = ttk.Label(master=frm_panel, text="Total Cycles")
lbl_total_cycles = ttk.Label(master=frm_panel, text="0")

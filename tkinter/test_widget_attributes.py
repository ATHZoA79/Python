import tkinter as tk
from tkinter import ttk
import _tkinter
import json

def con_dict(w):
    options = {}
    for i in w.keys():
        value = w.cget(i)
        options[i] = value.string if type(value) is _tkinter.Tcl_Obj else value
    return options

root = tk.Tk()
widget = tk.Label(
    root, text='test', relief='raised', borderwidth=3)
widget.pack()
# print(json.dumps(con_dict(widget), indent=4))
root.mainloop()
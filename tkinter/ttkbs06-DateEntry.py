from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox


def handleChange():
    label.config(text=f"You Picked: {dateEntry.entry.get()}")


def showBox():
    calendar = Querybox()
    label.config(text=f"You Picked: {calendar.get_date()}")


root = tb.Window(themename="darkly")
root.title("DateEntry")
root.geometry("500x500")

# 用startdate設定初始日期
# dateEntry = tb.DateEntry(root, bootstyle='info', startdate=date(2023, 2, 14))
dateEntry = tb.DateEntry(root, bootstyle="info")
dateEntry.pack(pady=(50, 0))

button = tb.Button(
    root, text="Click", bootstyle="success outline", command=handleChange
)
button.pack(pady=(20, 0))

boxButton = tb.Button(root, text="Get Calendar", bootstyle="success", command=showBox)
boxButton.pack(pady=(20, 0))

label = tb.Label(root, text="You Picked: ")
label.pack(pady=(20, 0))

root.mainloop()

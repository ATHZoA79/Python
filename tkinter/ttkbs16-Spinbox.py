from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="darkly")
root.title("Spinbox")
root.geometry("500x350")


def spin():
    my_label.config(text=my_spin.get())


stuffs = ["Janu", "Febu", "Mar", "Aprl"]

my_spin = tb.Spinbox(
    root,
    bootstyle="info",
    font=("helvetica", 20),
    from_=0,
    to=10,
    values=stuffs,
    state="readonly",
)
my_spin.pack()

my_spin.set("Janu")

my_button = tb.Button(root, text="Click", command=spin)
my_button.pack()

my_label = tb.Label(root, text="", font=("helvetica", 18))
my_label.pack()

root.mainloop()

from tkinter import * 
import ttkbootstrap as tb

# Functions
def handleClick():
    title_label.config(text=f"You have clicked on {comboBox.get()}")
def handleChange(e):
    title_label.config(text=f"You have clicked on {comboBox.get()}")

# =================================

root = tb.Window(themename='darkly')

root.title('ComboBox is just select inputs')
root.geometry('500x350')

title_label = tb.Label(root, text='Hello', font=("Helvetica", 20))
title_label.pack(pady=(50, 20))

# Combobox values
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

comboBox = tb.Combobox(root, bootstyle='success', value=days)
comboBox.pack(pady=20)
# bind value change with function
comboBox.bind("<<ComboboxSelected>>", handleChange)

# Combobox Default value
comboBox.current(0)

# Create a Button to trigger combobox value change
button = tb.Button(root, text="Click to chane", command=handleClick, bootstyle="info")
button.pack()

root.mainloop()
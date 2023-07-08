from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="solar")
root.title("Menu Button")
root.geometry("500x350")


def setLabel(x):
    menu.config(text=x, bootstyle=x)


menu = tb.Menubutton(root, bootstyle="warning", text="Things")
menu.pack(pady=50)

inner_menu = tb.Menu(menu)

item_var = StringVar()
style_list = [
    "primary",
    "secondary",
    "danger",
    "info",
    "outline primary",
    "outline secondary",
    "outline danger",
]
for x in style_list:
    # use lambda to pass x into function
    # use x=x to prevent overwrite previous lambda function
    inner_menu.add_radiobutton(
        label=x, variable=item_var, command=lambda x=x: setLabel(x)
    )

menu["menu"] = inner_menu

root.mainloop()

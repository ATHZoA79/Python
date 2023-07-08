from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="darkly")
root.title("Radio Button")
root.geometry("500x550")


def handleClick():
    my_label.configure(text=f"{toppingVar.get()}")


toppings = ["Pepper", "Cheese", "Veggie"]
toppingVar = StringVar()

for topping in toppings:
    tb.Radiobutton(
        root,
        bootstyle="info",
        variable=toppingVar,
        text=topping,
        value=topping,
        command=handleClick,
    ).pack(pady=(10, 0))

button = tb.Button(root, text="click", command=handleClick)
button.pack(pady=20)

my_label = tb.Label(root, text="")
my_label.pack()

root.mainloop()

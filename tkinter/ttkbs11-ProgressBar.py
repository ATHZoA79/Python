from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="darkly")
root.title("Progress Bar")
root.geometry("500x350")


def increment():
    # progress.step(20)       # 超過上限會歸零
    progress["value"] += 20  # 可以加超過 100


progress = tb.Progressbar(
    root,
    bootstyle="success striped",
    maximum=100,
    mode="determinate",
    length=200,
    value=20,
)
progress.pack(pady=20)

frame = tb.Frame(root)
frame.pack(pady=20)

button = tb.Button(frame, text="+ 20", bootstyle="info outline", command=increment)
button.grid(column=0, row=0, padx=10)

style = tb.Style()
print(button.keys("cursor"))

root.mainloop()

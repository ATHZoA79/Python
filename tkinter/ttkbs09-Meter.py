from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="solar")
root.title("Menu Button")
root.geometry("500x550")

counter = 0


def handlePlus5():
    global counter
    counter += 5
    meter.configure(amountused=counter)


def stepUp():
    global counter
    meter.step(10)
    counter = meter.amountusedvar.get()


def stepDown():
    global counter
    meter.step(-10)
    counter = meter.amountusedvar.get()


meter = tb.Meter(
    root,
    bootstyle="success",
    subtext="Tkinter",
    interactive=TRUE,
    textright="%",
    metertype="semi",
    meterthickness=20,
    metersize=240,
    stripethickness=2,
)
meter.pack(pady=20)

plus5_tick_btn = tb.Button(root, text="Tick +5", command=handlePlus5)
plus5_tick_btn.pack(pady=(20, 0))
stepup_tick_btn = tb.Button(root, text="Step Up", command=stepUp)
stepup_tick_btn.pack(pady=(20, 0))
stepdown_tick_btn = tb.Button(root, text="Step Down", command=stepDown)
stepdown_tick_btn.pack(pady=(20, 0))

root.mainloop()

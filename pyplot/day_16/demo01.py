import tkinter as tk
import ttkbootstrap as tb
import pandas as pd
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)  # matplotlib 在 tkinter 的插件

csv = pd.read_csv("pyplot\day_16\data_table_1.csv", encoding="utf-8")
csv = csv.T.to_numpy()

# Plot
# plot, data = plt.subplots()
fig, ax = plt.subplots()
plot = ax.plot(csv[1], csv[3])


root = tk.Tk()
root.title("Matplot-TKinter")
root.geometry("500x550")

side_frame = tk.Frame(root, bg="#96B6C5")
side_frame.pack(side="left", fill="y")

sidebar_label = tk.Label(
    side_frame, text="Side Bar", bg="#96B6C5", fg="#F1F0E8", font=24
)
sidebar_label.pack(padx=20, pady=(10, 40), fill="x")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

canvas = FigureCanvasTkAgg(plot, master=main_frame)
canvas.set_canvas(canvas.get_tk_widget())
canvas.draw()
# canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

root.mainloop()

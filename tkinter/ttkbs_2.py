from tkinter import * 
import ttkbootstrap as tb

root = tb.Window(themename="darkly")
root.title("Ttk Style")
root.geometry("500x350")

# Create Style
custom_style = tb.Style().configure('success.TButton', font=("Helvetica", 24))

# Create Button
styled_button = tb.Button(text="Style It", bootstyle="success", style="success.TButton", width=24)
styled_button.pack(pady=20)

root.mainloop()
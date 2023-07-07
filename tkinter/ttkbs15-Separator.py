from tkinter import * 
import ttkbootstrap as tb 

root = tb.Window(themename='darkly')
root.title('Separator and Sizegrip')
root.geometry('500x350')

label_1 = tb.Label(root, text='Label 1', bootstyle='light')
label_1.pack(pady=(40, 0))

# Create separator (it's just a line <hr>)
sep =tb.Separator(root, bootstyle='info')
sep.pack(pady=10)

label_2 = tb.Label(root, text='Label 2', bootstyle='success')
label_2.pack(pady=(0, 40))

# A Sizegrip let you click and drag to resize window
sizegrip = tb.Sizegrip(root, bootstyle='info')
sizegrip.pack(anchor='se', expand=True)

root.mainloop()
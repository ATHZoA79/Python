from tkinter import * 
import ttkbootstrap as tb 

root = tb.Window(themename='darkly')
root.title('Scrollbar')
root.geometry('500x350')

# Frame for layout
my_frame = tb.Frame(root)
my_frame.pack(pady=(20,0))

# Create scrollbar
my_scroll = tb.Scrollbar(my_frame, orient='vertical', bootstyle="info round")
my_scroll.pack(side='right', fill=Y)

my_text = Text(my_frame, width=30, height=25, yscrollcommand=my_scroll.set, wrap='none', font=('helvetica',20))
my_text.pack()

my_scroll.config(command=my_text.yview)

root.mainloop();
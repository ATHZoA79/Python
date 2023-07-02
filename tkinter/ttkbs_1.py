from tkinter import * 
from ttkbootstrap.constants import * 
import ttkbootstrap as tb 

# Window Settings
# root = Tk() 
root = tb.Window(themename="darkly") # 給 window 套用 ttk 設定，而不用原始的Tk
root.title("Ttk Bootstrap")
root.geometry('500x350')

# Functions for button
title_toggled = False
def handleTitleChange() :
    global title_toggled
    if title_toggled is False:
        title_label.configure(text="GoodBye")
        title_toggled = True
    else:
        title_label.configure(text="Hello TtkBootstrap~")
        title_toggled = False

def handleCheck_1() :
    if var_1.get() == 1:
        title_label.configure(text="Checked")
    else :
        title_label.configure(text="Unchecked")

#Create a Label
# Add ttkbootstrap style by bootstyle attribute
title_label = tb.Label(text="Hello TtkBootstrap~", font=('Helvetics', 28), bootstyle='success')
title_label.pack(pady=50)

# Create a Button
change_button = tb.Button(text="Click Me", bootstyle="primary, outline", command=handleTitleChange)
change_button.pack(pady=20)

# Create CheckButton
var_1 = IntVar()
checkbox_1 = tb.Checkbutton(bootstyle="primary, round-toggle", text="check", variable=var_1, onvalue=1, offvalue=0, command=handleCheck_1)
checkbox_1.pack(pady=10)


root.mainloop()
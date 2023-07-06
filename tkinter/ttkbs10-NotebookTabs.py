from tkinter import * 
import ttkbootstrap as tb 

root = tb.Window(themename='solar')
root.title('Menu Button')
root.geometry('500x550')

notebook = tb.Notebook(root, bootstyle='dark')
notebook.pack(pady=(30, 0))

Tab1 = tb.Frame(notebook)
Tab2 = tb.Frame(notebook)

label = Label(Tab1, text='Label 1', font=("helvetica", 20))
label.pack(pady=(20, 0))

text = Text(Tab1, width=70, height=10)
text.pack(pady=10, padx=10)

button = tb.Button(Tab1, text='Click', bootstyle='danger')
button.pack(pady=20)

label2 = Label(Tab2, text='Label 2', font=("helvetica", 20))
label2.pack(pady=(20, 0))

notebook.add(Tab1, text='Tab 1')
notebook.add(Tab2, text='Tab 2')

root.mainloop()
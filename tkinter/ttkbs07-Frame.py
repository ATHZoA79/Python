from tkinter import * 
import ttkbootstrap as tb 

root = tb.Window(themename='darkly')
root.title('Frame can contain widgeits')
root.geometry('500x550')

customFrame = tb.Frame(root, bootstyle='dark')
customFrame.pack(side='top', fill='both')

entry = tb.Entry(customFrame, font=('Helvetica', 20))
entry.pack(pady=(20, 0))
button = tb.Button(customFrame, text='Click', bootstyle='light outline')
button.pack(pady=(20, 0))

root.mainloop()
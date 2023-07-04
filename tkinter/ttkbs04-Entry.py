from tkinter import * 
import ttkbootstrap as tb 

def handleSubmit():
  textLabel.config(text=f"You've Typed : {entry.get()}")

root = tb.Window(themename="darkly")
root.geometry('500x350')

entry = tb.Entry(root)
entry.pack(pady=(50,0))

button = tb.Button(root, bootstyle="success", text="Click", command=handleSubmit)
button.pack(pady=(20, 0))

textLabel = tb.Label(root, text="")
textLabel.pack(pady=(20, 0))

root.mainloop()
from tkinter import * 
import ttkbootstrap as tb 

def startCount():
  gauge.start()

root = tb.Window(themename='darkly')

root.title('Floodgauge')
root.geometry('500x550')

gauge = tb.Floodgauge(
  root, 
  bootstyle='info', 
  font=('Helvetica', 20), 
  mask="Pos:{}%", 
  maximum=100, 
  orient='horizontal', 
  value=10)
gauge.pack(padx=20, pady=(50, 0), fill='x')

button = tb.Button(root, text="Start", bootstyle="success outline", command=startCount)
button.pack(pady=(30, 0))

root.mainloop()

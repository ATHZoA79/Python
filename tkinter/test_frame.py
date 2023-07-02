import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Nested Frame Layout Example")
root.geometry("500x350")

# Create the outer Frame widget
outer_frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
outer_frame.pack(fill=tk.BOTH, expand=True)

# Create the inner Frame widgets
inner_frame1 = tk.Frame(outer_frame, bg="red", padx=5, pady=5)
inner_frame2 = tk.Frame(outer_frame, bg="blue", padx=5, pady=5)
inner_frame1.pack(side=tk.LEFT, fill="y", expand=True)
# inner_frame1.pack(side=tk.LEFT, fill=tk.BOTH)
inner_frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create widgets to be placed inside the inner Frame 1
label1 = tk.Label(inner_frame1, text="Label 1")
button1 = tk.Button(inner_frame1, text="Button 1")
label1.pack(padx=5, pady=5)
button1.pack(padx=5, pady=5)

# Create widgets to be placed inside the inner Frame 2
label2 = tk.Label(inner_frame2, text="Label 2")
button2 = tk.Button(inner_frame2, text="Button 2")
label2.pack(padx=5, pady=5)
button2.pack(padx=5, pady=5)

# Start the main event loop
root.mainloop()

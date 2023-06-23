import tkinter
import customtkinter
from pytube import YouTube

# define functions
def handleDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=handleProgress)
        video = ytObject.streams.get_lowest_resolution()
        video.download()
    except:
        print("Youtube Link Invalid")
    print("-- Download Complete --")

def handleProgress(stream, chunk, bytes_remaining):
    total_size = stream.file
    downloaded = total_size - bytes_remaining
    percentage = downloaded / total_size
    percentage_text = str(int(percentage))  # get rid of number after dot
    progressBar.configure(text=percentage_text+"%")
    progressBar.update()

# System setting
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader")

# Create UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link", font=("Arial", 18))
title.grid(row=0, column=0, padx=20, pady=20, sticky=customtkinter.W)

## Input box
url_var = customtkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.grid(row=0, column=1, padx=(0, 0), sticky="w")

#@ Download Button
download_button = customtkinter.CTkButton(app, text="Download", width=80, command=handleDownload)
download_button.grid(row=0, column=2, padx=(10, 0), sticky="w")

# Download Progress Bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.grid(row=1, column=0, columnspan=3)

# App loop to keep window and codes run
app.mainloop()
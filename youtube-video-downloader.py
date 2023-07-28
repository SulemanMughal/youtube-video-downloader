from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry("350x200")
root.title("Youtube Video Downloader")
def download():
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.get_highest_resolution().download()
        link.set("Video downloaded successfully")
    except Exception as e:
        print(e)
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")
myVar = StringVar()
myVar.set("Enter the link below")
Entry(root, textvariable=myVar, width=40).pack(pady=10)
link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)
Button(root, text="Download video", command=download).pack()
root.mainloop()
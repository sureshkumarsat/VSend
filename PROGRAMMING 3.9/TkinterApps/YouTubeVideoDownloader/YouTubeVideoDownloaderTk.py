import os
import tkinter as tk
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
import shutil

master = tk.Tk()
master.title("Youtube Video Downloader")
master.iconbitmap("TkinterApps\\YouTubeVideoDownloader\\YtVidDownloaderIcon.ico")
master.resizable(0, 0)
master.configure(bg="#808080")


def Browse():
    if PathEntry.get().isspace() or PathEntry.get() == "" or PathEntry.get() == None:
        download_dir = tk.filedialog.askdirectory(
            initialdir=os.path.join(os.path.expanduser("~"), "Downloads")
        )
    else:
        download_dir = tk.filedialog.askdirectory(initialdir=PathEntry.get())
    PathEntry.delete("0", "end")
    PathEntry.insert("end", download_dir)
    if PathEntry.get().isspace() or PathEntry.get() == "" or PathEntry.get() == None:
        PathEntry.insert("end", f'{os.path.join(os.path.expanduser("~"), "Downloads")}')


def Download():
    try:
        video_link = LinkEntry.get()
        get_video = YouTube(video_link)
        get_stream = get_video.streams.first()
        DownloadedFile = get_stream.download()
        folder = PathEntry.get()
        OldFileName = DownloadedFile.split("\\")[-1]
        NewFileName = f"{SaveAsEntry.get()}.mp4"
        if NewFileName.isspace() or NewFileName == "" or NewFileName == None:
            NewFileName = OldFileName
        path = os.path.join(folder, NewFileName)
        os.rename(DownloadedFile, DownloadedFile.replace(OldFileName, NewFileName))
        tempLabel = tk.Label(
            master,
            text=f"{NewFileName} can be found in \n{path}",
            font=("Cascadia Code PL", 14),
            bg="#000055",
            fg="gray",
        )
        tempLabel.grid(row=5, column=0, padx=10, pady=10, columnspan=3)
    except Exception as e:
        tempLabel = tk.Label(
            master,
            text=f"Error Encountered: {e}",
            font=("Cascadia Code PL", 14),
            bg="#000055",
            fg="gray",
        )
        tempLabel.grid(row=5, column=0, padx=10, pady=10, columnspan=3)
    LinkEntry.delete(0, "end")
    SaveAsEntry.delete(0, "end")
    tempLabel.destroy()
    shutil.move(NewFileName, folder)
    os.chdir(folder)
    os.startfile(f"{NewFileName}")
    master.update_idletasks()


LinkLabel = tk.Label(
    master,
    text="Enter Link : ",
    fg="#ffff80",
    bg="black",
    font=("Cascadia Code PL", 16),
)
LinkLabel.grid(row=0, column=0, padx=10, pady=10)
LinkEntry = tk.Entry(
    master,
    fg="white",
    bg="black",
    font=("Cascadia Code PL", 16),
    width=36,
    insertbackground="#ff4040",
)
LinkEntry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
LinkEntry.focus()

PathLabel = tk.Label(
    master,
    text="Enter Path : ",
    fg="#ffff80",
    bg="black",
    font=("Cascadia Code PL", 16),
)
PathLabel.grid(row=1, column=0, padx=10, pady=10)
PathEntry = tk.Entry(
    master,
    fg="white",
    bg="black",
    font=("Cascadia Code PL", 16),
    width=25,
    insertbackground="#ff4040",
)
PathEntry.grid(row=1, column=1, padx=10, pady=10)
PathEntry.insert("end", os.path.join(os.path.expanduser("~"), "Downloads"))

BrowseButton = tk.Button(
    master,
    text="  Browse  ",
    fg="black",
    bg="#ffff80",
    font=("Cascadia Code PL", 12),
    command=Browse,
)
BrowseButton.grid(row=1, column=2, padx=10, pady=10)

SaveAsLabel = tk.Label(
    master,
    text="Save As    : ",
    fg="#ffff80",
    bg="black",
    font=("Cascadia Code PL", 16),
)
SaveAsLabel.grid(row=2, column=0, padx=10, pady=10)
SaveAsEntry = tk.Entry(
    master,
    fg="white",
    bg="black",
    font=("Cascadia Code PL", 16),
    width=25,
    insertbackground="#ff4040",
)
SaveAsEntry.grid(row=2, column=1, padx=10, pady=10)
SaveAsEntry.focus()

DownLoadButton = tk.Button(
    master,
    text=" Download Video ",
    fg="black",
    bg="#ffff80",
    font=("Cascadia Code PL", 12),
    command=Download,
)
DownLoadButton.grid(row=3, column=1, padx=10, pady=10)


master.mainloop()

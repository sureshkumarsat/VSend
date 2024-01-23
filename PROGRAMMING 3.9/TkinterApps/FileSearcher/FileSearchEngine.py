import tkinter as tk
from ttkwidgets import AutoHideScrollbar
import fnmatch
import os
import win32api


master = tk.Tk()
master.title("File Search Engine")
# master.iconbitmap("TkinterApps\\YouTubeVideoDownloader\\YtVidDownloaderIcon.ico")
master.resizable(0, 0)
master.configure(bg="#808080")

global DriveSelected


def LoadIndex(path):
    global DriveList
    DriveList = os.walk(DriveSelected.get())
    return DriveList


def GetData(pattern):
    global DriveList
    result = []
    for root, dirs, files in DriveList:
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def CreateList(TypedName):
    Name = SearchByNameEntry.get()
    if TypedName == "":
        FilesList.delete(0, "end")
    else:
        ListOfFiles = GetData(f"{Name}.*")
        for i in ListOfFiles:
            FilesList.insert("end", i)


SelectDriveLabel = tk.Label(
    master,
    text="  Select Main Drive To Search     : ",
    fg="#ffff80",
    bg="black",
    font=("Cascadia Code PL", 16),
)
SelectDriveLabel.grid(row=0, column=0, columnspan=2, pady=10)


drive = win32api.GetLogicalDriveStrings()
drives = drive.split("\000")[:-1]

DriveSelected = tk.StringVar()
DriveSelected.set(drives[0])

DriveDropdown = tk.OptionMenu(master, DriveSelected, *drives, command=LoadIndex)
DriveDropdown.grid(row=0, column=2, pady=10)

DriveList = os.walk(DriveSelected.get())


SearchByNameEntry = tk.Entry(
    master,
    fg="white",
    bg="black",
    font=("Cascadia Code PL", 16),
    width=36,
    insertbackground="#ff4040",
)
# SearchByNameEntry.insert("end", "Search By Name...")
SearchByNameEntry.grid(row=1, column=0, columnspan=2, pady=10, padx=10)


SearchByExtEntry = tk.Entry(
    master,
    fg="white",
    bg="black",
    font=("Cascadia Code PL", 16),
    width=24,
    insertbackground="#ff4040",
)
# SearchByExtEntry.insert("end", "Search By File Type...")
SearchByExtEntry.grid(row=1, column=2, pady=10, padx=10)


FilesListFrame = tk.Frame(master)

ScrollBar_List = tk.Scrollbar(FilesListFrame, orient="vertical")

FilesList = tk.Listbox(
    FilesListFrame,
    height=10,
    width=80,
    fg="#ffff80",
    bg="black",
    font=("Cascadia Code PL", 16),
    yscrollcommand=ScrollBar_List.set,
)

ScrollBar_List.config(command=FilesList.yview)
ScrollBar_List.pack(side="right", fill="y")
FilesList.pack()

FilesListFrame.grid(row=2, column=0, columnspan=3, pady=10, padx=10)


SearchByNameEntry.bind("<KeyRelease>", CreateList(SearchByNameEntry.get()))


master.mainloop()

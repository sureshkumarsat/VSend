from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '350')
Config.set('kivy','window_icon','APPLICATIONS\\YOUTUBE VIDEO DOWNLOADER\\YtVidDownloaderIcon.ico')
import os
import shutil
from pytube import YouTube
import youtube_dl
from plyer import filechooser
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
import win32api


class WOXApp(MDApp):

    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]

    def build(self):
        self.title = "Youtube Video Downloader"
        self.buildesh = Builder.load_file('APPLICATIONS\\YOUTUBE VIDEO DOWNLOADER\\YT-MP3-MP4.kv')
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Blue'
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            search = 'dirs'
        )
        menu_items = []
        for i in self.drives:
            menu_items.append(
                {
                    "viewclass": "MDMenuItem",
                    "text": i
                }
            )
        self.dd_menu = MDDropdownMenu(
            caller = self.buildesh.ids.Path,
            items = menu_items,
            width_mult = 4
        )
        self.dd_menu.bind(on_release = self.option_callback)
        return self.buildesh

    def on_start(self):
        self.buildesh.ids.Path.text = os.path.join(os.path.expanduser('~'), 'Downloads')

    def option_callback(self, instance_menu, instance_menu_item):
        print(instance_menu_item.text)
        self.buildesh.ids.Path.text = instance_menu_item.text
        self.dd_menu.dismiss()

    def Browse(self):
        pathesh = self.buildesh.ids.Path.text
        self.file_manager.show(f'{pathesh}')

    def exit_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        self.exit_manager()
        self.buildesh.ids.Path.text = path
        toast(path)

    def Download(self):
        try:
            video_link = self.buildesh.ids.Link.text
            get_video = YouTube(video_link)
            get_stream = get_video.streams.first()
            DownloadedFile = get_stream.download()
            folder = self.buildesh.ids.Path.text
            OldFileName = DownloadedFile.split("\\")[-1]
            NewFileName = f"{self.buildesh.ids.FileName.text}.mp4"
            if NewFileName.isspace():
                NewFileName = OldFileName
            os.rename(DownloadedFile, DownloadedFile.replace(OldFileName, NewFileName))
            shutil.move(NewFileName, folder)
            os.chdir(folder)
            os.startfile(f'{NewFileName}')
            print(f"{video_link}\n{folder}\n{NewFileName}")
            toast(f"Download successful!!!\nThe video has been downloaded successfully in the provided directory in the given name.")
        except Exception as e:
            toast(f"Download Error\nEncountered Error:\n{e}\nwhile downloading the video.")
        self.buildesh.ids.Link.text = ""
        self.buildesh.ids.FileName.text = ""

    def DownloadAudio(self):
        try:
            audio_url = self.buildesh.ids.Link.text
            audio_info = youtube_dl.YoutubeDL().extract_info(url=audio_url, download=False)
            folder = self.buildesh.ids.Path.text
            NewFileName = self.buildesh.ids.FileName.text
            filename = f"{audio_info['title']}.mp3"
            if NewFileName.isspace():
                pass
            else:
                filename = f"{NewFileName}.mp3"
            options = {
                "format": "bestaudio/best",
                "keepvideo": False,
                "outtmpl": filename,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }]
            }
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([audio_info['webpage_url']])
            shutil.move(filename, folder)
            os.chdir(folder)
            os.startfile(filename)
            print(f"{audio_url}\n{folder}\n{NewFileName}")
            toast(f"Download successful\nThe video has been downloaded successfully in the provided directory in the given name.")
        except Exception as e:
            toast(f"Download Error\nEncountered Error:\n{e}\nwhile downloading the audio.")
        self.buildesh.ids.Link.text = ""
        self.buildesh.ids.FileName.text = ""


WOXApp().run()
from kivy.config import Config
Config.set('graphics', 'resizable', '0') 
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '400')
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


screen = '''
Screen:
    id: MainScreen
    name: 'MainScreen'

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'ENVIRONMENT VARIABLES'
            anchor_title: 'center'
        ScrollView:
            MDList:
                id: env_var_list
'''


class WOXApp(MDApp):

    def build(self):
        self.title = "ENVIRONMENT VARIABLES"
        self.buildesh = Builder.load_string(screen)
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Blue'
        return self.buildesh

    def on_start(self):
        pass


WOXApp().run()
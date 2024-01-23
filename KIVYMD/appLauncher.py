from kivy.config import Config
Config.set('graphics', 'resizable', '0') 
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
# Config.set('kivy','window_icon','APPLICATIONS\\YOUTUBE VIDEO DOWNLOADER\\YtVidDownloaderIcon.ico')
import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
import json
import webbrowser
import time
import pyautogui as pag


screen = '''
Screen:
    id: MainScreen
    name: 'MainScreen'

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'APP LAUNCHER'
            anchor_title: 'center'
        ScrollView:

    MDFloatingActionButton:
        id: Terminals
        icon: "google-controller"
        elevation_normal: 12
        pos_hint: {"center_x": 0.3 ,"center_y": 0.7}
        font_size: "64sp"
        on_press: app.open_bottom_sheet("Terminals")

    MDFloatingActionButton:
        id: Browsers
        icon: "web"
        elevation_normal: 12
        pos_hint: {"center_x": 0.7 ,"center_y": 0.7}
        font_size: "64sp"
        on_press: app.open_bottom_sheet("Browsers")

    MDFloatingActionButton:
        id: CodeEditors
        icon: "brain"
        elevation_normal: 12
        pos_hint: {"center_x": 0.3 ,"center_y": 0.45}
        font_size: "64sp"
        on_press: app.open_bottom_sheet("Code Editors And IDE's")

    MDFloatingActionButton:
        id: Essentials
        icon: "menu"
        elevation_normal: 12
        pos_hint: {"center_x": 0.7 ,"center_y": 0.45}
        font_size: "64sp"
        on_press: app.open_bottom_sheet("Essentials")

    MDFloatingActionButton:
        id: MicrosoftOffice
        icon: "microsoft"
        elevation_normal: 12
        pos_hint: {"center_x": 0.3 ,"center_y": 0.2}
        font_size: "64sp"
        on_press: app.open_bottom_sheet("Microsoft Office")

    MDFloatingActionButton:
        id: MyApps
        icon: "apps"
        elevation_normal: 12
        pos_hint: {"center_x": 0.7 ,"center_y": 0.2}
        font_size: "64sp"
        on_press: app.open_bottom_sheet("My Apps")
'''


class WOXApp(MDApp):

    apps = {
        "Terminals": {
            "Command Prompt": "apple-keyboard-command",
            "Windows Powershell": "powershell",
            "Git Bash": "git",
            "Windows Terminal": "microsoft-windows"
        },
        "Browsers": {
            "Google Chrome": "google-chrome",
            "Firefox": "firefox",
            "Brave": "language-html5"
        },
        "Code Editors And IDE's": {
            "Sublime Text 3": "language css3",
            "Visual Studio Code": "microsoft-visual-studio-code",
            "Atom": "atom",
            "PyCharm": "language-python",
            "NotePad++": "notebook-plus",
            "IDLE 3.8": "spider",
            "Android Studio": "android-studio"
        },
        "Essentials": {
            "Franz": "instagram",
            "Spotify": "spotify",
            "File Explorer": "folder-multiple",
            "NotePad": "note-text",
            "Zoom": "video",
            "Discord": "discord"
        },
        "Microsoft Office": {
            "Microsoft Word": "microsoft-word",
            "Microsoft PowerPoint": "microsoft-powerpoint",
            "Microsoft Excel": "microsoft-excel"
        },
        "My Apps": {
            "My Browser": "web",
            "YouTube Downloader": "youtube"
        }
    }

    def build(self):
        self.title = "App Launcher"
        self.buildesh = Builder.load_string(screen)
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Blue'
        return self.buildesh

    def open_bottom_sheet(self, category=None):
        bottom_sheet_menu = MDGridBottomSheet()
        data = self.apps[category]
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.OpenFile(app=y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def OpenFile(self, app=None):
        if app == "EverNote" or app == "Snipping Tool":
            pag.hotkey('winleft')
            time.sleep(1)
            pag.typewrite(app)
            time.sleep(1)
            pag.hotkey('enter')

        else:
            with open('apps.json') as apps:
                data = json.load(apps)
            for i in data.keys():
                for j in data[i].keys():
                    if app == j:
                        os.startfile(data[i][j])


WOXApp().run()
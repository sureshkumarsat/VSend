from kivymd.app import MDApp
from kivy.lang import Builder


screen = '''
Screen:
    name: "MainScreen"
    id: MainScreen
'''


class MP3(MDApp):
    def build(self):
        return Builder.load_string(screen)


MP3().run()
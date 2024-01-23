from kivy.config import Config
Config.set('graphics', 'resizable', '0') 
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '300')
# Config.set('kivy','window_icon','YtVidDownloaderIcon.ico')
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivymd.uix.card import MDSeparator
from kivymd.uix.label import MDLabel
from PyDictionary import PyDictionary


Mainscreen = '''
Screen:
    id: main_screen
    name: "main_screen"

    MDLabel:
        text: 'DICTIONARY'
        font_size: 32
        font_style: "H6"
        theme_text_color: "Custom"
        color: 1, 1, 1, 1
        size_hint_x: 0.8
        pos_hint: {"center_x": 0.78, "center_y": 0.8}

    MDTextField:
        id: word
        text: ''
        size_hint_x: 0.604
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        hint_text: "Enter Word"
        helper_text: "Enter The Word For Which You Want To Search The Meaning For"
        helper_text_mode: "on_focus"
        font_size: 28

    MDIconButton:
        id: iconbutton
        icon: "magnify"
        size_hint_x: 0.8
        pos_hint: {"center_x": 0.78, "center_y": 0.62}

    MDRaisedButton:
        text: "FIND SYNONYM"
        bold: True
        size_hint_x: 0.4
        pos_hint: {"center_x": 0.298, "center_y": 0.4}
        on_release: app.find_synonym()

    MDRaisedButton:
        text: "FIND ANTONYM"
        bold: True
        size_hint_x: 0.4
        pos_hint: {"center_x": 0.702, "center_y": 0.4}
        on_release: app.find_antonym()
'''


Meaningsscreen = '''
Screen:
    id: meaning_screen
    name: "meaning_screen"

    MDIconButton:
        icon: "backburger"
        on_release: app.backburger("MeaningScreen")
        pos_hint: {"center_x": 0.04, "center_y": 0.95}

    ScrollView:
        id: scroller_synonym
        pos_hint: {"center_x": 0.5 ,"center_y": 0.45}
        size_hint: 0.9, 0.8
'''


Antonymsscreen = '''
Screen:
    id: antonym_screen
    name: "antonym_screen"

    MDIconButton:
        icon: "backburger"
        on_release: app.backburger("AntonymScreen")
        pos_hint: {"center_x": 0.04, "center_y": 0.95}

    ScrollView:
        id: scroller_antonym
        pos_hint: {"center_x": 0.5 ,"center_y": 0.4}
        size_hint: 0.9, 0.8
'''


class DictionaryApp(MDApp):
    def build(self):
        self.title = "Dictionary"
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Blue'
        self.dictionary = PyDictionary()
        self.screen_manager = ScreenManager(transition = SlideTransition())
        self.MainScreen = Builder.load_string(Mainscreen)
        self.MeaningScreen = Builder.load_string(Meaningsscreen)
        self.AntonymScreen = Builder.load_string(Antonymsscreen)
        self.screen_manager.add_widget(self.MainScreen)
        self.screen_manager.add_widget(self.MeaningScreen)
        self.screen_manager.add_widget(self.AntonymScreen)
        self.screen_manager.current = "main_screen"
        return self.screen_manager

    def find_synonym(self):
        word = self.MainScreen.ids.word.text.capitalize()
        meaning = self.dictionary.meaning(word)
        print(meaning)
        text_meaning = ""
        for i in meaning.keys():
            text_meaning += f"{i}:\n"
            for j in range(0, len(meaning[i])):
                text_meaning += f"{j+1}. {meaning[i][j]}.\n"
        self.screen_manager.current = "meaning_screen"
        self.title_label = MDLabel(
            text = word,
            halign = "center",
            size_hint_y = None,
            font_size = 32,
            font_style = "H6",
            pos_hint = {"center_x": 0.5, "center_y": 0.9}
        )
        self.body_label = MDLabel(
            text = text_meaning,
            halign = "center",
            size_hint_y = None,
            font_size = 28,
            font_style = "H6",
        )
        self.MeaningScreen.add_widget(self.title_label)
        self.MeaningScreen.ids.scroller_synonym.add_widget(self.body_label)

    def find_antonym(self):
        word = self.MainScreen.ids.word.text.capitalize()
        antonym = self.dictionary.antonym(word)
        print(antonym)
        text_antonym = ""
        for i in range(0, len(antonym)):
            text_antonym += f"{i+1}. {antonym[i]}.\n"
        self.screen_manager.current = "antonym_screen"
        self.title_label = MDLabel(
            text = word,
            halign = "center",
            size_hint_y = None,
            font_size = 32,
            font_style = "H6",
            pos_hint = {"center_x": 0.5, "center_y": 0.9}
        )
        self.body_label = MDLabel(
            text = text_antonym,
            halign = "center",
            size_hint_y = None,
            font_size = 28,
            font_style = "H6",
        )
        self.AntonymScreen.add_widget(self.title_label)
        self.AntonymScreen.ids.scroller_antonym.add_widget(self.body_label)

    def backburger(self, screen):
        self.screen_manager.transition = SlideTransition(direction = 'right')
        if screen == "MeaningScreen":
            self.MeaningScreen.remove_widget(self.title_label)
            self.MeaningScreen.ids.scroller_synonym.remove_widget(self.body_label)
        if screen == "AntonymScreen":
            self.AntonymScreen.remove_widget(self.title_label)
            self.AntonymScreen.ids.scroller_antonym.remove_widget(self.body_label)
        self.screen_manager.current = "main_screen"
        self.MainScreen.ids.word.text = ''
        self.screen_manager.transition = SlideTransition(direction = 'left')


DictionaryApp().run()
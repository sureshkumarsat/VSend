from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '500')
# Config.set('kivy','window_icon','YtVidDownloaderIcon.ico')
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem
import webbrowser
import json
import os
import fnmatch
import pickle
import wikipedia


screen = '''
Screen:
    id: MainScreen
    name: 'MainScreen'

    MDBottomNavigation:

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'GOOGLE'
            icon: 'google'

            MDIconButton:
                icon: 'google'
                user_font_size: '64sp'
                pos_hint: {"center_x": 0.5, "center_y": 0.8}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDTextField:
                id: search_google
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
                size_hint_x: 0.8
                hint_text: 'Search Google'
                font_size: '24sp'

            MDIconButton:
                id: search_button_google
                icon: 'magnify'
                pos_hint: {"center_x": 0.88, "center_y": 0.62}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release: app.search_google()

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'YOUTUBE'
            icon: 'youtube'

            MDIconButton:
                icon: 'youtube'
                user_font_size: '64sp'
                pos_hint: {"center_x": 0.5, "center_y": 0.8}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDTextField:
                id: search_youtube
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
                size_hint_x: 0.8
                hint_text: 'Search Youtube'
                font_size: '24sp'

            MDIconButton:
                id: search_button_youtube
                icon: 'magnify'
                pos_hint: {"center_x": 0.88, "center_y": 0.62}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release: app.search_youtube()

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'WIKIPEDIA'
            icon: 'wikipedia'

            MDIconButton:
                icon: 'wikipedia'
                user_font_size: '64sp'
                pos_hint: {"center_x": 0.5, "center_y": 0.9}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDTextField:
                id: search_wikipedia
                pos_hint: {"center_x": 0.5, "center_y": 0.8}
                size_hint_x: 0.8
                hint_text: 'Search Wikipedia'
                font_size: '24sp'

            MDIconButton:
                id: search_button_wikipedia
                icon: 'magnify'
                pos_hint: {"center_x": 0.88, "center_y": 0.82}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release: app.search_wikipedia()

            MDTextFieldRect:
                id: result_wikipedia
                size_hint: 0.8, 0.7
                pos_hint: {"center_x": 0.5, "center_y": 0.4}

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'GITHUB'
            icon: 'github'

            MDIconButton:
                icon: 'github'
                user_font_size: '64sp'
                pos_hint: {"center_x": 0.5, "center_y": 0.8}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDTextField:
                id: search_github
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
                size_hint_x: 0.8
                hint_text: 'Search Github'
                font_size: '24sp'

            MDIconButton:
                id: search_button_github
                icon: 'magnify'
                pos_hint: {"center_x": 0.88, "center_y": 0.62}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

        MDBottomNavigationItem:
            name: 'screen 5'
            text: 'STACK OVERFLOW'
            icon: 'stack-overflow'

            MDIconButton:
                icon: 'stack-overflow'
                user_font_size: '64sp'
                pos_hint: {"center_x": 0.5, "center_y": 0.8}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDTextField:
                id: search_stackoverflow
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
                size_hint_x: 0.8
                hint_text: 'Search Stack Overflow'
                font_size: '24sp'

            MDIconButton:
                id: search_button_stackoverflow
                icon: 'magnify'
                pos_hint: {"center_x": 0.88, "center_y": 0.62}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

        MDBottomNavigationItem:
            name: 'screen 6'
            text: 'FILES / FOLDERS'
            icon: 'google-drive'

            MDIconButton:
                icon: 'google-drive'
                user_font_size: '64sp'
                pos_hint: {"center_x": 0.5, "center_y": 0.8}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDTextField:
                id: search_filesnfolders
                pos_hint: {"center_x": 0.4, "center_y": 0.6}
                size_hint_x: 0.6
                hint_text: 'Search Files'
                font_size: '24sp'
                on_text: app.spontaneous_search()

            MDIconButton:
                id: search_button_filesnfolders
                icon: 'magnify'
                pos_hint: {"center_x": 0.7, "center_y": 0.62}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatIconButton:
                id: button
                icon: 'google-drive'
                text: 'All Files'
                on_release: app.menu.open()
                pos_hint: {"center_x": 0.8, "center_y": 0.62}
                size_hint: None, None

            ScrollView:
                pos_hint: {"center_x": 0.5, "center_y": 0.3}
                size_hint: 0.8, 0.4
                MDList:
                    id: file_search_results
'''


# class SearchEngine:
#     ''' Create a search engine object '''

#     def __init__(self):
#         self.file_index = [] # directory listing returned by os.walk()
#         self.results = [] # search results returned from search method
#         self.matches = 0 # count of records matched
#         self.records = 0 # count of records searched


#     def create_new_index(self, values: Dict[str, str]) -> None:
#         ''' Create a new file index of the root; then save to self.file_index and to pickle file '''
#         root_path = values['PATH']
#         self.file_index: list = [(root, files) for root, dirs, files in os.walk(root_path) if files]

#         # save index to file
#         with open('file_index.pkl','wb') as f:
#             pickle.dump(self.file_index, f)


#     def load_existing_index(self) -> None:
#         ''' Load an existing file index into the program '''
#         try:
#             with open('file_index.pkl','rb') as f:
#                 self.file_index = pickle.load(f)
#         except:
#             self.file_index = []


#     def search(self, values: Dict[str, str]) -> None:
#         ''' Search for the term based on the type in the index; the types of search
#             include: contains, startswith, endswith; save the results to file '''
#         self.results.clear()
#         self.matches = 0
#         self.records = 0
#         term = values['TERM']

#         # search for matches and count results
#         for path, files in self.file_index:
#             for file in files:
#                 self.records +=1
#                 if (values['CONTAINS'] and term.lower() in file.lower() or 
#                     values['STARTSWITH'] and file.lower().startswith(term.lower()) or 
#                     values['ENDSWITH'] and file.lower().endswith(term.lower())):

#                     result = path.replace('\\','/') + '/' + file
#                     self.results.append(result)
#                     self.matches +=1
#                 else:
#                     continue 
        
#         # save results to file
#         with open('search_results.txt','w') as f:
#             for row in self.results:
#                 f.write(row + '\n')


class Browser(MDApp):

    google_url = "https://google.com/search?q="
    youtube_url = "https:/youtube.com/results?search_query="
    FileType = "*"

    with open('file_ext.json', 'r') as ext:
        file_extensions = json.load(ext)

    def build(self):
        self.title = "MY BROWSER"
        self.buildesh = Builder.load_string(screen)
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Blue'
        menu_items = [{"text": f'{i}'} for i in self.file_extensions.keys()]
        self.menu = MDDropdownMenu(
            caller=self.buildesh.ids.button,
            items=menu_items,
            width_mult=4,
        )
        self.menu.bind(on_release=self.menu_callback)
        return self.buildesh

    def menu_callback(self, instance_menu, instance_menu_item):
        self.buildesh.ids.button.text = instance_menu_item.text
        self.menu.dismiss()
        self.FileType = f'{self.file_extensions[instance_menu_item.text]}'

    def search_google(self):
        url = self.google_url
        query = self.buildesh.ids.search_google.text
        words = query.split()
        for i in range(0, len(words)):
            if i < len(words) - 1:
                url += f'{words[i]}+'
            else:
                url += f'{words[i]}'
        webbrowser.open(url)

    def search_youtube(self):
        url = self.youtube_url
        query = self.buildesh.ids.search_youtube.text
        words = query.split()
        for i in range(0, len(words)):
            if i < len(words) - 1:
                url += f'{words[i]}+'
            else:
                url += f'{words[i]}'
        webbrowser.open(url)

    # def find(self, pattern, path):
    #     result = []
    #     for root, dirs, files in self.index:
    #         for name in files:
    #             if fnmatch.fnmatch(name, pattern):
    #                 result.append(os.path.join(root, name))
    #     return result

    # def spontaneous_search(self):
    #     self.buildesh.ids.file_search_results.clear_widgets()
    #     print(self.FileType)
    #     print(self.buildesh.ids.search_filesnfolders.text)
    #     result = self.find(f'{self.buildesh.ids.search_filesnfolders.text}*.{self.FileType}', 'D:\\')
    #     for i in range(0, len(result)):
    #         item = OneLineListItem(text = f'{result[i]}')
    #         self.buildesh.ids.file_search_results.add_widget(item)

    def search_wikipedia(self):
        query = self.buildesh.ids.search_wikipedia.text
        try:
            data = wikipedia.page(query)
            self.buildesh.ids.result_wikipedia.text = data.content
        except Exception as e:
            self.buildesh.ids.result_wikipedia.text = f"{e}"


Browser().run()
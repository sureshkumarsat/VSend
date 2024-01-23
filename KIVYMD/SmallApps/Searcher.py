from kivymd.app import MDApp
from kivy.lang import Builder
from selenium import webdriver
import pyautogui as pag


screen = '''
Screen:
    MDTextField:
        id: Browser
        pos_hint: {"center_x":0.5, "center_y":0.6}
        size_hint_x: 0.9
        hint_text: "Search"
        helper_text: "Enter your query"
        helper_text_mode: "on_focus"
        color_active: app.theme_cls.primary_color
        font_size: 20

    MDIconButton:
        icon: "magnify"
        icon_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.95, "center_y":0.62}
        on_press: app.gen_search()
        font_size: 20

    MDList:
        id: listi
        size_hint_x: 0.9
        pos_hint: {"center_x": 0.5}

        ThreeLineIconListItem:
            text: "Google"
            secondary_text: "g <query>"
            tertiary_text: "Opens the <query> in Google"
            on_press: app.prefix_it("Google")
            IconLeftWidget:
                icon: "google"

        ThreeLineIconListItem:
            text: "YouTube"
            secondary_text: "yt <query>"
            tertiary_text: "Opens the <query> in YouTube"
            on_press: app.prefix_it("YouTube")
            IconLeftWidget:
                icon: "youtube"

        ThreeLineIconListItem:
            text: "Wikipedia"
            secondary_text: "wiki <query>"
            tertiary_text: "Opens the <query> in Wikipedia"
            on_press: app.prefix_it("Wikipedia")
            IconLeftWidget:
                icon: "wikipedia"

'''


class WOXApp(MDApp):
    def build(self):
        self.title = 'WOX'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.TheApp = Builder.load_string(screen)
        return self.TheApp

    def prefix_it(self, site):
        if site == "Google":
            self.TheApp.ids.Browser.text = 'g '
        if site == "YouTube":
            self.TheApp.ids.Browser.text = 'yt '
        if site == "Wikipedia":
            self.TheApp.ids.Browser.text = 'wiki '

    def gen_search(self):
        query = self.TheApp.ids.Browser.text
        if query.startswith('g '):
            query = query.replace('g ', '')

            browser = webdriver.Chrome()
            browser.get('https://www.google.com')

            search_box = browser.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
            search_box.send_keys(query)

            pag.press('Enter')

        if query.startswith('yt '):
            query = query.replace('yt ', '')

            browser = webdriver.Chrome()
            browser.get('https://www.youtube.com')

            search_box = browser.find_element_by_xpath('//*[@id="search"]')
            search_box.send_keys(query)

            search_button = browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button/yt-icon')
            search_button.click()

        self.TheApp.ids.Browser.text = ""
WOXApp().run()
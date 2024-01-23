from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '300')
Config.set('kivy','window_icon','APPLICATIONS\\URL SHORTENER\\URL_SHORTENER_ICON.ico')
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
import pyshorteners
import pyperclip


class URLshortener(MDApp):

    URL_Shortener = pyshorteners.Shortener()

    def build(self):
        self.title = "URL SHORTENER"
        self.buildesh = Builder.load_file('APPLICATIONS\\URL SHORTENER\\URL_shortener.kv')
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Blue'
        return self.buildesh

    def create_short_URL(self):
        long_link = self.buildesh.ids.long_link.text
        try:
            shortened_URL = self.URL_Shortener.tinyurl.short(long_link)
            self.buildesh.ids.short_url.text = f"[ref=shortlink]{shortened_URL}[/ref]"
            self.buildesh.ids.short_url.markup = True
            toast('New shortened link has been created.')
        except Exception as e:
            toast(f'Error Encountered : {e}')

    def copy_short_link(self):
        try:
            short_link_raw = self.buildesh.ids.short_url.text
            short_link_refined1 = short_link_raw.replace('[ref=shortlink]', '')
            short_link = short_link_refined1.replace('[/ref]', '')
            try:
                pyperclip.copy(short_link)
                toast(f'{short_link} has been copied to clipboard')
            except Exception as e:
                toast(f'Error Encountered : {e}')
        except Exception as e:
            toast(f'Error Encountered : {e}')


URLshortener().run()

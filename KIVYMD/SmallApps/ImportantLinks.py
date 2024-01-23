from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '400')
# Config.set('kivy','window_icon','YtVidDownloaderIcon.ico')
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty


screen = '''
<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height

    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            # on_release: app.remove_alarm(root)

    MDCardSwipeFrontBox:

        TwoLineListItem:
            id: content
            text: root.text
            secondary_text: root.secondary_text
            on_press: print(content.text)


Screen:
    id: MainScreen
    name: 'MainScreen'

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'IMPORTANT LINKS'
            anchor_title: 'center'
        ScrollView:
            MDList:
                SwipeToDeleteItem:
                SwipeToDeleteItem:
                SwipeToDeleteItem:
                SwipeToDeleteItem:
                SwipeToDeleteItem:
                SwipeToDeleteItem:
                SwipeToDeleteItem:
        MDFloatingActionButton:
            id: add_link
            icon: "plus-thick"
            pos_hint: {"center_x": 0.9, "center_y": 0.15}


'''


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    secondary_text = StringProperty()


class ImportantLinks(MDApp):

    def build(self):
        self.title = "URL SHORTENER"
        self.buildesh = Builder.load_string(screen)
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Blue'
        return self.buildesh


ImportantLinks().run()

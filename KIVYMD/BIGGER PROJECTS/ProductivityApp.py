from kivy.config import Config
Config.set('graphics', 'resizable', '0') 
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import *
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.picker import MDThemePicker, MDDatePicker, MDTimePicker
from kivymd.uix.menu import MDDropdownMenu


ThemeScreen = '''
Screen:
    id: ThemeScreen
    name: 'ThemeScreen'


'''


MainScreen = '''

<Tab>:

Screen:
    id: MainScreen
    name: 'MainScreen'

    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'TO DO LIST'
                        specific_text_color: [0,0,0,1]
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [['yin-yang', lambda x: app.change_theme()]]

                    MDBottomNavigation:
                        MDBottomNavigationItem:
                            name: 'Notes Screen'
                            text: 'Notes'
                            icon: 'notebook'

                            Screen:
                                id: ViewNotes_screen

                                MDCard:
                                    size_hint: None, None
                                    size: "280dp", "180dp"
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    ripple_behavior: True
                                    on_release:print("worked")

                                MDFloatingActionButton:
                                    icon: "notebook-plus"
                                    pos_hint: {"center_x": 0.8, "center_y": 0.1}


                        MDBottomNavigationItem:
                            name: 'Tasks Screen'
                            text: 'Tasks'
                            icon: 'view-list'

                            MDTabs:

                                Tab:
                                    text: 'TASKS'

                                    ScrollView:
                                        MDList:
                                            id: MDListesh
                                    MDFloatingActionButton:
                                        icon: "playlist-plus"
                                        pos_hint: {"center_x": 0.8, "center_y": 0.1}

                                Tab:
                                    text: 'ADD TASKS'

                                    Screen:

                                        MDTextField:
                                            id: TaskName
                                            hint_text: 'Enter Name Of The Task'
                                            font_size: 30
                                            size_hint_x: 0.8
                                            pos_hint: {"center_x": 0.5, "center_y": 0.9}

                                        MDTextFieldRect:
                                            id: TaskDesc
                                            hint_text: 'Enter Brief Description Of The Task'
                                            
                                            size_hint_x: 0.8
                                            size_hint_y: 0.4
                                            pos_hint: {"center_x": 0.5, "center_y": 0.65}

                                        MDTextField:
                                            id: date
                                            icon: 'calendar-month'
                                            hint_text: 'Select Date'
                                            disabled: True
                                            font_size: 20
                                            size_hint_x: 0.8
                                            pos_hint: {"center_x": 0.5, "center_y": 0.36}

                                        MDIconButton:
                                            icon: 'calendar-month'
                                            pos_hint: {"center_x": 0.87, "center_y": 0.38}
                                            on_release: app.date_picker.open()

                                        MDTextField:
                                            id: time
                                            icon: 'clock'
                                            disabled: True
                                            hint_text: 'Select Time'
                                            font_size: 20
                                            size_hint_x: 0.8
                                            pos_hint: {"center_x": 0.5, "center_y": 0.26}

                                        MDIconButton:
                                            icon: 'clock'
                                            pos_hint: {"center_x": 0.87, "center_y": 0.28}
                                            on_release: app.time_picker.open()

                                        MDTextField:
                                            id: frequency
                                            hint_text: 'Select Frequency'
                                            disabled: True
                                            icon: 'update'
                                            font_size: 20
                                            size_hint_x: 0.8
                                            pos_hint: {"center_x": 0.5, "center_y": 0.16}

                                        MDIconButton:
                                            id: frequency_btn
                                            icon: 'update'
                                            pos_hint: {"center_x": 0.87, "center_y": 0.18}
                                            on_release: app.dd_menu.open()

                                        MDRaisedButton:
                                            text: 'ADD TASK'
                                            size_hint_x: 0.4
                                            pos_hint: {"center_x": 0.5, "center_y": 0.07}
                                            on_press: app.AddTask()

                                Tab:
                                    text: 'DELETE TASKS'

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                spacing: '8dp'
                padding: '8dp'
                orientation: "vertical"
                Image:
                    source: "C:\\Varun\\WALLPAPERS\\KYRIE IRVING.jpg"

                MDList:
                    id: nav_drawer_list

                    OneLineIconListItem:
                        text: 'Profile'
                        IconLeftWidget:
                            icon: 'account-circle'

                    OneLineIconListItem:
                        text: 'Change Color Scheme'
                        on_release: app.theme_picker.open()
                        IconLeftWidget:
                            icon: 'theme-light-dark'

                    OneLineIconListItem:
                        text: 'About'
                        IconLeftWidget:
                            icon: 'information'
                ScrollView:
'''


class Tab(FloatLayout, MDTabsBase):
    pass


class ProductivityApp(MDApp):

    def build(self):
        self.title = 'TO - DO LIST'
        self.theme_cls.theme_style = 'Dark'
        self.screen_manager = ScreenManager(transition = SlideTransition())
        self.app_build = Builder.load_string(MainScreen)
        self.theme_picker = MDThemePicker()
        self.date_picker = MDDatePicker(callback = self.get_date)
        self.time_picker = MDTimePicker()
        self.time_picker.bind(time=self.get_time)
        dd_menu_items = ['Once', 'Daily', 'Weekly', 'Monthly']
        menu_items = []
        for i in dd_menu_items:
            menu_items.append(
                {
                    "viewclass": "MDMenuItem",
                    "text": i
                }
            )
        self.dd_menu = MDDropdownMenu(
            caller = self.app_build.ids.frequency_btn,
            items = menu_items,
            width_mult = 4
        )
        self.dd_menu.bind(on_release = self.option_callback)
        return self.app_build

    def get_date(self, date):
        print(str(date))
        self.app_build.ids.date.text = str(date)

    def get_time(self, widget, time):
        print(str(time))
        self.app_build.ids.time.text = str(time)

    def option_callback(self, instance_menu, instance_menu_item):
        print(instance_menu_item.text)
        self.app_build.ids.frequency.text = instance_menu_item.text
        self.dd_menu.dismiss()

    def AddTask(self):
        print(f"TASK NAME : {self.app_build.ids.TaskName.text}")
        print(f"TASK DESC : {self.app_build.ids.TaskDesc.text}")
        print(f"DATE      : {self.app_build.ids.date.text}")
        print(f"TIME      : {self.app_build.ids.time.text}")
        print(f"FREQUENCY : {self.app_build.ids.frequency.text}")

    def change_theme(self):
        self.theme_cls.theme_style = 'Dark' if self.theme_cls.theme_style == 'Light' else 'Light'


ProductivityApp().run()
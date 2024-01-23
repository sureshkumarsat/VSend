from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.picker import MDThemePicker, MDDatePicker, MDTimePicker
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.list import ThreeLineAvatarIconListItem, IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.properties import StringProperty
from kivy.clock import Clock
import pyrebase
import json
import requests


LoginScreen = '''
Screen:
    id: LoginScreen
    name: "LoginScreen"
    on_enter:
        app.anim(back)
        app.anim1(back1)
        app.anim_text(title_label)
    on_pre_enter:
        app.text_clear_login()

    MDFloatLayout:
        MDFloatLayout:
            id: back
            size_hint_y: 0.6
            pos_hint: {"center_y": 1.8}
            canvas.before:
                Color:
                    rgb: (58/255, 187/255, 242/255, 1)
                Rectangle:
                    size: self.size
                    pos: self.pos

        MDFloatLayout:
            id: back1
            size_hint_y: 0.6
            pos_hint: {"center_y": 1.8}
            canvas:
                Color:
                    rgb: (58/255, 187/255, 242/255, 1)
                Ellipse:
                    size: self.size
                    pos: self.pos

        MDIconButton:
            id: title_icon
            icon: 'account-circle'
            pos_hint: {"center_x": 0.5,"center_y": 0.8}
            user_font_size: "120sp"
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1

        MDLabel:
            id: title_label
            text: f"[size=40]Login Page[/size]"
            markup: True
            pos_hint: {"center_x": 0.5,"center_y": 0.65}
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1
            font_style: 'H5'

        MDTextField:
            id: Mail
            mode: 'rectangle'
            text: ''
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            hint_text: "Enter Mail ID"
            icon_right: 'gmail'
            icon_right_color: app.theme_cls.primary_color
            font_size: 18

        MDTextField:
            id: Pwd_login
            mode: 'rectangle'
            text: ''
            password: True
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            hint_text: "Enter Password"
            icon_right: 'eye'
            icon_right_color: app.theme_cls.primary_color
            font_size: 18

        MDIconButton:
            id: iconbutton_login
            icon: "eye-off"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            pos_hint: {"center_x": 0.85, "center_y": 0.295}
            on_press: app.password_main("LoginScreen")

        MDRaisedButton:
            text: 'LOGIN'
            size_hint_x: 0.4
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_release: app.login()

        MDLabel:
            text: "Don't have an account?"
            font_size: 18
            halign: 'center'
            font_style: 'Body2'
            pos_hint: {"center_x": 0.45, "center_y": 0.13}

        MDTextButton:
            text: '[u]Sign Up[/u]'
            markup: True
            pos_hint: {"center_x": 0.71, "center_y": 0.1325}
            theme_text_color: 'Custom'
            text_color: 0, 0, 1, 1
            on_press: app.screen_manager.current = 'SignupScreen'
'''


SignupScreen = '''
Screen:
    id: SignupScreen
    name: "SignupScreen"
    on_enter:
        app.anim(back)
        app.anim1(back1)
        app.anim_text(title_label)
    on_pre_enter: app.text_clear_signup()

    MDFloatLayout:
        MDFloatLayout:
            id: back
            size_hint_y: 0.6
            pos_hint: {"center_y": 1.8}
            canvas.before:
                Color:
                    rgb: (58/255, 187/255, 242/255, 1)
                Rectangle:
                    size: self.size
                    pos: self.pos

        MDFloatLayout:
            id: back1
            size_hint_y: 0.6
            pos_hint: {"center_y": 1.8}
            canvas:
                Color:
                    rgb: (58/255, 187/255, 242/255, 1)
                Ellipse:
                    size: self.size
                    pos: self.pos

        MDIconButton:
            id: title_icon
            icon: 'account-circle'
            pos_hint: {"center_x": 0.5,"center_y": 0.8}
            user_font_size: "120sp"
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1

        MDLabel:
            id: title_label
            text: f"[size=40]Sign - Up Page[/size]"
            markup: True
            pos_hint: {"center_x": 0.5,"center_y": 0.65}
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1
            font_style: 'H5'

        MDTextField:
            id: Mail
            mode: 'rectangle'
            text: ''
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            hint_text: "Enter Mail ID"
            icon_right: 'gmail'
            icon_right_color: app.theme_cls.primary_color
            font_size: 18

        MDTextField:
            id: Pwd_signup
            mode: 'rectangle'
            text: ''
            password: True
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            hint_text: "Enter Password"
            icon_right: 'eye'
            icon_right_color: app.theme_cls.primary_color
            font_size: 18

        MDIconButton:
            id: iconbutton_signup
            icon: "eye-off"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.85, "center_y": 0.295}
            on_press: app.password_main("SignUpScreen")

        MDRaisedButton:
            text: 'SIGN UP'
            size_hint_x: 0.4
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_release: app.SignUp()

        MDLabel:
            text: "Already have an account?"
            font_size: 18
            halign: 'center'
            font_style: 'Body2'
            pos_hint: {"center_x": 0.45, "center_y": 0.13}

        MDTextButton:
            text: '[u]Login[/u]'
            markup: True
            pos_hint: {"center_x": 0.71, "center_y": 0.1325}
            theme_text_color: 'Custom'
            text_color: 0, 0, 1, 1
            on_press: app.screen_manager.current = 'LoginScreen'
'''


AboutScreen = '''
Screen:
    id: AboutScreen
    name: 'AboutScreen'

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'About'
            specific_text_color: [0,0,0,1]
            left_action_items: [['backburger', lambda x: app.BackToTasks()]]
            right_action_items: [['yin-yang', lambda x: app.change_theme()]]

        ScrollView:
'''


AppMainScreen = '''
<MDClickableTextFieldDate@MDRelativeLayout>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        mode: 'rectangle'
        hint_text: 'Select Date'
        icon_right: 'calendar'
        disabled: True
    MDIconButton:
        icon: "calendar"
        ripple_scale: .5
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
        on_release: app.date_picker.open()


<MDClickableTextFieldTime@MDRelativeLayout>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        mode: 'rectangle'
        hint_text: 'Select Time'
        icon_right: 'clock'
        disabled: True
    MDIconButton:
        icon: "clock"
        ripple_scale: .5
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
        on_release: app.time_picker.open()


<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"


<Content_Add_Task>:
    id: Dialog_box
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "310dp"
    MDTextField:
        id: name_task
        mode: 'rectangle'
        hint_text: 'Enter Task Name'
        font_size: 20
    MDClickableTextFieldDate:
        id: date_input
        font_size: 18
        hint_text: 'SELECT DATE'
        icon_right: 'calendar'
        icon_right_color: app.theme_cls.primary_color
    MDClickableTextFieldTime:
        id: time_input
        font_size: 18
        hint_text: 'SELECT TIME'
        icon_right: 'clock'
        icon_right_color: app.theme_cls.primary_color
    ScrollView:
        MDList:
            ItemConfirm:
                id: once
                text: 'Once'
            ItemConfirm:
                id: daily
                text: 'Daily'
            ItemConfirm:
                id: weekly
                text: 'Weekly'
            ItemConfirm:
                id: monthly
                text: 'Monthly'


<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height

    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            on_release: app.remove_task(root)

    MDCardSwipeFrontBox:

        ThreeLineIconListItem:
            id: content
            text: root.text
            secondary_text: root.secondary_text
            tertiary_text: root.tertiary_text
            on_press: print(content.text)
            IconLeftWidget:
                icon: 'alarm'


Screen:
    id: AppMainScreen
    name: 'AppMainScreen'

    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        id: MainToolBar
                        title: 'TASKS'
                        specific_text_color: [0,0,0]
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [['theme-light-dark', lambda x: app.change_theme()]]
                        elevation: 10

                    MDBottomNavigation:

                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'TASKS'
                            icon: 'alarm'
                            on_tab_press:
                                MainToolBar.title = 'TASKS'
                                app.onTasks_Enter()

                            MDScrollViewRefreshLayout:
                                id: refresh_layout_tasks
                                refresh_callback: app.refresh_callback_tasks
                                root_layout: root
                                MDList:
                                    id: Tasks_List
                                    spacing: '8dp'
                                    padding: '12dp'

                            MDFloatingActionButton:
                                icon: 'alarm-plus'
                                pos_hint: {"center_x": 0.85, "center_y": 0.1}
                                on_release: app.add_task_dialog.open()

                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'NOTES'
                            icon: 'view-list'
                            on_tab_press: 
                                MainToolBar.title = 'NOTES'

                            MDFloatingActionButton:
                                icon: 'notebook-plus-outline'
                                pos_hint: {"center_x": 0.85, "center_y": 0.1}

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                spacing: '8dp'
                padding: '8dp'
                orientation: "vertical"
                Image:
                    id: ImageNavDrawer
                    source: "data:image/png;base64,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"
                    size: '100dp', '100dp'

                MDList:
                    id: nav_drawer_list

                    OneLineListItem:
                        id: user_mail_list_item

                    OneLineIconListItem:
                        text: 'Change Color Scheme'
                        on_release: app.theme_picker.open()
                        IconLeftWidget:
                            icon: 'theme-light-dark'

                    OneLineIconListItem:
                        text: 'Logout'
                        on_release: app.screen_manager.current = 'LoginScreen'
                        IconLeftWidget:
                            icon: 'logout'

                    OneLineIconListItem:
                        text: 'Create an account'
                        on_release: app.screen_manager.current = 'SignupScreen'
                        IconLeftWidget:
                            icon: 'account-plus'

                    OneLineIconListItem:
                        text: 'About'
                        on_release: app.screen_manager.current = 'AboutScreen'
                        IconLeftWidget:
                            icon: 'information'

                    OneLineIconListItem:
                        text: 'Exit'
                        on_release: app.stop()
                        IconLeftWidget:
                            icon: 'exit-run'

                ScrollView:
'''


class Content_Add_Task(MDBoxLayout):
    pass


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()


class ToDoListApp(MDApp):

    x = 0
    y = 15

    title = 'TO - DO LIST'
    firebaseConfig = {
        "apiKey": "AIzaSyDGvMHjKJwvIllrpnB7XrpJMSPyMXF5njk",
        "authDomain": "todo-notes-app-424d3.firebaseapp.com",
        "databaseURL": "https://todo-notes-app-424d3-default-rtdb.firebaseio.com",
        "projectId": "todo-notes-app-424d3",
        "storageBucket": "todo-notes-app-424d3.appspot.com",
        "messagingSenderId": "811101120479",
        "appId": "1:811101120479:web:921f65ce525f6a7cae466a",
        "measurementId": "G-LYBNEJ6WS4"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    db = firebase.database()

    date = None
    time = None
    frequency = None

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.screen_manager = ScreenManager(transition = SlideTransition())
        self.AppMainScreen = Builder.load_string(AppMainScreen)
        self.AboutScreen = Builder.load_string(AboutScreen)
        self.LoginScreen = Builder.load_string(LoginScreen)
        self.SignUpScreen = Builder.load_string(SignupScreen)
        self.theme_picker = MDThemePicker()
        self.date_picker = MDDatePicker(callback = self.get_date)
        self.time_picker = MDTimePicker()
        self.time_picker.bind(time=self.get_time)
        self.add_task_dialog = MDDialog(
            title="ADD TASK",
            type="custom",
            content_cls = Content_Add_Task(),
            buttons=[
                MDRaisedButton(
                    text="ADD TASK",
                    theme_text_color = 'Custom',
                    text_color = (0, 0, 0, 1),
                    on_release = lambda _: self.AddTask()
                ),
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = lambda _: self.close_add_task_dialogue()
                ),
            ],
        )
        self.screen_manager.add_widget(self.LoginScreen)
        self.screen_manager.add_widget(self.SignUpScreen)
        self.screen_manager.add_widget(self.AppMainScreen)
        self.screen_manager.add_widget(self.AboutScreen)
        return self.screen_manager

    def on_start(self):
        pass

    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LOGIN AND SIGNUP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def anim(self, widget):
        anim = Animation(pos_hint = {"center_y": 1.16})
        anim.start(widget)

    def anim1(self, widget):
        anim = Animation(pos_hint = {"center_y": 0.85})
        anim.start(widget)

    def anim_icons(self, widget):
        anim = Animation(pos_hint = {"center_y": 0.7})
        anim += Animation(pos_hint = {"center_y": 0.8})
        anim.start(widget)

    def anim_text(self, widget):
        anim = Animation(opacity = 0, duration = 2)
        anim += Animation(opacity = 1)
        anim.start(widget)

    def password_main(self, screen):
        if screen == "LoginScreen":
            if self.LoginScreen.ids.Pwd_login.password == True:
                self.LoginScreen.ids.Pwd_login.password = False
                self.LoginScreen.ids.iconbutton_login.icon = "eye"
            else:
                self.LoginScreen.ids.Pwd_login.password = True
                self.LoginScreen.ids.iconbutton_login.icon = "eye-off"
        elif screen == "SignUpScreen":
            if self.SignUpScreen.ids.Pwd_signup.password == True:
                self.SignUpScreen.ids.Pwd_signup.password = False
                self.SignUpScreen.ids.iconbutton_signup.icon = "eye"
            else:
                self.SignUpScreen.ids.Pwd_signup.password = True
                self.SignUpScreen.ids.iconbutton_signup.icon = "eye-off"

    def SignUp(self):
        MailID = self.SignUpScreen.ids.Mail.text
        Password = self.SignUpScreen.ids.Pwd_signup.text
        print(MailID, Password)
        try:
            self.user = self.auth.create_user_with_email_and_password(MailID, Password)
            toast(f'Account has been created with {MailID}')
            self.screen_manager.current = 'AppMainScreen'
            self.AppMainScreen.ids.user_mail_list_item.text = self.user['email']
        except requests.HTTPError as e:
            error_dict = e.args[1]
            error = json.loads(error_dict)['error']['message']
            print(f"{error.replace('_', ' ')}")
            toast(f"{error.replace('_', ' ')}")
        self.SignUpScreen.ids.Mail.text = ''
        self.SignUpScreen.ids.Pwd_signup.text = ''

    def login(self):
        MailID = self.LoginScreen.ids.Mail.text
        Password = self.LoginScreen.ids.Pwd_login.text
        print(MailID, Password)
        try:
            self.user = self.auth.sign_in_with_email_and_password(MailID, Password)
            toast(f'Logged in to {MailID}')
            self.screen_manager.current = 'AppMainScreen'
            self.AppMainScreen.ids.user_mail_list_item.text = self.user['email']
        except requests.HTTPError as e:
            error_dict = e.args[1]
            error = json.loads(error_dict)['error']['message']
            print(f"{error.replace('_', ' ')}")
            toast(f"{error.replace('_', ' ')}")
        self.LoginScreen.ids.Mail.text = ''
        self.LoginScreen.ids.Pwd_login.text = ''

    def text_clear_signup(self):
        self.SignUpScreen.ids.Mail.text = ''
        self.SignUpScreen.ids.Pwd_signup.text = ''

    def text_clear_login(self):
        self.LoginScreen.ids.Mail.text = ''
        self.LoginScreen.ids.Pwd_login.text = ''


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASKS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def onTasks_Enter(self):
        self.AppMainScreen.ids.Tasks_List.clear_widgets()
        tasks = self.db.child(f"{self.user['email'].replace('@gmail.com', '')}").child("Tasks").get()
        for task in tasks.each():
            print(task.key())
            print(task.val())
            text = task.key()
            secondary_text = f'{task.val()["time"]}  {task.val()["frequency"]}'
            tertiary_text = task.val()["date"]
            item = SwipeToDeleteItem(text = text, secondary_text = secondary_text, tertiary_text = tertiary_text)
            self.AppMainScreen.ids.Tasks_List.add_widget(item)

    def get_date(self, date):
        self.date = date
        print(str(date))
        self.add_task_dialog.content_cls.ids.date_input.ids.text_field.text = str(date)

    def get_time(self, widget, time):
        self.time = time
        timesh = str(time)
        print(timesh)
        houresh = time.hour
        if houresh < 12:
            if houresh < 10:
                timesh = f'0{houresh}:{str(time)[3:5]} a.m'
            else:
                timesh = f'{houresh}:{str(time)[3:5]} a.m'
        else:
            houresh -= 12
            if houresh < 10:
                timesh = f'0{houresh}:{str(time)[3:5]} p.m'
            else:
                timesh = f'{houresh}:{str(time)[3:5]} p.m'
        self.add_task_dialog.content_cls.ids.time_input.ids.text_field.text = timesh

    def close_add_task_dialogue(self):
        self.add_task_dialog.content_cls.ids.name_task.text = ''
        self.add_task_dialog.content_cls.ids.date_input.ids.text_field.text = ''
        self.add_task_dialog.content_cls.ids.time_input.ids.text_field.text = ''
        self.add_task_dialog.content_cls.ids.once.ids.check.active = False
        self.add_task_dialog.content_cls.ids.daily.ids.check.active = False
        self.add_task_dialog.content_cls.ids.weekly.ids.check.active = False
        self.add_task_dialog.content_cls.ids.monthly.ids.check.active = False
        self.date = None
        self.time = None
        self.add_task_dialog.dismiss()

    def AddTask(self):
        tasks_previous = self.db.child(f"{self.user['email'].replace('@gmail.com', '')}").child("Tasks").shallow().get().val()
        print(type(tasks_previous))
        if self.add_task_dialog.content_cls.ids.name_task.text == '' or self.add_task_dialog.content_cls.ids.name_task.text.isspace():
            toast('All fields are required to be entered. Enter name of the task.')
        else:
            if tasks_previous != None:
                if self.add_task_dialog.content_cls.ids.name_task.text in tasks_previous:
                    toast('Task name already exists. Please enter an unused name')
                else:
                    name_task = self.add_task_dialog.content_cls.ids.name_task.text
                    if self.date == None:
                        toast('Select a date.')
                    else:
                        if self.time == None:
                            toast('Select a time.')
                        else:
                            if self.add_task_dialog.content_cls.ids.once.ids.check.active:
                                self.frequency = 'Once'
                            elif self.add_task_dialog.content_cls.ids.daily.ids.check.active:
                                self.frequency = 'Daily'
                            elif self.add_task_dialog.content_cls.ids.weekly.ids.check.active:
                                self.frequency = 'Weekly'
                            elif self.add_task_dialog.content_cls.ids.monthly.ids.check.active:
                                self.frequency = 'Monthly'
                            if self.frequency != None:
                                print(name_task)
                                print(self.date)
                                print(self.time)
                                print(self.frequency)
                                task_data = {"date": f'{self.date}', "time": f'{self.time}', "frequency": f'{self.frequency}'}
                                self.db.child(f"{self.user['email'].replace('@gmail.com', '')}").child("Tasks").child(f'{name_task}').set(task_data)
                                self.close_add_task_dialogue()
                                toast('Task has been added!')
                            else:
                                toast('Select a frequency.')
            else:
                name_task = self.add_task_dialog.content_cls.ids.name_task.text
                if self.date == None:
                    toast('Select a date.')
                else:
                    if self.time == None:
                        toast('Select a time.')
                    else:
                        if self.add_task_dialog.content_cls.ids.once.ids.check.active:
                            self.frequency = 'Once'
                        elif self.add_task_dialog.content_cls.ids.daily.ids.check.active:
                            self.frequency = 'Daily'
                        elif self.add_task_dialog.content_cls.ids.weekly.ids.check.active:
                            self.frequency = 'Weekly'
                        elif self.add_task_dialog.content_cls.ids.monthly.ids.check.active:
                            self.frequency = 'Monthly'
                        if self.frequency != None:
                            print(name_task)
                            print(self.date)
                            print(self.time)
                            print(self.frequency)
                            task_data = {"date": f'{self.date}', "time": f'{self.time}', "frequency": f'{self.frequency}'}
                            self.db.child(f"{self.user['email'].replace('@gmail.com', '')}").child("Tasks").child(f'{name_task}').set(task_data)
                            self.close_add_task_dialogue()
                            toast('Task has been added!')
                        else:
                            toast('Select a frequency.')

    def remove_task(self, instance):
        space = "               "
        text_delete_dialog = f'Are you sure you want to delete the task "{instance.text}"?\n\n{space}date            :  {instance.tertiary_text}\n{space}time            :  {instance.secondary_text.split("  ")[0]}\n{space}frequency  :  {instance.secondary_text.split("  ")[1]}'
        self.dialog_delete_confirm = MDDialog(
            title="DELETE TASK",
            text = text_delete_dialog,
            buttons=[
                MDRaisedButton(
                    text="DELETE TASK",
                    theme_text_color = 'Custom',
                    text_color = (0, 0, 0, 1),
                    on_release = lambda _: self.remove_from_db(instance)# self.AppMainScreen.ids.Tasks_List.remove_widget(instance)
                ),
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = lambda _: self.dialog_delete_confirm.dismiss()
                ),
            ],
        )
        self.dialog_delete_confirm.open()

    def remove_from_db(self, instance):
        self.db.child(f"{self.user['email'].replace('@gmail.com', '')}").child("Tasks").child(f'{instance.text}').remove()
        self.AppMainScreen.ids.Tasks_List.remove_widget(instance)
        toast(f"Deleted '{instance.text}' successfully.")
        self.dialog_delete_confirm.dismiss()

    def set_list_tasks(self):
        self.onTasks_Enter()

    def refresh_callback_tasks(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback_tasks(interval):
            self.AppMainScreen.ids.Tasks_List.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list_tasks()
            self.AppMainScreen.ids.refresh_layout_tasks.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback_tasks, 1)


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GENERAL~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def screentoAdd(self):
        self.screen_manager.current = 'AddTaskScreen'

    def screentoDelete(self):
        self.screen_manager.current = 'DeleteTaskScreen'

    def BackToTasks(self):
        self.screen_manager.transition = SlideTransition(direction = 'right')
        self.screen_manager.current = 'AppMainScreen'
        self.screen_manager.transition = SlideTransition(direction = 'left')

    def change_theme(self):
        self.theme_cls.theme_style = 'Dark' if self.theme_cls.theme_style == 'Light' else 'Light'


ToDoListApp().run()
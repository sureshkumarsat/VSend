from kivy.config import Config
# Config.set('graphics', 'resizable', '0')
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
from kivy.properties import StringProperty, BooleanProperty
from kivy.clock import Clock
import mysql.connector as MySQL


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
<MDRightSwitch@IRightBodyTouch+MDSwitch>:


<ListItemWithMDSwitch@OneLineAvatarIconListItem>:
    MDRightSwitch:
        id: switch


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
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "410dp"
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
    MDList:
        ListItemWithMDSwitch:
            id: reminder_option
            text: 'Remind Me?'
    ScrollView:
        MDList:
            spacing: "8dp"
            OneLineListItem:
                text: 'Select A Frequency :'
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


<Content_Add_Note>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "410dp"
    MDTextField:
        id: Note_Title
        pos_hint: {"center_x": 0.5,"center_y": 0.9}
        hint_text: "Enter Name Of The Note"
        mode: "fill"
        fill_color: 0, 0, 0, 0
    MDTextFieldRect:
        id: Note_Desc
        hint_text: "Enter Description Of The Note"


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

        ThreeLineAvatarIconListItem:
            id: content
            text: root.text
            secondary_text: root.secondary_text
            tertiary_text: root.tertiary_text
            on_press: app.EditTaskDialogConfig(content.text)
            IconLeftWidget:
                icon: 'alarm'


<SwipeToDeleteItemNotes>:
    size_hint_y: None
    height: content.height

    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            on_release: app.remove_note(root)

    MDCardSwipeFrontBox:

        OneLineIconListItem:
            id: content
            text: root.text
            on_press: app.EditNoteDialogConfig(content.text)
            IconLeftWidget:
                icon: 'circle-slice-8'


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
                                app.onNotes_Enter()

                            MDScrollViewRefreshLayout:
                                id: refresh_layout_notes
                                refresh_callback: app.refresh_callback_notes
                                root_layout: root
                                MDList:
                                    id: Notes_List
                                    spacing: '8dp'
                                    padding: '12dp'

                            MDFloatingActionButton:
                                icon: 'notebook-plus-outline'
                                pos_hint: {"center_x": 0.85, "center_y": 0.1}
                                on_release: app.add_note_dialog.open()

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
                        on_release:
                            app.Logout()
                            app.screen_manager.current = 'LoginScreen'
                        IconLeftWidget:
                            icon: 'logout'

                    OneLineIconListItem:
                        text: 'Create an account'
                        on_release:
                            app.Logout()
                            app.screen_manager.current = 'SignupScreen'
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


class Content_Add_Note(MDBoxLayout):
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


class SwipeToDeleteItemNotes(MDCardSwipe):
    text = StringProperty()


class ToDoListApp(MDApp):

    user = None

    MySQL_Config = {
        'host' : 'localhost',
        'user' : 'root',
        'passwd' : 'MYSQLVARY',
        'database' : 'todolist_kivymd'
    }

    x = 0
    y = 15

    title = 'TO - DO LIST'

    date = None
    time = None
    frequency = None
    reminder_option = 'N'

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.screen_manager = ScreenManager(transition = SlideTransition())
        self.AppMainScreen = Builder.load_string(AppMainScreen)
        self.AboutScreen = Builder.load_string(AboutScreen)
        self.LoginScreen = Builder.load_string(LoginScreen)
        self.SignUpScreen = Builder.load_string(SignupScreen)
        self.theme_picker = MDThemePicker()
        self.date_picker = MDDatePicker() # callback = self.get_date)
        self.date_picker.bind(on_save=self.get_date, on_cancel=self.on_cancel)
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
        self.edit_task_dialog = MDDialog(
            title="EDIT TASK",
            type="custom",
            content_cls = Content_Add_Task(),
            buttons=[
                MDRaisedButton(
                    text="UPDATE TASK",
                    theme_text_color = 'Custom',
                    text_color = (0, 0, 0, 1),
                    on_release = lambda _: self.EditTask()
                ),
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = lambda _: self.close_edit_task_dialogue()
                ),
            ],
        )
        self.add_note_dialog = MDDialog(
            title="ADD TASK",
            type="custom",
            content_cls = Content_Add_Note(),
            buttons=[
                MDRaisedButton(
                    text="ADD NOTE",
                    theme_text_color = 'Custom',
                    text_color = (0, 0, 0, 1),
                    on_release = lambda _: self.AddNote()
                ),
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = lambda _: self.close_add_note_dialogue()
                ),
            ],
        )
        self.edit_note_dialog = MDDialog(
            title="EDIT TASK",
            type="custom",
            content_cls = Content_Add_Note(),
            buttons=[
                MDRaisedButton(
                    text="EDIT NOTE",
                    theme_text_color = 'Custom',
                    text_color = (0, 0, 0, 1),
                    on_release = lambda _: self.EditNote()
                ),
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = lambda _: self.close_edit_note_dialogue()
                ),
            ],
        )
        self.screen_manager.add_widget(self.LoginScreen)
        self.screen_manager.add_widget(self.SignUpScreen)
        self.screen_manager.add_widget(self.AppMainScreen)
        self.screen_manager.add_widget(self.AboutScreen)
        return self.screen_manager

    def on_start(self):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM USERPWD')
        login_data = cursor.fetchall()
        connection.close()
        for i in login_data:
            if i[3] == 'YES':
                self.user = i[1]
                self.screen_manager.current = 'AppMainScreen'
                toast(f"Logged in to '{self.user}'")
                self.AppMainScreen.ids.user_mail_list_item.text = self.user
                self.onTasks_Enter()
                self.onNotes_Enter()


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
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        MailID = self.SignUpScreen.ids.Mail.text
        Password = self.SignUpScreen.ids.Pwd_signup.text
        print(MailID, Password)
        if len(MailID) < 11:
            toast('Enter Valid Email ID')
        elif len(Password) < 1:
            toast('Enter Valid Password.')
        elif len(Password) > 12:
            toast('Password must be of maximum 12 characters.')
        else:
            try:
                qry = f"INSERT INTO USERPWD (MAIL, PASSWORD, LoggedInStatus) values('{MailID}', '{Password}', 'YES')"
                cursor.execute(qry)
                connection.commit()
                connection.close()
                self.user = MailID
                toast(f'Account has been created with {MailID}')
                self.screen_manager.current = 'AppMainScreen'
                self.AppMainScreen.ids.user_mail_list_item.text = self.user
                self.SignUpScreen.ids.Mail.text = ''
                self.SignUpScreen.ids.Pwd_signup.text = ''
            except Exception as e:
                toast(f'{e}')
        self.SignUpScreen.ids.Mail.text = ''
        self.SignUpScreen.ids.Pwd_signup.text = ''

    def login(self):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        MailID = self.LoginScreen.ids.Mail.text
        Password = self.LoginScreen.ids.Pwd_login.text
        print(f'{MailID}\n{Password}')
        if len(MailID) < 11:
            toast('Enter Valid Email ID')
        elif len(Password) < 1:
            toast('Enter Valid Password.')
        elif len(Password) > 12:
            toast('Password must be of maximum 12 characters.')
        else:
            try:
                cursor.execute('SELECT * FROM USERPWD')
                login_data = cursor.fetchall()
                for i in login_data:
                    if i[1] == MailID:
                        if i[2] == Password:
                            qry = f"UPDATE USERPWD SET LoggedInStatus = 'YES' WHERE MAIL = '{MailID}'"
                            cursor.execute(qry)
                            connection.commit()
                            connection.close()
                            self.user = MailID
                            self.screen_manager.current = 'AppMainScreen'
                            toast(f"Logged in to '{MailID}'")
                            self.AppMainScreen.ids.user_mail_list_item.text = MailID
                        else:
                            toast('You have entered wrong password.')
                            self.LoginScreen.ids.Mail.text = ''
                            self.LoginScreen.ids.Pwd_login.text = ''
            except Exception as e:
                toast(f'Error Encountered : {e}')
        self.LoginScreen.ids.Mail.text = ''
        self.LoginScreen.ids.Pwd_login.text = ''

    def text_clear_signup(self):
        self.SignUpScreen.ids.Mail.text = ''
        self.SignUpScreen.ids.Pwd_signup.text = ''

    def text_clear_login(self):
        self.LoginScreen.ids.Mail.text = ''
        self.LoginScreen.ids.Pwd_login.text = ''

    def Logout(self):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        MailID = self.user
        qry = f"UPDATE USERPWD SET LoggedInStatus = 'NO' WHERE MAIL = '{MailID}'"
        cursor.execute(qry)
        connection.commit()
        connection.close()
        self.user = None

    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASKS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def onTasks_Enter(self):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        self.AppMainScreen.ids.Tasks_List.clear_widgets()
        qry = f"SELECT * FROM USERTASKS WHERE MAIL = '{self.user}'"
        cursor.execute(qry)
        tasks = cursor.fetchall()
        for task in tasks:
            text = f"{task[0]} . {task[4]}"
            secondary_text = f'{task[3]} | {task[6]}'
            tertiary_text = f"{task[2]}"
            item = SwipeToDeleteItem(text = text, secondary_text = secondary_text, tertiary_text = tertiary_text)
            self.AppMainScreen.ids.Tasks_List.add_widget(item)
        connection.close()

    def get_date(self, date):
        self.date = date
        print(str(date))
        self.add_task_dialog.content_cls.ids.date_input.ids.text_field.text = str(date)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

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
        self.add_task_dialog.content_cls.ids.reminder_option.ids.switch.active = False
        self.date = None
        self.time = None
        self.frequency = None
        self.reminder_option = 'N'
        self.add_task_dialog.dismiss()

    def EditTaskDialogConfig(self, Text):
        self.TaskID = int(Text.split(' . ')[0])
        self.edit_task_dialog.open()
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        qry = f"SELECT * FROM USERTASKS WHERE SNO = {self.TaskID}"
        cursor.execute(qry)
        edit_data = cursor.fetchall()
        self.edit_task_dialog.content_cls.ids.name_task.text = edit_data[0][4]
        self.edit_task_dialog.content_cls.ids.date_input.ids.text_field.text = str(edit_data[0][2])
        self.edit_task_dialog.content_cls.ids.time_input.ids.text_field.text = str(edit_data[0][3])
        if edit_data[0][-2] == 'Once':
            self.edit_task_dialog.content_cls.ids.once.ids.check.active = True
        if edit_data[0][-2] == 'Daily':
            self.edit_task_dialog.content_cls.ids.daily.ids.check.active = True
        if edit_data[0][-2] == 'Weekly':
            self.edit_task_dialog.content_cls.ids.weekly.ids.check.active = True
        if edit_data[0][-2] == 'Monthly':
            self.edit_task_dialog.content_cls.ids.monthly.ids.check.active = True
        if edit_data[0][-3] == 'N':
            self.edit_task_dialog.content_cls.ids.reminder_option.ids.switch.active = False
        if edit_data[0][-3] == 'Y':
            self.edit_task_dialog.content_cls.ids.reminder_option.ids.switch.active = True

    def close_edit_task_dialogue(self):
        self.edit_task_dialog.content_cls.ids.name_task.text = ''
        self.edit_task_dialog.content_cls.ids.date_input.ids.text_field.text = ''
        self.edit_task_dialog.content_cls.ids.time_input.ids.text_field.text = ''
        self.edit_task_dialog.content_cls.ids.once.ids.check.active = False
        self.edit_task_dialog.content_cls.ids.daily.ids.check.active = False
        self.edit_task_dialog.content_cls.ids.weekly.ids.check.active = False
        self.edit_task_dialog.content_cls.ids.monthly.ids.check.active = False
        self.edit_task_dialog.content_cls.ids.reminder_option.ids.switch.active = False
        self.date = None
        self.time = None
        self.frequency = None
        self.reminder_option = 'N'
        self.edit_task_dialog.dismiss()

    def AddTask(self):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        if self.add_task_dialog.content_cls.ids.name_task.text == '' or self.add_task_dialog.content_cls.ids.name_task.text.isspace():
            toast('All fields are required to be entered. Enter name of the task.')
        else:
            if self.add_task_dialog.content_cls.ids.name_task.text != None:
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
                            if self.add_task_dialog.content_cls.ids.reminder_option.ids.switch.active:
                                self.reminder_option = 'Y'
                            print(name_task)
                            print(self.date)
                            print(self.time)
                            print(self.frequency)
                            print(self.reminder_option)
                            qry = f"INSERT INTO USERTASKS(MAIL, REMINDER_DATE, REMINDER_TIME, REMINDER_NAME, rem_option, rem_frequency) VALUES('{self.user}', '{self.date}', '{self.time}', '{name_task}', '{self.reminder_option}', '{self.frequency}')"
                            cursor.execute(qry)
                            connection.commit()
                            self.close_add_task_dialogue()
                            toast('Task has been added!')
                        else:
                            toast('Select a frequency.')
        connection.close()

    def EditTask(self):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        if self.edit_task_dialog.content_cls.ids.name_task.text == '' or self.edit_task_dialog.content_cls.ids.name_task.text.isspace():
            toast('All fields are required to be entered. Enter name of the task.')
        else:
            if self.edit_task_dialog.content_cls.ids.name_task.text != None:
                name_task = self.edit_task_dialog.content_cls.ids.name_task.text
                if self.edit_task_dialog.content_cls.ids.date_input.ids.text_field.text == '' or self.edit_task_dialog.content_cls.ids.date_input.ids.text_field.text.isspace():
                    toast('Select a date.')
                else:
                    if self.edit_task_dialog.content_cls.ids.time_input.ids.text_field.text == '' or self.edit_task_dialog.content_cls.ids.time_input.ids.text_field.text.isspace():
                        toast('Select a time.')
                    else:
                        if self.edit_task_dialog.content_cls.ids.once.ids.check.active:
                            self.frequency = 'Once'
                        elif self.edit_task_dialog.content_cls.ids.daily.ids.check.active:
                            self.frequency = 'Daily'
                        elif self.edit_task_dialog.content_cls.ids.weekly.ids.check.active:
                            self.frequency = 'Weekly'
                        elif self.edit_task_dialog.content_cls.ids.monthly.ids.check.active:
                            self.frequency = 'Monthly'
                        if self.frequency != None:
                            if self.edit_task_dialog.content_cls.ids.reminder_option.ids.switch.active:
                                self.reminder_option = 'Y'
                            print(name_task)
                            print(self.date)
                            print(self.time)
                            print(self.frequency)
                            print(self.reminder_option)
                            qry = f"UPDATE USERTASKS SET REMINDER_DATE = '{self.edit_task_dialog.content_cls.ids.date_input.ids.text_field.text}', REMINDER_TIME = '{self.edit_task_dialog.content_cls.ids.time_input.ids.text_field.text}', REMINDER_NAME = '{name_task}', rem_option = '{self.reminder_option}', rem_frequency = '{self.frequency}' WHERE SNO = {self.TaskID}"
                            cursor.execute(qry)
                            connection.commit()
                            self.close_edit_task_dialogue()
                            toast('Task has been edited!')
                        else:
                            toast('Select a frequency.')
        connection.close()

    def remove_task(self, instance):
        text_delete_dialog = f'Are you sure you want to delete the task {instance.text.split(" . ")[-1]}?\n\n'
        self.dialog_delete_confirm = MDDialog(
            title="DELETE TASK",
            text = text_delete_dialog,
            buttons=[
                MDRaisedButton(
                    text="DELETE TASK",
                    theme_text_color = 'Custom',
                    text_color = (0, 0, 0, 1),
                    on_release = lambda _: self.remove_task_from_db(instance)# self.AppMainScreen.ids.Tasks_List.remove_widget(instance)
                ),
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = lambda _: self.dialog_delete_confirm.dismiss()
                ),
            ],
        )
        self.dialog_delete_confirm.open()

    def remove_task_from_db(self, instance):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        qry = f'DELETE FROM USERTASKS WHERE SNO = {instance.text.split(" . ")[0]}'
        cursor.execute(qry)
        connection.commit()
        connection.close()
        self.AppMainScreen.ids.Tasks_List.remove_widget(instance)
        toast(f"Deleted {instance.text.split(' . ')[-1]} successfully.")
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


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~NOTES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def onNotes_Enter(self):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        self.AppMainScreen.ids.Notes_List.clear_widgets()
        qry = f"SELECT * FROM USERNOTES WHERE MAIL = '{self.user}'"
        cursor.execute(qry)
        notes = cursor.fetchall()
        for i in range(0, len(notes)):
            title = f"{notes[i][0]} . {notes[i][2]}"
            item = SwipeToDeleteItemNotes(text = title)
            self.AppMainScreen.ids.Notes_List.add_widget(item)
        connection.close()

    def set_list_notes(self):
        self.onNotes_Enter()

    def refresh_callback_notes(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback_notes(interval):
            self.AppMainScreen.ids.Notes_List.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list_notes()
            self.AppMainScreen.ids.refresh_layout_notes.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback_notes, 1)

    def AddNote(self):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        name = self.add_note_dialog.content_cls.ids.Note_Title.text
        desc = self.add_note_dialog.content_cls.ids.Note_Desc.text
        if name == '' or name.isspace():
            toast('Enter name of the note.')
        else:
            if desc == '' or desc.isspace():
                toast('Enter Notes.')
            else:
                qry = f'INSERT INTO USERNOTES(MAIL, NOTES_TITLE, NOTES_DESC) VALUES("{self.user}", "{name}", "{desc}")'
                cursor.execute(qry)
                connection.commit()
                toast("Note has been added!!!")
                self.close_add_note_dialogue()
        self.add_note_dialog.content_cls.ids.Note_Title.text = ''
        self.add_note_dialog.content_cls.ids.Note_Desc.text = ''
        connection.close()

    def EditNote(self):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        name = self.edit_note_dialog.content_cls.ids.Note_Title.text
        desc = self.edit_note_dialog.content_cls.ids.Note_Desc.text
        if name == '' or name.isspace():
            toast('Enter name of the note.')
        else:
            if desc == '' or desc.isspace():
                toast('Enter Notes.')
            else:
                qry = f'UPDATE USERNOTES SET MAIL = "{self.user}", NOTES_TITLE = "{name}", NOTES_DESC = "{desc}" WHERE SNO = {self.NoteID}'
                cursor.execute(qry)
                connection.commit()
                toast("Note has been added!!!")
                self.close_edit_note_dialogue()
        self.add_note_dialog.content_cls.ids.Note_Title.text = ''
        self.add_note_dialog.content_cls.ids.Note_Desc.text = ''
        connection.close()

    def EditNoteDialogConfig(self, Text):
        self.NoteID = int(Text.split(' . ')[0])
        self.edit_note_dialog.open()
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        qry = f"SELECT * FROM USERNOTES WHERE SNO = {self.NoteID}"
        cursor.execute(qry)
        edit_data = cursor.fetchall()
        self.edit_note_dialog.content_cls.ids.Note_Title.text = edit_data[0][2]
        self.edit_note_dialog.content_cls.ids.Note_Desc.text = edit_data[0][3]
        connection.close()

    def close_add_note_dialogue(self):
        self.add_note_dialog.content_cls.ids.Note_Title.text = ''
        self.add_note_dialog.content_cls.ids.Note_Desc.text = ''
        self.add_note_dialog.dismiss()

    def remove_note(self, instance):
        text_delete_dialog = f'Are you sure you want to delete the note {instance.text.split(" . ")[-1]}?\n\n'
        self.dialog_delete_confirm = MDDialog(
            title="DELETE NOTE",
            text = text_delete_dialog,
            buttons=[
                MDRaisedButton(
                    text="DELETE NOTE",
                    theme_text_color = 'Custom',
                    text_color = (0, 0, 0, 1),
                    on_release = lambda _: self.remove_note_from_db(instance)# self.AppMainScreen.ids.Tasks_List.remove_widget(instance)
                ),
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = lambda _: self.dialog_delete_confirm.dismiss()
                ),
            ],
        )
        self.dialog_delete_confirm.open()

    def remove_note_from_db(self, instance):
        connection = MySQL.connect(**self.MySQL_Config)
        cursor = connection.cursor()
        qry = f'DELETE FROM USERNOTES WHERE SNO = {instance.text.split(" . ")[0]}'
        cursor.execute(qry)
        connection.commit()
        connection.close()
        self.AppMainScreen.ids.Notes_List.remove_widget(instance)
        toast(f"Deleted {instance.text.split(' . ')[-1]} successfully.")
        self.dialog_delete_confirm.dismiss()

    def close_edit_note_dialogue(self):
        self.add_note_dialog.content_cls.ids.Note_Title.text = ''
        self.add_note_dialog.content_cls.ids.Note_Desc.text = ''
        self.edit_note_dialog.dismiss()


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GENERAL~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def BackToTasks(self):
        self.screen_manager.transition = SlideTransition(direction = 'right')
        self.screen_manager.current = 'AppMainScreen'
        self.screen_manager.transition = SlideTransition(direction = 'left')

    def change_theme(self):
        self.theme_cls.theme_style = 'Dark' if self.theme_cls.theme_style == 'Light' else 'Light'


ToDoListApp().run()
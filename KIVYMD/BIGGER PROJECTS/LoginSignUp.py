from kivy.config import Config
Config.set('graphics', 'resizable', '0') 
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
import mysql.connector as db


connection = db.connect(host = 'localhost', user = 'root', passwd = 'MYSQLVARY', database = 'todolist')
cursor = connection.cursor()


LoginScreen = '''
Screen:
    id: LoginScreen
    name: "LoginScreen"
    on_enter:
        app.anim(back)
        app.anim1(back1)
        app.anim_icons(title_icon)
        app.anim_text(title_label)

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
            id: Usn
            text: ''
            size_hint_x: 0.604
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            hint_text: "Enter Username"
            font_size: 24

        MDIconButton:
            icon: 'tag'
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.78, "center_y": 0.42}

        MDTextField:
            id: Pwd_login
            text: ''
            password: True
            size_hint_x: 0.604
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            hint_text: "Enter Password"
            font_size: 24

        MDIconButton:
            id: iconbutton_login
            icon: "eye-off"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.78, "center_y": 0.32}
            on_press: app.password_main("LoginScreen")

        MDRaisedButton:
            text: 'LOGIN'
            size_hint_x: 0.4
            pos_hint: {"center_x": 0.5, "center_y": 0.2}

        MDLabel:
            text: "Don't have an account?"
            font_size: 18
            halign: 'center'
            font_style: 'Body2'
            pos_hint: {"center_x": 0.45, "center_y": 0.13}

        MDTextButton:
            text: '[u]Sign Up[/u]'
            markup: True
            pos_hint: {"center_x": 0.63, "center_y": 0.13}
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
        app.anim_icons(title_icon)
        app.anim_text(title_label)

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
            id: Usn
            text: ''
            size_hint_x: 0.604
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            hint_text: "Enter Username"
            font_size: 24

        MDIconButton:
            icon: 'tag'
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.78, "center_y": 0.47}

        MDTextField:
            id: Mail
            text: ''
            size_hint_x: 0.604
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
            hint_text: "Enter Username"
            font_size: 24

        MDIconButton:
            icon: 'gmail'
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.78, "center_y": 0.37}

        MDTextField:
            id: Pwd_signup
            text: ''
            password: True
            size_hint_x: 0.604
            pos_hint: {"center_x": 0.5, "center_y": 0.25}
            hint_text: "Enter Password"
            font_size: 24

        MDIconButton:
            id: iconbutton_signup
            icon: "eye-off"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.78, "center_y": 0.27}
            on_press: app.password_main("SignUpScreen")

        MDRaisedButton:
            text: 'SIGN UP'
            size_hint_x: 0.4
            pos_hint: {"center_x": 0.5, "center_y": 0.15}

        MDLabel:
            text: "Already have an account?"
            font_size: 18
            halign: 'center'
            font_style: 'Body2'
            pos_hint: {"center_x": 0.45, "center_y": 0.1}

        MDTextButton:
            text: '[u]Login[/u]'
            markup: True
            pos_hint: {"center_x": 0.63, "center_y": 0.1}
            theme_text_color: 'Custom'
            text_color: 0, 0, 1, 1
            on_press: app.screen_manager.current = 'LoginScreen'
'''


class LoginSignUpApp(MDApp):
    def build(self):
        self.title = " Login Signup "
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Blue'
        self.screen_manager = ScreenManager()
        self.LoginScreen = Builder.load_string(LoginScreen)
        self.SignUpScreen = Builder.load_string(SignupScreen)
        self.screen_manager.add_widget(self.LoginScreen)
        self.screen_manager.add_widget(self.SignUpScreen)
        self.screen_manager.current = "LoginScreen"
        return self.screen_manager

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


LoginSignUpApp().run()
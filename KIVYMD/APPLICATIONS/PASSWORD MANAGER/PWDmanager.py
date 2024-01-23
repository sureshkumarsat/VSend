from kivy.config import Config
Config.set('graphics', 'resizable', '0') 
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '450')
Config.set('kivy','window_icon','APPLICATIONS\\PASSWORD MANAGER\\shield.ico')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import *
from kivymd.uix.datatables import MDDataTable
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
import pyperclip
import json
import os


Entryscreen = '''
Screen:
    id: EntryScreen
    name: "EntryScreen"

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'PASSWORD MANAGER'
            anchor_title: 'center'
        ScrollView:

    MDTextField:
        id: MasterPwd
        text: ''
        mode: 'rectangle'
        password: True
        size_hint_x: 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        hint_text: "Enter Master Password"
        font_size: 28

    MDIconButton:
        id: iconbutton
        icon: "eye-off"
        size_hint_x: 0.8
        pos_hint: {"center_x": 0.78, "center_y": 0.55}
        on_press: app.password_main()

    MDRaisedButton:
        text: "ADD PASSWORD"
        bold: True
        size_hint_x: 0.3
        pos_hint: {"center_x": 0.348, "center_y": 0.4}
        on_press: app.confirmed_view("AddPwd")

    MDRaisedButton:
        text: "REMOVE PASSWORD"
        bold: True
        size_hint_x: 0.3
        pos_hint: {"center_x": 0.652, "center_y": 0.4}
        on_press: app.confirmed_view("Remove")

    MDRaisedButton:
        text: "VIEW PASSWORDS"
        bold: True
        size_hint_x: 0.604
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_press: app.confirmed_view("View")
        # screen_manager.current = "ViewScreen"
'''

Viewscreen = '''
Screen:
    id: ViewScreen
    name: "ViewScreen"

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'VIEW PASSWORDS'
            anchor_title: 'center'
            left_action_items: [['backburger', lambda x: app.backburger()]]
        ScrollView:
'''

Add_pwd_screen = '''
Screen:
    id: AddPwdScreen
    name: "AddPwdScreen"

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'ADD PASSWORD'
            anchor_title: 'center'
            left_action_items: [['backburger', lambda x: app.backburger()]]
        ScrollView:

    MDTextField:
        id: title
        text: ''
        size_hint_x: 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        hint_text: "Enter Title"
        font_size: 28

    MDTextField:
        id: add_password
        text: ''
        password: True
        size_hint_x: 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        hint_text: "Enter Password"
        font_size: 28

    MDIconButton:
        id: iconeshbutton
        icon: "eye-off"
        size_hint_x: 0.8
        pos_hint: {"center_x": 0.78, "center_y": 0.47}
        on_press: app.password_add()

    MDRaisedButton:
        text: "ADD PASSWORD"
        size_hint_x: 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_press: app.add_password()
'''

Remove_pwd_screen = '''
Screen:
    id: RemoveScreen
    name: "RemoveScreen"

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'DELETE PASSWORD'
            anchor_title: 'center'
            left_action_items: [['backburger', lambda x: app.backburger()]]
        ScrollView:
'''


class PasswordManager(MDApp):

    def build(self):
        self.title = 'Password Manager'
        self.master_password = os.environ.get('MASTER PASSWORD')
        self.screen_manager = ScreenManager(transition = SlideTransition())
        self.entry_screen = Builder.load_string(Entryscreen)
        self.view_screen = Builder.load_string(Viewscreen)
        self.add_screen = Builder.load_string(Add_pwd_screen)
        self.del_screen = Builder.load_string(Remove_pwd_screen)
        self.screen_manager.add_widget(self.entry_screen)
        self.screen_manager.add_widget(self.view_screen)
        self.screen_manager.add_widget(self.add_screen)
        self.screen_manager.add_widget(self.del_screen)
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Blue'
        return self.screen_manager

    def on_start(self):
        with open('passwords.json', 'r') as passwds:
            raw_data = passwds.read()

        data = json.loads(raw_data)

        self.row_data = []
        for i in data.keys():
            tuple_temp = (i, data[i])
            self.row_data.append(tuple_temp)

        self.table_viewScreen = MDDataTable(
            size_hint_x = 0.9,
            size_hint_y = 0.8,
            elevation = 12,
            pos_hint = {"center_x": 0.5, "center_y": 0.45},
            column_data = [
                ("Account", 50),
                ("Password", 50)
            ],
            row_data = self.row_data,
            use_pagination = True,
            rows_num = 5
        )
        self.table_viewScreen.bind(on_row_press=self.row_press)
        self.view_screen.add_widget(self.table_viewScreen)

        self.table_removeScreen = MDDataTable(
            size_hint_x = 0.9,
            size_hint_y = 0.8,
            elevation = 12,
            pos_hint = {"center_x": 0.5, "center_y": 0.45},
            check = True,
            column_data = [
                ("Account", 50),
                ("Password", 50)
            ],
            row_data = self.row_data,
            use_pagination = True,
            rows_num = 5
        )
        self.table_removeScreen.bind(on_check_press=self.check_press)
        self.del_screen.add_widget(self.table_removeScreen)

    def row_press(self, instance_table, instance_row):
        index = instance_row.index
        if index == 0:
            clicked_val = self.table_viewScreen.row_data[0][1]
        else:
            clicked_val = self.table_viewScreen.row_data[index//2][1]
        pyperclip.copy(clicked_val)
        toast("Password has been copied to clipboard")

    def check_press(self, instance_table, current_row):
        title = current_row[0]
        pwd = current_row[1]
        space1 = "     " 
        space2 = "     "*2 
        self.dialog = MDDialog(
            text=f"{space1}Would you like to remove\n\n{space2}TITLE             :  {title}\n{space2}PASSWORD  :  {pwd}\n\n{space1}from the list?",
            buttons=[
                    MDRaisedButton(
                        text="YES",
                        on_press = lambda _: self.delete_password(current_row)
                    ),
                    MDRaisedButton(
                        text="NO",
                        on_press = lambda _: self.dialog.dismiss()
                    ),
                ]
        )
        self.dialog.open()

    def password_main(self):
        if self.entry_screen.ids.MasterPwd.password == True:
            self.entry_screen.ids.MasterPwd.password = False
            self.entry_screen.ids.iconbutton.icon = "eye"
        else:
            self.entry_screen.ids.MasterPwd.password = True
            self.entry_screen.ids.iconbutton.icon = "eye-off"

    def password_add(self):
        if self.add_screen.ids.add_password.password == True:
            self.add_screen.ids.add_password.password = False
            self.add_screen.ids.iconeshbutton.icon = "eye"
        else:
            self.add_screen.ids.add_password.password = True
            self.add_screen.ids.iconeshbutton.icon = "eye-off"

    def confirmed_view(self, btn):
        if self.entry_screen.ids.MasterPwd.text == self.master_password:
            toast("Password is right. You have gained access to all your passwords!!!")
            self.screen_manager.current = f"{btn}Screen"
        else:
            toast("Password is wrong. Access denied.")
        self.entry_screen.ids.MasterPwd.text = ''

    def add_password(self):
        if self.add_screen.ids.title.text.isspace():
            toast("Title needs to have characters other than space.")
        else:
            if self.add_screen.ids.add_password.text.isspace():
                toast("Password needs to have characters other than space.")
            else:
                    with open('passwords.json', 'r') as passwds:
                        raw_data = passwds.read()

                    data = json.loads(raw_data)
                    if self.add_screen.ids.title.text in data.keys():
                        toast("Title already exists for another password. Enter another title.")

                    else:
                        data[self.add_screen.ids.title.text] = self.add_screen.ids.add_password.text
                        with open('passwords.json', 'w') as passwds:
                            json.dump(data, passwds, indent=4)
                        toast("Password has been added!!!")
                        self.view_screen.remove_widget(self.table_removeScreen)
                        self.del_screen.remove_widget(self.table_viewScreen)
                        self.on_start()
        self.add_screen.ids.title.text = ''
        self.add_screen.ids.add_password.text = ''

    def delete_password(self, listesh):
        self.dialog.dismiss()
        with open('passwords.json', 'r') as passwds:
            raw_data = passwds.read()

        data = json.loads(raw_data)
        if listesh[0] in data.keys():
            toast(f"{listesh[0]} : {data.pop(listesh[0])} has been deleted.")
            with open('passwords.json', 'w') as passwds:
                json.dump(data, passwds, indent=4)
        else:
            toast(f"Something went wrong.")
        self.view_screen.remove_widget(self.table_removeScreen)
        self.del_screen.remove_widget(self.table_viewScreen)
        self.on_start()

    def backburger(self):
            self.screen_manager.transition = SlideTransition(direction = 'right')
            self.screen_manager.current = "EntryScreen"
            self.screen_manager.transition = SlideTransition(direction = 'left')



if __name__ == '__main__':
    PasswordManager().run()
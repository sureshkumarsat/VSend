
from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '500')
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem, OneLineAvatarIconListItem
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.list import OneLineListItem
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.chip import MDChip, MDChooseChip
from kivy.properties import StringProperty
from kivymd.toast import toast
import json
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
import time


AddAlarmScreen = '''
<OneLineCheckListItem>:
    id: list_text
    text: root.text
    MDCheckbox:
        id: check
        pos_hint: {"center_x": 0.9, "center_y": 0.5}
        on_active: app.days_check_turned(*args, list_text.text)


Screen:
    id: AddAlarmScreen
    name: 'AddAlarmScreen'
    on_pre_enter: app.reset_addAlarm()

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: ToolBar
            title: 'ADD ALARM'
            specific_text_color: [0,0,0,1]
            left_action_items: [['backburger', lambda x: app.BackToMain()]]
            right_action_items: [['yin-yang', lambda x: app.change_theme()]]
        Widget:

    MDTextField:
        id: AlarmName
        mode: 'rectangle'
        hint_text: 'Alarm Tag / Name'
        font_size: '20sp'
        size_hint_x: 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.86}

    MDIconButton:
        icon: 'tag'
        pos_hint: {"center_x": 0.88, "center_y": 0.855}

    MDLabel:
        id: alarm_time
        text: ''#'00:00[size=40] a.m[/size]'
        halign: 'center'
        font_size: 60
        markup: True
        pos_hint: {"center_x": 0.5, "center_y": 0.77}

    MDRaisedButton:
        text: 'SELECT TIME'
        size_hint_x: 0.4
        pos_hint: {"center_x": 0.5, "center_y": 0.68}
        on_release: app.time_picker.open()

    MDList:
        pos_hint: {"center_y": 0.6}
        OneLineIconListItem:
            text: 'Repeat Everyday?'
            IconLeftWidget:
                id: freq_icon
                icon: 'circle-slice-8'
                on_press: app.everyday_freq_check()

    MDList:
        id: alarm_days
        pos_hint: {"center_y": 0.32}

    MDRaisedButton:
        text: 'ADD'
        size_hint_x: 0.4
        pos_hint: {"center_x": 0.5, "center_y": 0.04}
        on_release: app.Add_Alarm()
'''


screen = '''
<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"


<Content>:
    id: Dialog_box
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "250dp"
    MDTextField:
        id: name_note
        mode: 'rectangle'
        hint_text: 'Enter Task Name'
    MDTextField:
        id: desc_note
        mode: 'rectangle'
        hint_text: 'Enter Brief Description'
    ScrollView:
        MDList:
            ItemConfirm:
                id: important
                text: 'Important'
            ItemConfirm:
                id: regular
                text: 'Regular'
            ItemConfirm:
                id: basic
                text: 'Basic'
            ItemConfirm:
                id: urgent
                text: 'Urgent'
            ItemConfirm:
                id: leisure
                text: 'Leisure'


<CustomCardSwipe>:
    size_hint_y: None
    height: content.height
    MDCardSwipeLayerBox:
        padding: "8dp"
        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            on_release: app.remove_note(root)
    MDCardSwipeFrontBox:
        ThreeLineIconListItem:
            id: content
            text: root.text
            secondary_text: root.secondary_text
            tertiary_text: root.tertiary_text
            on_press: print(content.text)
            IconLeftWidget:
                icon: root.icon


<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height

    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            on_release: app.remove_alarm(root)

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
    name: 'MainScreen'

    BoxLayout:
        id: MainBox
        orientation: 'vertical'
        MDToolbar:
            id: MainToolBar
            title: 'ALARM'
            right_action_items: [['theme-light-dark', lambda x: app.change_theme()]]

        MDBottomNavigation:

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'ALARM'
                icon: 'alarm'
                on_tab_press:
                    MainToolBar.title = 'ALARM'
                    app.onAlarmEnter()

                MDScrollViewRefreshLayout:
                    id: refresh_layout_alarm
                    refresh_callback: app.refresh_callback_alarm
                    root_layout: root
                    MDList:
                        id: MDListesh
                        spacing: '8dp'
                        padding: '12dp'

                MDFloatingActionButton:
                    icon: 'alarm-plus'
                    pos_hint: {"center_x": 0.85, "center_y": 0.1}
                    on_release: app.screen_manager.current = 'AddAlarmScreen'

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'TASKS'
                icon: 'view-list'
                on_tab_press: 
                    MainToolBar.title = 'NOTES'
                    app.onNotesEnter()

                MDScrollViewRefreshLayout:
                    id: refresh_layout_notes
                    refresh_callback: app.refresh_callback_notes
                    root_layout: root
                    MDList:
                        id: MDNotesList
                        spacing: '8dp'
                        padding: '12dp'

                MDFloatingActionButton:
                    icon: 'notebook-plus-outline'
                    pos_hint: {"center_x": 0.85, "center_y": 0.1}
                    on_release: app.dialog_task.open()

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'STOPWATCH'
                icon: 'progress-clock'
                on_tab_press: MainToolBar.title = 'STOPWATCH'

                MDFloatingActionButton:
                    id: startstop
                    icon: "play"
                    pos_hint: {"center_x": 0.3, "center_y": 0.1}
                    on_release: app.startORstop()

                MDFloatingActionButton:
                    id: resetlap
                    icon: "refresh"
                    pos_hint: {"center_x": 0.7, "center_y": 0.1}
                    on_press: app.resetORlap()

                MDLabel:
                    id: stopwatch_timer
                    text: '00:00.[size=40]00[/size]'
                    halign: 'center'
                    font_size: 60
                    markup: True
                    pos_hint: {"center_x": 0.5, "center_y": 0.85}

                ScrollView:
                    size_hint_x: 0.7
                    size_hint_y: 0.5
                    pos_hint: {"center_x": 0.5, "center_y": 0.45}
                    MDList:
                        id: lap_list

            MDBottomNavigationItem:
                name: 'screen 4'
                text: 'TIMER'
                icon: 'camera-timer'
                on_tab_press: MainToolBar.title = 'TIMER'

                MDFloatingActionButton:
                    id: timerstartstop
                    icon: "play"
                    pos_hint: {"center_x": 0.3, "center_y": 0.1}
                    # on_release: app.startORstop()

                MDFloatingActionButton:
                    id: timerreset
                    icon: "refresh"
                    pos_hint: {"center_x": 0.7, "center_y": 0.1}
                    # on_press: app.resetORlap()

                MDLabel:
                    id: timer_stopwatch_timer
                    text: '00:00.[size=40]00[/size]'
                    halign: 'center'
                    font_size: 60
                    markup: True
                    pos_hint: {"center_x": 0.5, "center_y": 0.85}

                MDTextField:
                    id: timer_min_input
                    font_size: 24
                    pos_hint: {"center_x": 0.5, "center_y": 0.55}
                    size_hint_x: 0.3
                    input_filter: 'int'
                    max_text_length: 3
                    on_text: app.set_timer()#timer_stopwatch_timer.text = f'{timer_min_input.text}:00.[size=40]00[/size]'

'''


class Content(MDBoxLayout):
    pass


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class OneLineCheckListItem(OneLineListItem):
    text = StringProperty()


class CustomCardSwipe(MDCardSwipe):
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()
    icon = StringProperty()


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()


class CLOCKApp(MDApp):
    sw_seconds = 0
    sw_started = False
    lap_count = 0
    x = 0
    y = 15
    alarm_time = None
    options_for_alarm = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    everyday = True
    options_for_alarm_chosen = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    timer_seconds = 0
    timer_started = False
    timer_minutes = 0
    word = 'Welcome To Your Personal Task Reminder!!!'

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.screen_manager = ScreenManager(transition = SlideTransition())
        self.app_build = Builder.load_string(screen)
        self.AddAlarmScreen = Builder.load_string(AddAlarmScreen)
        self.screen_manager.add_widget(self.app_build)
        self.screen_manager.add_widget(self.AddAlarmScreen)
        self.time_picker = MDTimePicker()
        self.time_picker.bind(time=self.get_time)
        self.dialog_task = MDDialog(
            title="Add Note",
            type="custom",
            content_cls = Content(),
            buttons=[
                MDRaisedButton(
                    text="ADD NOTE",
                    theme_text_color = 'Custom',
                    text_color = (0, 0, 0, 1),#self.theme_cls.primary_color,
                    on_release = lambda _: self.AddNote()
                ),
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = lambda _: self.close_dialogue()
                ),
            ],
        )
        return self.screen_manager

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)
        self.onAlarmEnter()
        self.onNotesEnter()


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ALARM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def remove_alarm(self, instance):
        print(instance.text, instance.secondary_text, instance.tertiary_text)
        with open('BIGGER PROJECTS\\alarms.json', 'r') as AlarmsFile:
            data = json.load(AlarmsFile)
        data.pop(instance.text)
        with open('BIGGER PROJECTS\\alarms.json', 'w') as NewAlarmsFile:
            json.dump(data, NewAlarmsFile, indent = 4)
        self.app_build.ids.MDListesh.remove_widget(instance)
        toast(f"Alarm with tage '{instance.text}' has been deleted.")
        self.onAlarmEnter()

    def onAlarmEnter(self):
        self.app_build.ids.MDListesh.clear_widgets()
        with open('BIGGER PROJECTS\\alarms.json', 'r') as AlarmsFile:
            data = json.load(AlarmsFile)
        for i in data.keys():
            text = data[i][0]
            s_text = i
            t_text = ''
            for j in data[i][1]:
                t_text += f"{j},"
            item = SwipeToDeleteItem(text = s_text, secondary_text = text, tertiary_text = t_text)
            self.app_build.ids.MDListesh.add_widget(item)

    def get_time(self, widget, time):
        self.alarm_time = time
        timesh = str(time)
        print(timesh)
        houresh = time.hour
        if houresh < 12:
            if houresh < 10:
                timesh = f'0{houresh}:{str(time)[3:5]}[size=40] a.m[/size]'
            else:
                timesh = f'{houresh}:{str(time)[3:5]}[size=40] a.m[/size]'
        else:
            houresh -= 12
            if houresh < 10:
                timesh = f'0{houresh}:{str(time)[3:5]}[size=40] p.m[/size]'
            else:
                timesh = f'{houresh}:{str(time)[3:5]}[size=40] p.m[/size]'
        self.AddAlarmScreen.ids.alarm_time.text = timesh
        self.AddAlarmScreen.ids.alarm_time.markup = True

    def set_list(self):
        self.onAlarmEnter()

    def refresh_callback_alarm(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback_alarm(interval):
            self.app_build.ids.MDListesh.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list()
            self.app_build.ids.refresh_layout_alarm.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback_alarm, 1)

    def everyday_freq_check(self):
        if self.AddAlarmScreen.ids.freq_icon.icon == 'circle-slice-8':
            self.everyday = False
            self.options_for_alarm_chosen = []
            self.AddAlarmScreen.ids.freq_icon.icon = 'checkbox-blank-circle-outline'
            for i in self.options_for_alarm:
                item = OneLineCheckListItem(text = i)
                self.AddAlarmScreen.ids.alarm_days.add_widget(item)
        else:
            self.everyday = True
            self.options_for_alarm_chosen = self.options_for_alarm
            self.AddAlarmScreen.ids.freq_icon.icon = 'circle-slice-8'
            self.AddAlarmScreen.ids.alarm_days.clear_widgets()
        print(self.options_for_alarm_chosen)

    def days_check_turned(self, checkbox, value, list_text):
        print(checkbox.state, value, list_text)
        if value:
            self.options_for_alarm_chosen.append(list_text)
        else:
            try:
                self.options_for_alarm_chosen.remove(list_text)
            except ValueError:
                pass
        print(self.options_for_alarm_chosen)

    def Add_Alarm(self):
        with open('BIGGER PROJECTS\\alarms.json', 'r') as AlarmsFile:
            raw_data = AlarmsFile.read()
            data = json.loads(raw_data)
        print(data)
        if self.AddAlarmScreen.ids.AlarmName.text == '' or self.AddAlarmScreen.ids.AlarmName.text.isspace():
            toast('All fields are required to be entered. Enter name of the alarm.')
        elif self.AddAlarmScreen.ids.AlarmName.text in data.keys():
            toast('Alarm Tag already exists. Please Enter a valid one.')
        else:
            if self.alarm_time == None:
                toast('All fields are required to be entered. Select time of the alarm.')
            else:
                if self.options_for_alarm_chosen == []:
                    toast('All fields are required to be entered. Select days the alarm has to ring.')
                else:
                    print(self.AddAlarmScreen.ids.AlarmName.text)
                    print(self.alarm_time)
                    print(self.options_for_alarm_chosen)
                    new_alarm_details = [f"{self.alarm_time}", self.options_for_alarm_chosen]
                    data[f"{self.AddAlarmScreen.ids.AlarmName.text}"] = new_alarm_details
                    print(data)
                    with open('BIGGER PROJECTS\\alarms.json', 'w') as NewAlarmsFile:
                        json.dump(data, NewAlarmsFile, indent=4)
                        toast('Alarm added successfully!')
        self.AddAlarmScreen.ids.AlarmName.text = ''
        self.alarm_time = None
        self.AddAlarmScreen.ids.alarm_time.text = ''
        self.AddAlarmScreen.ids.freq_icon.icon = 'checkbox-blank-circle-outline'
        self.everyday_freq_check()

    def reset_addAlarm(self):
        self.AddAlarmScreen.ids.AlarmName.text = ''
        self.alarm_time = None
        self.AddAlarmScreen.ids.alarm_time.text = ''
        self.AddAlarmScreen.ids.freq_icon.icon = 'checkbox-blank-circle-outline'
        self.everyday_freq_check()

    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~NOTES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def remove_note(self, instance):
        with open('BIGGER PROJECTS\\tasks.json', 'r') as TasksFile:
            data = json.load(TasksFile)
        data.pop(instance.text)
        with open('BIGGER PROJECTS\\tasks.json', 'w') as NewTasksFile:
            json.dump(data, NewTasksFile, indent = 4)
        toast('Task has been removed.')
        self.app_build.ids.MDNotesList.remove_widget(instance)

    def onNotesEnter(self):
        self.app_build.ids.MDNotesList.clear_widgets()
        with open('BIGGER PROJECTS\\tasks.json', 'r') as TasksFile:
            data = json.load(TasksFile)
        for i in data.keys():
            text = i
            secondary_text = data[i]["Priority"]
            tertiary_text = data[i]["BriefDesc"]
            if data[i]["Priority"] == "Important":
                icon = 'star'
            elif data[i]["Priority"] == "Urgent":
                icon = 'alert'
            elif data[i]["Priority"] == "Leisure":
                icon = 'bed'
            elif data[i]["Priority"] == "Regular":
                icon = 'calendar'
            else:
                icon = 'circle-slice-8'
            item = CustomCardSwipe(text = text, secondary_text = secondary_text, tertiary_text = tertiary_text, icon = icon)
            self.app_build.ids.MDNotesList.add_widget(item)

    def close_dialogue(self):
        self.dialog_task.content_cls.ids.name_note.text = ''
        self.dialog_task.content_cls.ids.desc_note.text = ''
        self.dialog_task.content_cls.ids.important.ids.check.active = False
        self.dialog_task.content_cls.ids.regular.ids.check.active = False
        self.dialog_task.content_cls.ids.basic.ids.check.active = False
        self.dialog_task.content_cls.ids.urgent.ids.check.active = False
        self.dialog_task.content_cls.ids.leisure.ids.check.active = False
        self.dialog_task.dismiss()

    def AddNote(self):
        with open('BIGGER PROJECTS\\tasks.json', 'r') as TasksFile:
            data = json.load(TasksFile)
        print(data)
        TaskName = self.dialog_task.content_cls.ids.name_note.text
        TaskDesc = self.dialog_task.content_cls.ids.desc_note.text
        Priority = None
        if self.dialog_task.content_cls.ids.important.ids.check.active:
            Priority = 'Important'
        else:
            if self.dialog_task.content_cls.ids.regular.ids.check.active:
                Priority = 'Regular'
            else:
                if self.dialog_task.content_cls.ids.basic.ids.check.active:
                    Priority = 'Basic'
                else:
                    if self.dialog_task.content_cls.ids.urgent.ids.check.active:
                        Priority = 'Urgent'
                    else:
                        if self.dialog_task.content_cls.ids.leisure.ids.check.active:
                            Priority = 'Leisure'
        if TaskName == '' or TaskName.isspace():
            toast('All fields are required. Please enter name of the task.')
        else:
            if TaskName in data.keys():
                toast('Task name already exists. Enter a new one.')
            else:
                print("Name is unique")
                if TaskDesc == '' or TaskDesc.isspace():
                    toast('All fields are required. Please enter desc of the task.')
                else:
                    print("Desc passed.")
                    if Priority == None:
                        toast('All fields are required. Please select a priority level')
                    else:
                        print("Priority selected")
                        data_new = {f"{TaskName}" : {"BriefDesc": TaskDesc, "Priority": Priority}}
                        print(data_new)
                        data.update(data_new)
                        print(data)
                        with open('BIGGER PROJECTS\\tasks.json', 'w') as NewTasksFile:
                            json.dump(data, NewTasksFile, indent = 4)
                        toast('Task has been added.')
                        self.close_dialogue()
        self.dialog_task.content_cls.ids.name_note.text = ''
        self.dialog_task.content_cls.ids.desc_note.text = ''
        self.dialog_task.content_cls.ids.important.ids.check.active = False
        self.dialog_task.content_cls.ids.regular.ids.check.active = False
        self.dialog_task.content_cls.ids.basic.ids.check.active = False
        self.dialog_task.content_cls.ids.urgent.ids.check.active = False
        self.dialog_task.content_cls.ids.leisure.ids.check.active = False

    def set_list_notes(self):
        self.onNotesEnter()

    def refresh_callback_notes(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback_notes(interval):
            self.app_build.ids.MDNotesList.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list_notes()
            self.app_build.ids.refresh_layout_notes.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback_notes, 1)


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STOPWATCH~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def update_time(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
            minutes, seconds = divmod(self.sw_seconds, 60)
            part_seconds = seconds * 100 % 100
            self.app_build.ids.stopwatch_timer.text = f'{int(minutes):02}:{int(seconds):02}.[size=40]{int(part_seconds):02}[/size]'

    def startORstop(self):
        self.sw_started = not self.sw_started
        if self.sw_started:
            self.app_build.ids.startstop.icon = 'pause'
            self.app_build.ids.startstop.md_bg_color = 0, 1, 0
            self.app_build.ids.resetlap.icon = 'timelapse'
        else:
            self.app_build.ids.startstop.icon = 'play'
            self.app_build.ids.startstop.md_bg_color = self.theme_cls.primary_color
            self.app_build.ids.resetlap.icon = 'refresh'

    def resetORlap(self):
        if self.sw_started:
            self.lap_count += 1
            lap = self.app_build.ids.stopwatch_timer.text
            lap = lap.replace('[size=40]', '')
            lap = lap.replace('[/size]', '')
            item = OneLineListItem(text = f"Lap {self.lap_count}          :          {lap}")
            self.app_build.ids.lap_list.add_widget(item)
        else:
            self.lap_count = 0
            self.app_build.ids.stopwatch_timer.text = "00:00.[size=40]00[/size]"
            self.sw_seconds = 0
            self.app_build.ids.lap_list.clear_widgets()


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ALARM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def set_timer(self):
        if not self.timer_started:
            if 0 < len(self.app_build.ids.timer_min_input.text) < 4:
                self.app_build.ids.timer_stopwatch_timer.text = f'{self.app_build.ids.timer_min_input.text}:00.[size=40]00[/size]'
                self.app_build.ids.timer_stopwatch_timer.markup = True
                self.timer_minutes = int(self.app_build.ids.timer_min_input.text)
                # minutes, seconds = divmod(self.timer_seconds, 60)
                # part_seconds = seconds * 100 % 100
                # self.app_build.ids.stopwatch_timer.text = f'{int(minutes):02}:{int(seconds):02}.[size=40]{int(part_seconds):02}[/size]'
            elif len(self.app_build.ids.timer_min_input.text) == 0:
                self.app_build.ids.timer_stopwatch_timer.text = f'00:00.[size=40]00[/size]'
                self.app_build.ids.timer_stopwatch_timer.markup = True
                self.timer_minutes = 0
            print(self.timer_minutes)


    def startORstop(self):
        self.sw_started = not self.sw_started
        if self.sw_started:
            self.app_build.ids.startstop.icon = 'pause'
            self.app_build.ids.startstop.md_bg_color = 0, 1, 0
            self.app_build.ids.resetlap.icon = 'timelapse'
        else:
            self.app_build.ids.startstop.icon = 'play'
            self.app_build.ids.startstop.md_bg_color = self.theme_cls.primary_color
            self.app_build.ids.resetlap.icon = 'refresh'

    def resetORlap(self):
        if self.sw_started:
            self.lap_count += 1
            lap = self.app_build.ids.stopwatch_timer.text
            lap = lap.replace('[size=40]', '')
            lap = lap.replace('[/size]', '')
            item = OneLineListItem(text = f"Lap {self.lap_count}          :          {lap}")
            self.app_build.ids.lap_list.add_widget(item)
        else:
            self.lap_count = 0
            self.app_build.ids.stopwatch_timer.text = "00:00.[size=40]00[/size]"
            self.sw_seconds = 0
            self.app_build.ids.lap_list.clear_widgets()


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GENERAL~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def BackToMain(self):
        self.screen_manager.transition = SlideTransition(direction = 'right')
        self.screen_manager.current = 'MainScreen'
        self.screen_manager.transition = SlideTransition(direction = 'left')

    def change_theme(self):
        self.theme_cls.theme_style = 'Dark' if self.theme_cls.theme_style == 'Light' else 'Light'


CLOCKApp().run()
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from instructions import *

lbl_color = (.0, .0, .0, 0.5)
btn_color = (.56, .83, .3, 1.6)

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

name = ""
age = 7
p1 = 0
p2 = 0
p3 = 0


class IntroduceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        inst_lbl = Label(text=txt_instruction, color=lbl_color, bold=True)

        name_lbl = Label(text="Введіть ім'я", color=lbl_color, bold=True, font_size=30)
        self.name_input = TextInput(text="Mикола", multiline=False)
        age_lbl = Label(text="Введіть вік", color=lbl_color, bold=True, font_size=30)
        self.age_input = TextInput(text="7", multiline=False)

        self_btn = Button(
            text="Почати",
            bold=True,
            font_size=15,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )

        self_btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')

        line1.add_widget(name_lbl)
        line1.add_widget(self.name_input)

        line2.add_widget(age_lbl)
        line2.add_widget(self.age_input)

        main_line = BoxLayout(orientation='vertical', padding=15, spacing=20)
        main_line.add_widget(inst_lbl)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self_btn)

        self.add_widget(main_line)

    def next(self):
        if self.name_input.text:
            name  = self.name_input.text
            age = check_int(self.age_input.text)
        if age is False or age < 7 or name == "":
            self.age_input.text = "7"
            self.name_input = "Микола"
        else:
            self.manager.current = "second"    

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = True

        inst_lbl = Label(text=txt_test1, color=lbl_color, bold=True)

        lbl_time = Label(text="Пройшло секунд: 0", bold = True)
        lbl_result = Label(text="Введіть результат", color=lbl_color, bold=True, font_size=35)
        self.result_input = TextInput(text="1", multiline=False)
        #self.result_input.set_disabled(True)

        self_btn = Button(
            text="Почати",
            bold=True,
            font_size=15,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )

        self_btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl_result)
        line1.add_widget(self.result_input)

        main_line = BoxLayout(orientation='vertical', padding=15, spacing=20)
        main_line.add_widget(inst_lbl)
        main_line.add_widget(lbl_time)
        main_line.add_widget(line1)
        main_line.add_widget(self_btn)

        self.add_widget(main_line)

    def next(self):
        if self.next_screen is False:
            pass
        else:
            p1 = check_int(self.result_input.text)
            if p1 is False or p1 <= 1:
                self.result_input.text = "1"
            else:
                self.manager.current = "third"

class ThirdScreen(Screen):
    ...

class FourthScreen(Screen):
    ...

class ResultScreen(Screen):
    ...

class HeartCheck(App):
    def build(self):
        Window.clearcolor = (.56, .83, .3, 1)
        self.title = "Heart Check"
        self.icon = "icon.png"
        sm = ScreenManager()
        sm.add_widget(IntroduceScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(ResultScreen(name='result'))
        return sm
    
app = HeartCheck()
app.run()




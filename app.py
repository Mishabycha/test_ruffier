from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from timer import Timer

from instructions import *

from ruffier import *

lbl_color = (.500, .500, .500, 0.5)
btn_color = (.500, .500, .500, 0.5)

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

        self.btn = Button(
            text = "Продовжити",
            bold=True,
            font_size=15,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )

        self.btn.on_press = self.next

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
        main_line.add_widget(self.btn)

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
        self.next_screen = False

        inst_lbl = Label(text=txt_test1, color=lbl_color, bold=True)

        self.lbl_time = Timer(txt="Пройшло секунд: ",total=15 ,bold=True)
        lbl_result = Label(text="Введіть результат", color=lbl_color, bold=True, font_size=35)
        self.lbl_time.bind(done=self.end_timer)
        self.result_input = TextInput(text="1", multiline=False)
        self.result_input.set_disabled(True)

        self.btn = Button(
            text="Почати",
            bold=True,
            font_size=15,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )

        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl_result)
        line1.add_widget(self.result_input)

        main_line = BoxLayout(orientation='vertical', padding=15, spacing=20)
        main_line.add_widget(inst_lbl)
        main_line.add_widget(self.lbl_time)
        main_line.add_widget(line1)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def end_timer(self, *args):
        self.result_input.set_disabled(False)
        self.next_screen = True
        self.btn.text = "Продовжити"

    def next(self):
        global p1
        if self.next_screen is False:
            self.lbl_time.start()
        else:
            p1 = check_int(self.result_input.text)
            if p1 is False or p1 <= 1:
                self.result_input.text = "1"
            else:
                self.manager.current = "third"

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        inst_lbl = Label(text=txt_test2, color=lbl_color, bold=True, size_hint=(1, 1))

        lbl_prus = Label(text="Залишилось присідань: 30", bold=True, size_hint=(1.2, 1))
        self.lbl_secs = Timer(txt="Пройшло секунд: ", total=45, bold=True, size_hint=(1.1, 1))
        self.lbl_secs.bind(done=self.end_timer)
        #self.result_input.set_disabled(True)

        self.btn = Button(
            text="Почати",
            bold=True,
            font_size=15,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )

        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl_prus)
        line2.add_widget(self.lbl_secs)

        main_line = BoxLayout(orientation='vertical', padding=15, spacing=20)
        main_line.add_widget(inst_lbl)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def end_timer(self, *args):
        self.next_screen = True
        self.btn.set_disabled(False)
        self.btn.text = "Продовжити"

    def next(self):
        if self.next_screen is False:
            self.lbl_secs.start()
            self.btn.set_disabled(True)
        else:
            self.manager.current = 'fourth'

class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.next_screen = False
        self.stage = 1

        inst_lbl = Label(text=txt_test3, color=lbl_color, bold=True)

        self.count_lbl = Label(text="Рахуйте пульс", bold=True)
        self.second_lbl = Timer(txt="Пройшло секунд: ", total=15, bold=True)
        self.second_lbl.bind(done=self.end_timer)
        result_lbl = Label(text="Результат:", color=lbl_color, bold=True, font_size=30, size_hint=(1.2, 1))
        self.result_input = TextInput(text="0", multiline=False)
        rest_result_lbl = Label(text="Результат після відпочинку:", color=lbl_color, bold=True, font_size=30, size_hint=(1.2, 1))
        self.rest_result_input = TextInput(text="0", multiline=False)
        self.rest_result_input.set_disabled(True)
        self.result_input.set_disabled(True)

        self.btn = Button(
            text="Почати",
            bold=True,
            font_size=15,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )

        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')

        line1.add_widget(result_lbl)
        line1.add_widget(self.result_input)

        line2.add_widget(rest_result_lbl)
        line2.add_widget(self.rest_result_input)


        main_line = BoxLayout(orientation='vertical', padding=15, spacing=20)
        main_line.add_widget(inst_lbl)
        main_line.add_widget(self.count_lbl)
        main_line.add_widget(self.second_lbl)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def end_timer(self, *args):
        if self.second_lbl.done:
            if self.stage == 1:
                self.stage = 2
                self.second_lbl.restart(30)
                self.result_input.set_disabled(False)
                self.btn.set_disabled(False) 
                self.count_lbl.text = "Відпочивайте"
            elif self.stage == 2:
                self.stage = 3
                self.second_lbl.restart(15)
                self.btn.set_disabled(False) 
                self.count_lbl.text = "Рахуйте пульс"
            elif self.stage == 3:
                self.next_screen = True
                self.count_lbl.text = "Введіть пульс"
                self.rest_result_input.set_disabled(False)
                self.btn.text = "Завершити" 
                self.btn.set_disabled(False) 
        
    def next(self):
        global p2, p3
        if self.next_screen is False:
            self.second_lbl.start()
            self.btn.set_disabled(True) 
        else:
            p2 = check_int(self.result_input.text)
            p3 = check_int(self.rest_result_input.text)
            if p2 is False or p2 <= 1:
                self.result_input.text = "1"
            elif p3 is False or p3 <= 1:
                self.rest_result_input.text = "1"
            else:
                self.manager.current = "result"

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lbl = Label(text="")
        self.add_widget(self.lbl)
        self.on_enter = self.before

    def before(self):
        text = test(p1, p2, p3, age)
        self.lbl.text = text    

class HeartCheck(App):
    def build(self):
        Window.clearcolor = (.0, .140, .255, 1)
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




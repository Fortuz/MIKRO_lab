from kivy.base import runTouchApp
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

default_list = ['Python', 'Kivy', 'Tkinter']
first_row = ['abc', 'def', 'ghi', 'jkl']


col_found = GridLayout(cols=1)


def show_dropdown(button, *largs):
    dp = DropDown()
    dp.bind(on_select=lambda instance, x: setattr(button, 'text', x))

    for i in range(len(first_row)):
        item = Button(text=str(first_row[i]) + '%d' % i, size_hint_y=None, height=24, color=(1, 1, 1, 1))
        item.bind(on_release=lambda btn: dp.select(btn.text))
        dp.add_widget(item)
    dp.open(button)


for i in range(len(default_list)):
    btn = Button(text=default_list[i], color=(1, 1, 1, 1), size_hint=(None, None))
    btn.bind(on_release=show_dropdown)
    col_found.add_widget(btn)


runTouchApp(col_found)

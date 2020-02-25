from kivy.app import App

from kivy.uix.button import Label

class KivyButton(App):

    def build(self):

        return Label(text='[u][color=ff0066][b]Welcome[/b][/color] To [i][color=ff9933]Like[/i]Geeks[/color][/u]', markup = True)

KivyButton().run()

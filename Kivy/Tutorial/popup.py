from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder


Builder.load_string("""

<NoTitleDialog>:
    title: ""                 # <<<<<<<<
    separator_height: 0       # <<<<<<<<
    size_hint: None, None
    size: 400, 200

    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Are you sure you want to exit?"
        BoxLayout: 
            size_hint_y: 0.3   
            Button:
                text: "Yes"
            Button:
                text: "No"

""")


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.dialog = NoTitleDialog()
        self.dialog.open()


class NoTitleDialog(Popup):
    pass


class Example(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    Example().run()
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty # ID reference
from kivy.graphics import Color, Rectangle # Background color
from kivy.uix.image import Image   
from kivy.properties import StringProperty   
from kivy.uix.popup import Popup     
from kivy.uix.floatlayout import FloatLayout

# Main window class
class MainWindow(Widget):
    image_src = StringProperty('pics/background_640x480.jpg')
    
    def btn_settings(self):
        print('Settings')
        show_SettingsPopup()
        
    def btn_help(self):
        print('Help')
        show_HelpPopup()

    def btn_credits(self):
        print('Credits')
        show_CreditsPopup()
        
# Popup Windows (Settings, Help, Credit)    
class SettingsPopup(FloatLayout):
    pass

class HelpPopup(FloatLayout):
    pass

class CreditsPopup(FloatLayout):
    pass

# Main App class        
class DeepMusic(App):
    def build(self):
        layout = MainWindow()
        '''
        Refresh displayed picture:
        # layout.image_src = 'pics/do.png'
        '''            
        return layout

# Popup window functions (Settings, Help, Credit)
def show_SettingsPopup():
    show = SettingsPopup()
    popupWindow = Popup(title="Settings", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

def show_HelpPopup():
    show = HelpPopup()
    popupWindow = Popup(title="Help", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()
    
def show_CreditsPopup():
    show = CreditsPopup()
    popupWindow = Popup(title="Credits", content=show, size_hint=(None, None), size=(500,500))
    popupWindow.open()

# If this file is the main file launch the application  
if __name__ == "__main__":
    DeepMusic().run()
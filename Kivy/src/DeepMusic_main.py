import kivy
import GlobalShared
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty # ID reference
from kivy.graphics import Color, Rectangle # Background color
from kivy.uix.image import Image   
from kivy.uix.popup import Popup     
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout  
from kivy.uix.spinner import Spinner

class SmoothButton(Button):
    btn_text_color   = StringProperty(GlobalShared.BTN_TEXT_COLOR)
    btn_normal       = ObjectProperty(GlobalShared.BTN_COLOR_NORMAL)

# Popup Windows (Settings, Help, Credit)    
class SettingsPopup(FloatLayout):
    text_color = StringProperty(GlobalShared.TEXT_COLOR)
    
    # Callback for the checkbox 
    def checkbox_Predict(self, instance, value): 
        if value is True: 
            print("Prediction enabled") 
        else: 
            print("Prediction disabled") 
            
    def checkbox_Tune(self, instance, value): 
        if value is True: 
            print("Tune help enabled") 
        else: 
            print("Tune help disabled")
            
    def checkbox_Rythm(self, instance, value): 
        if value is True: 
            print("Rythm help enabled") 
        else: 
            print("Rythm help disabled") 
            
    def slider_Volume(self, instance, value):
        print('Volume', value)
    
    def spinner_Instrument(self, value):
        print('instrument', self.value)
        
    def btn_SettingsApply(self):
        GlobalShared.POPUP_WINDOW.dismiss()


class HelpPopup(FloatLayout):
    text_color = StringProperty(GlobalShared.TEXT_COLOR)
    
    def btn_HelpBack(self):
        GlobalShared.POPUP_WINDOW.dismiss()

class CreditsPopup(FloatLayout):
    text_color = StringProperty(GlobalShared.TEXT_COLOR)
    
    def btn_CreditBack(self):
        GlobalShared.POPUP_WINDOW.dismiss()


# Main window class
class MainWindow(Widget):
    image_src = StringProperty('pics/background_640x480.jpg')
    background_color = StringProperty(GlobalShared.BACKGROUND_COLOR)
    text_color = StringProperty(GlobalShared.TEXT_COLOR)
    btn_text_color = StringProperty(GlobalShared.BTN_TEXT_COLOR)
    
    def btn_settings(self):
        show = SettingsPopup()
        GlobalShared.POPUP_WINDOW = Popup(title="Settings", title_color=GlobalShared.TEXT_COLOR, content=show, size_hint=(None, None), size=(500,400))
        GlobalShared.POPUP_WINDOW.open()
        
    def btn_help(self):
        show = HelpPopup()
        GlobalShared.POPUP_WINDOW = Popup(title="Help", title_color=GlobalShared.TEXT_COLOR, content=show, size_hint=(None, None), size=(750,420))
        GlobalShared.POPUP_WINDOW.open()

    def btn_credits(self):
        show = CreditsPopup()
        GlobalShared.POPUP_WINDOW = Popup(title="Credits", title_color=GlobalShared.TEXT_COLOR, content=show, size_hint=(None, None), size=(500,500))
        GlobalShared.POPUP_WINDOW.open()
    
# Main App class        
class DeepMusic(App):
    def build(self):
        layout = MainWindow()
        
        '''
        Refresh displayed picture example:
        # layout.image_src = 'pics/do.png'
        '''            
        
        return layout


# If this file is the main file launch the application  
if __name__ == "__main__":
    DeepMusic().run()
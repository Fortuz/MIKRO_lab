import kivy
from kivy.app              import App
from kivy.uix.label        import Label
from kivy.uix.button       import Button
from kivy.uix.widget       import Widget
from kivy.graphics         import Color, Rectangle
from kivy.uix.image        import Image   
from kivy.uix.popup        import Popup     
from kivy.uix.floatlayout  import FloatLayout
from kivy.uix.boxlayout    import BoxLayout  
from kivy.uix.spinner      import Spinner
from kivy.uix.anchorlayout import AnchorLayout

class SmoothButton(Button):
    pass

# Popup Windows (Settings, Help, Credit)    
class SettingsPopup(Popup):        
    def btn_SettingsApply(self):
        self.dismiss()


class HelpPopup(Popup):        
    def btn_HelpBack(self):
        self.dismiss()
        
class CreditsPopup(Popup):
    def btn_CreditBack(self):
        self.dismiss()

# Main window class
class MainWindow(Widget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.settings_window = SettingsPopup()
        self.help_window     = HelpPopup()
        self.credits_window  = CreditsPopup()
        
    def btn_settings(self):
        self.settings_window.open()
        
    def btn_help(self):
        self.help_window.open()
        
    def btn_credits(self):
        self.credits_window.open()
        
# Main App class        
class DeepMusic(App):
    def build(self):
        # Design coloring
        self.background_color = (1, 1, 1, .2)
        self.text_color       = (1, 1, 1, 1)
        # Buttons
        self.btn_text_color   = (1, 1, 1, 1)
        self.btn_color_normal = (0.157, 0.455, 0.753, 0.5)
        self.btn_color_down   = (0.2, 0.5, 0.8, 0.5)
        self.back_color_normal= (0.753, 0.753, 0.753, 0.5)
        self.back_color_down  = (0.753, 0.753, 0.753, 0.2)
        # Check button
        self.cb_color         = (0.294, 0.761, 0.623)
        
        self.back_color_n_blue= (0.157, 0.455, 0.753, 0.5)
        self.back_color_d_blue= (0.157, 0.455, 0.753, 0.2)
    
        # Read kottak.txt and populate songs, tunes and rythm
        file = open('../src/conf/kottak.txt', mode = 'r', encoding = 'utf-8-sig')
        lines=file.read().splitlines() 
        file.close()
        
        self.songs = []
        self.tunes = {}
        self.rythm = {}

        for i in range(len(lines)):
            if lines[i] == str("--Title--"):
                self.songs.append(lines[i+1])
                self.tunes[lines[i+1]] = lines[i+3].split()
                self.rythm[lines[i+1]] = lines[i+5].split()
        
        # Default image for camera
        self.image_src = 'pics/background_640x480.jpg'
        self.layout = MainWindow()    
             
        return self.layout
    
    def displayUpdate(self, picture_ref):
        self.layout.image_src = picture_ref
        
    # Callback functions for the elements of settings window 
    def checkbox_Predict(self, instance, value): 
        if value is True: 
            print("Prediction enabled") 
        else: 
            print("Prediction disabled") 
            
    def checkbox_Tune(self, instance, value): 
        if value is True: 
            print("Tune help enabled")
            self.layout.tune_enable = (1, 1, 1, 1)
        else:
            print("Tune help disabled")
            self.layout.tune_enable = (1, 1, 1, 0)
            
    def checkbox_Rythm(self, instance, value): 
        if value is True: 
            print("Rythm help enabled") 
            self.layout.rythm_enable = (1, 1, 1, 1)
        else: 
            print("Rythm help disabled") 
            self.layout.rythm_enable = (1, 1, 1, 0)
            
    def slider_Volume(self, instance, value):
        print('Volume', value)
    
    def spinner_Instrument(self, text):
        print('Instrument: ', text)
            
    def spinner_Language(self, text):
        print('Language: ', text)
        
    def spinner_Song(self, text):
        print('Song: ', text)
            
# If this file is the main file launch the application  
if __name__ == "__main__":
    DeepMusic().run()
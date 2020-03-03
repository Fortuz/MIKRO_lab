import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty # ID reference
from kivy.graphics import Color, Rectangle # Background color
from kivy.uix.image import Image   
from kivy.properties import StringProperty        


class MainWindow(Widget):
    image_src = StringProperty('pics/background_640x480.jpg')
    pass

class DeepMusic(App):
    def build(self):
        layout = MainWindow()
        
        '''
        Refresh displayed picture:
        # layout.image_src = 'pics/do.png'
        '''
            
        return layout
    
if __name__ == "__main__":
    DeepMusic().run()
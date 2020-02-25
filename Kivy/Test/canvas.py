from kivy.app import App

from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

kvWidget = """

MyWidget:

    orientation: 'vertical'
    
    canvas:    
        
        Color:
        
            rgb: (1, 0, 0)
            
        Rectangle:
        
            size: self.size
            
            pos: self.pos
            
            source: '../src/pics/la.png'
            
"""

class MyWidget(BoxLayout):

    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)

class CanvasApp(App):

    def build(self):
        
        return Builder.load_string(kvWidget)

CanvasApp().run()

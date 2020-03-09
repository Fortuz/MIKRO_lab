# main.py to manipulate the window  
# color or screen clour in kivy 
  
# base Class of your App inherits from the App class.   
# app:always refers to the instance of your application   
from kivy.app import App 
  
# BoxLayout arranges children in a vertical or horizontal box.  
# or help to put the childrens at the desired location.  
from kivy.uix.boxlayout import BoxLayout  
  
# creating the root widget used in .kv file  
class MultipleSliderWidget(BoxLayout): 
    pass
  
# class in which name .kv file must be named Slider.kv. 
# or creating the App class 
class SliderControl(App): 
    def build(self): 
        # returning the instance of SliderWidget class  
        return MultipleSliderWidget() 
  
# run the app     
if __name__ == '__main__': 
    SliderControl().run() 
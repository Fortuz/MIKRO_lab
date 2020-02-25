class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("Hi I am", self.name, 'and I am ', self.age, 'yeras old.')
    
    def talk(self):
        print("Bark!")
"""    
class Cat(object):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        
    def speak(self):
        print("Hi I am", self.name, 'and I am ', self.age, 'yeras old.')
"""

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def talk(self):
        print('Meow!')
        
tim = Cat('tim',5,'blue')
tim.speak()
tim.talk()
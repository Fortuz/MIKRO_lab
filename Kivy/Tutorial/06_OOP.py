class Dog:
    dogs = []
    x = 0
    
    
    def __init__(self, name):
        self.name = name
        self.dogs.append(self)
        
    @classmethod    
    def num_dogs(cls):
        return len(cls.dogs)
   
    @classmethod
    def value(cls, p):
        cls.x = p
    
    @staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")
            
tim = Dog("Tim")
print(len(tim.dogs)) # Dog.dogs = 1
print(tim.x)         # tim.x = 0
print(Dog.x)         # Dog.x = 0

tim.value(5) 
Dog.value(3)   
print(tim.x)         # tim.x = 5
print(Dog.x)         # Dog.x = 0

jim = Dog("Jim")     
print(len(jim.dogs)) # Dog.dogs = 2
print(jim.x)         # jim.x = 0
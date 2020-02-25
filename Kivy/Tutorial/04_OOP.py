class Vehicle():
    def __init__(self):
        self.price = 0
        self.gas = 0
        self.color = 0
    
    def fillUpTank(self):
        self.gas = 100
        
    def emptyTank(self):
        self.gas = 0
        
    def gasLeft(self):
        return self.gas
    

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.speed = 50
        
    def beep(self):
        print('Beep beep')
        
        
class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.tries = 6
        
    def beep(self):
        print('Honk honk')
        
truck = Truck()

print(truck.gasLeft())

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass
    def maintenance(self):
        pass
    def value(self):
        pass
    
    
class FourWheeler(Vehicle):
    def speed(self):
        print('>> speed FourWheeler')
        
    def maintenance(self):
        print(">> maintenance FourWheeler")
        
    def value(self):
        print(">> value FourWheeler")
        
class TwoWheeler(Vehicle):
    def speed(self):
        print('>> speed TwoWheeler')
        
    def maintenance(self):
        print(">> maintenance TwoWheeler")
        
    def value(self):
        print(">> value TwoWheeler")
        
class Airborne(Vehicle):
    def speed(self):
        print('>> speed Airborne')
        
    def maintenance(self):
        print(">> maintenance Airborne")
        
    def value(self):
        print(">> value Airborne")
        
four = FourWheeler()
two  = TwoWheeler()
air = Airborne()

l = [four, two, air]
for method in l:
    method.speed()
    method.maintenance()
    method.value()
    print("\n")
 
va = Vehicle()
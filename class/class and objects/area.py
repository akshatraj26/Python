import math
class Solid:
     
    def __init__(self, r):
        self.__r = r
        
    def surface_area(self):
        
        return 3 * math.pi * self.__r ** 2
    
    def volume(self):
        return (4 * math.pi * self.__r ** 3) / 3
    
obj = Solid(3)
print(obj.surface_area())
print(obj.volume())
import math
class RegularShape:
    def __init__(self, name):
        self.name = name
    
    def perimeter(self):
        pass
    def area(self):
        pass
    
class Square(RegularShape):
    def __init__(self, length):
        super().__init__('square')
        self.length = length
    
    def perimeter(self):
        return 4 * self.length
    def area(self):
        return self.length ** 2
    
class Circle(RegularShape):
    def __init__(self, radius):
        super().__init__('circle')
        self.radius = radius
    
    def perimeter(self):
        return 2* math.pi *  self.radius
    def area(self):
        return math.pi * self.radius ** 2
    
c = Circle(3)
print(c.area())
print(c.perimeter())
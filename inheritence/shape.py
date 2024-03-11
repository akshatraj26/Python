
class Shape():
    
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("In Rectangle.draw")
    
    
class Circle(Shape):
    def draw(self):
        print("In Circle.show")
        
s = Shape()
c = Circle()
r = Rectangle()

print(isinstance(s, Shape))
print(isinstance(s, Circle))
print(isinstance(s, Rectangle))
print(issubclass(Circle, Shape))
print(issubclass(Rectangle, Shape))
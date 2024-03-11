class Base:
    def display(self):
        print("In Base")
        
### Heirarichal            
class Derived1(Base):
    def display(self):
        print("In Derived1")
        
class Derived2(Base):
    def display(self):
        print("In Derived2")
    
# Multiple Inheritence    
class Der(Derived1, Derived2):
    def display(self):
        super().display()
        Derived1.display(self)
        Derived2.display(self)
        print(Der.__mro__)
        
d1 = Der()
d1.display()
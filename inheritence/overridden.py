class Base:
    def __method(self):
        print("In Base__method")
        
    def func(self):
        self.__method()
        
class Derived(Base):
    def __method(self):
        print("In Derived__method")
        
b  = Base()
b.func()
d = Derived()
d.func()
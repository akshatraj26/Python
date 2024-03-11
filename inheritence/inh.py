class Base:
    def __init__(self):
        self.i = 10
        self._a = 3.14
        self.__s = 'Hello'
        
    def display(self):
        print(self.i, self._a, self.__s)
        
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.i =100
        self._a = 31.44
        self.__s = 'Good Evening'
        self.j = 20
        self._b = 34
        self.__ss = 'JI'
        
    def display(self):
        super().display()
        print(self.i, self._a, self.__s)
        print(self.j, self._b, self.__ss)
        
        
print("Base Class \n")
bobj = Base()
bobj.display()
print(bobj.i)
print(bobj._a)


print("Derived Class")
dobj = Derived()
dobj.display()
print(dobj.j)
print(dobj._b)
# print(dobj.__ss, bobj.__s)

print(dir(object))
print(dir(Base))
print(dir(Derived))

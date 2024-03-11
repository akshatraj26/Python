# Super class, Base Class, Parent Class
class Index:
    def __init__(self):
        self._count = 0
        
    def display(self):
        print("count= " + str(self._count))
        
    def incr(self):
        self._count += 1
        
# Child, Derived and Sub Class

class NewIndex(Index):
    def __init__(self):
        super().__init__()
        
    def decr(self):
        self._count -= 1
        
i = NewIndex()
i.incr()
i.incr()
i.incr()
i.incr()
i.display()
i.decr()
i.display()
i.decr()
i.display()
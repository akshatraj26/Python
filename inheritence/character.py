from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def patriotism(self):
        pass
    
class Actor:
    def style(self):
        print("Actor style class")
        
class Person(Character, Actor):
    def patriotism(self):
        print("Patriotism method from Person Class")
        
    def style(self):
        
        Actor().__init__()
        print("style from person class")
        
        
    def do_acting(self):
        print("Acting class")
        
p = Person()
p.patriotism()
p.style()
p.do_acting()

    
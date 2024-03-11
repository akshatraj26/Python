from abc import ABC, abstractmethod

class Printer(ABC):
    def __init__(self, n):
        self.n = n
    @abstractmethod    
    def print(self, docName):
        pass

class LaserPrinter(Printer):
    def __init__(self, n):
        super().__init__(n)
        
    def print(self, docName):
        print(">> LaserPrinter.print")
        print("LaserPrinter Filename:- ", docName)
           
class InkjetPrinter(Printer):
    def __init__(self, n):
        super().__init__(n)
        
    def print(self, docName):
        print(">> InkjetPrinter.print")
        print("InkjetPrinter Filename:", docName)
        
l = LaserPrinter("Laserjet 1100")
i = InkjetPrinter("IBM 200")

l.print("file.pdf")
i.print("hello.py")
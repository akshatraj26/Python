class Adding:
    def __init__(self, string):
        self.__str = string
        
    def __add__(self, other):
        return f"{self.__str} {other.__str}"
    
a = Adding('Hi')
b =Adding('Hello')
print(a +b )
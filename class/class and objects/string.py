class String:
    def __init__(self, s):
        self.__str = s
        
    def __iadd__(self, other):
        self.__str = self.__str + " " + other.__str
        return self.__str
    
    def toUpper(self):
        return self.__str.upper()
    def toLower(self):
        return self.__str.lower()
    
s = String("Hello")

s += String('Fire')
print(s)

print(String('Hello').toLower())
print(String("hihow").toUpper())

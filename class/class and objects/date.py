class Date:
    def __init__(self, d, m, y):
        self.__day, self.__mth, self.__yr = d, m, y
        
    def __eq__(self, other):
        if self.__day == other.__day & self.__mth == other.__mth & self.__yr == other.__yr:
            return True
        else:
            return False
            
            
            
d1 = Date(12, 3, 2024)
d2 = Date(12, 3, 2024)
d3 = Date(11, 12, 2011)
print(id(d1))
print(id(d2))
print(d1 == d3)
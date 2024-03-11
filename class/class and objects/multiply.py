class Multiply:
    def __init__(self, r, i):
        self.__real =  r
        self.__imag = i
    def __str__(self):
        return f"{self.__real} + {self.__imag} i"
    
    def __mul__(self, other):
        return f"{round(self.__real * other.__real, 2)} + {round(self.__imag * other.__imag, 4)} i"
    
    
    
c1 = Multiply(1.1, 0.2)
c2 = Multiply(1.1 , 0.2)

print(c1 * c2)
# Write a program to create a class that represents Complex numbers containing real number and imaginary parts and the use it to perform complex number addition, substraction, multiplication and division.

class ComplexNumber:
    def __init__(self, real, imag):
        self.__real = real
        self.__imag = imag
        
    def show(self):
        return f"{self.__real} + {self.__imag} i"
    
    def __add__(self, other):
        return  f"{self.__real + other.__real} + {self.__imag + other.__imag} i"
    
    def __sub__(self, other):
        r = self.__real + other.__real
        i = self.__imag + other.__imag
        return  f"{self.__real - other.__real} + {round(self.__imag - other.__imag, 4)} i"
    
    def __mul__(self, other):
        return  f"{self.__real * other.__real} + {round(self.__imag * other.__imag, 4)}  i"
    
    def __truediv__(self, other):
        return  f"{self.__real / other.__real} + {round(self.__imag / other.__imag, 4)} i"
    
# a = ComplexNumber(3, 0.4)
# b = ComplexNumber(4, 0.2)
# print(a+b)
# print(a -b)
# print(a*b)
# print(a/b)    

n = [[2,3,4], [4, 6, 7]]
print(type(n)) 
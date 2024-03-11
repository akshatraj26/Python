class Complex:
    def __init__(self, r = 0.0, i = 0.0):
        self.__real = r
        self.__imag = i
    
    def __eq__(self, other):
        if self.__real == other.__real and self.__imag == other.__imag:
            return True
        else:
            False
            
            
c1 = Complex(1.2, 2.5)
c2 = Complex(4.2, 3.3)
c3 = c1
if c1 == c2:
    print("Attributes of c1 and c2 are same")
else:
    print("Attributes of c1 and c2 are different")
    
if type(c1) == type(c3):
    print("c1 and c3 are the same type.")
    
else:
    print("c1 and c3 are of different type")
    
if c1 is c3:
    print("c1 and c3 are pointing to same object")
else:
    print("c1 and c3 are pointing to different objects")
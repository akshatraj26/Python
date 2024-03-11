class B:
    def b1(self):
        print(">> B b1()")
        print("I am b1 function from D any one can access me")
        
    def __b2(self):
       print("Can't access me I am private method") 
       
class D(B):
    def d1(self):
        print(" I am from a B class d1() function")
    def d2(self):
        print(" I am from a B class d2() function")
        
b = B()
b.b1()

b.b2()  # throw an error
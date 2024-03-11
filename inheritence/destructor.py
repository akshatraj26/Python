class B1:
    def __init__(self):
        print("Constructor B1 called")
        
    def __del__(self):
        print("Destructor of B1 is called")
        
class B2:
    def __init__(self):
        print("Constructor of B2 called")
        
    def __del__(self):
        print("Destructor of B2 is called")
        
class D(B1, B2):
    def __init__(self):
        B2.__init__(self)
        print("Constructor D is called")
        
    def __del__(self):
        print("Destructor of D called")
        super(D, self).__del__()

d = D()
del d
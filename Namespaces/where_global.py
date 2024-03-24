a = 20
b = 3.14
s = 'Aabra ka kadabra'
lst = ['a', 'b', 's']
for var in lst:
    print(globals()[var])


def fun1():
    print("Fun1")

def fun2():
    print("Fun2")

def fun3():
    print("Fun3")

def fun4():
    print("Fun4")

lst = ['fun1', 'fun2', 'fun3', 'fun4']
for var in lst:
    globals()[var]()
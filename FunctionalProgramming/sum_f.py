def sum(x, y, f):
    print(x+y)
    f()

def func():
    print("Hello World")
    
f = func

sum(45, 67, f)
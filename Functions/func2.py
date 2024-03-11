def fun1():
    print("Reached func1")
    def func2():
        print("Inner Avatar")
    print("Outer avatar")
    func2()

# fun1()
# fun2() # Throw an error
print(type(fun1()))
a = fun1()
print(a)
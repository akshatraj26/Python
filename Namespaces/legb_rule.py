def fun1():
    y = 20
    print(x, y)
    print(len(str(x)))

    def fun2():
        z =30
        print(x, y, z)
        print(len(str(x)))

    fun2()

x = 100
print("Global x:- ")
print(len(str(x)))
fun1()
def fun1():
    a = 45
    print(a)
    print(id(a))

    def fun2():
        a ='Jhi'
        print(a)
        print(id(a))
    fun2()

fun1()
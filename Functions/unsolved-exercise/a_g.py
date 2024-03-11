def fun(a, *args, s = '!'):
    print(a, s)
    for i in args:
        print(i, s)
    print()


fun(10)
fun(10, 20)
fun(10 ,20, 30)
fun(10, 20, 30, 40, s ='+')
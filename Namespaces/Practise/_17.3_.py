def fun():
    a =10
    b =20
    c =30

    locals()['a'] = 25
    locals()['c'] = 234
    locals()['b'] = 5467
    print(a, b, c)

    def fun():
        a = 50
        b =343
        print(a, b,c)
    fun()

fun()


a = 20
b =40
print(globals())
print(locals())
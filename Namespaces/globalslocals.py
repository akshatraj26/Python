def fun():
    # name conflict. local a shadows out global a
    a = 45
    global b
    b = 6.89
    c = '239283'
    d = 4 + 4j
    print(locals())
    print(globals())


# global identifiers
a = 20
b = 3.14
s = 'Aabra ka kadabra'
print(locals())
print(globals())
fun()

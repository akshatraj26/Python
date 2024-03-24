def fun():
    # name conflict. local a shadows out global a
    a = 45

    # name conflict. use global b
    global  b
    b = 6.89
    print(a, b, s)


# global identifiers
a = 20
b = 3.14
s = 'Aabra ka kadabra'
fun()
print(a, b, s) # b has changed but a and s are unchanged

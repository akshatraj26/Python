dct1 = {
    'A101': {'Type': 'Dog', 'Name': 'Tommy', 'Age':3},
    'B102': {'Type': "Cat", 'Name': 'Sheru', 'Age': 12},
    'C103': {'Type': "Cat", 'Name': 'Kranti', 'Age': 8},
    "D104": {'Type': "Dog", 'Name': 'doggy', 'Age': 6},
}


def fun1(d):
    if d['Type'] == 'Dog':
        return d['Age']
    else:
        return 0


def fun2(n):
    if n==0:
        return False
    else:
        return True


res = list(filter(fun2, list(map(fun1, list(dct1.values())))))
print(res)


print("The Sum of all dogs ages are:-", sum(res))
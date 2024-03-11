def print_it(i, j, *args, x, y, **kwargs):
    print()
    print(i, j, end=' ')
    for var in args:
        print(var, end=' ')
    print(x, y, end=' ')
    for name, value in kwargs.items():
        print(name, ':', value)

print_it(34, 456, x =78, y = 'joj')
print_it(10, 20, 100, 200, x = 45, y =34)
print_it(10, 20, 100, 200, x = 45, y =34)
print_it(10, 20, 100, 200, y =45, x =56, a =5, b=6, c=7)
print_it(10, 20, 30, 40)
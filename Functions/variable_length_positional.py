def print_it(*args):
    print(type(args))
    for var in args:
        print(var)
print_it(344, 'Silicon', 23.4656)
print()
print_it(10)
print()
print_it(10, 3.14)
print()
print_it(10, 3.14, 'Akshat', 'Amogsidh')
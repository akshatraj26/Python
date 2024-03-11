def print_it(**kwargs):
    print()
    for name, value in kwargs.items():
        print(name, value, end='')


print_it(a =10)
print_it(a =10, name = 'Akshat')
print_it(a =10, b =3.14, s = 'Silicon')
dct = {'Student': 'Amogsidh', ' age':2434}
print_it(**dct)

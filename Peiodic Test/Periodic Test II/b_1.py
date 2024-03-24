
# a, b, c, d = [int(n) for n in input("Enter four values:-").split()]
# print(a, b, c, d)
import random
print([random.randrange(10, 100) for n in range(20)])

a = [[n** 2, n**3] for n in range(5, 11)]
print(a)

even = {n for n in range(10, 30) if n % 2 ==0}
print(even)

lst = [10, 3, 4, 5, 15, 20, 21, 23, 46, 50]
print([n for n in lst if n < 20 or n > 50])

d = {'AMOL': 20, 'ANIL': 12, 'SUNIL': 13, 'RAMESH': 10}
print({key: val**2 for key, val in d.items()})

def	print_it(a,	b,	c,	d,	e):
    print(a,	b,	c,	d,	e)

tpl	=('A',	'B',	'C',	'D',	'E')
print_it(*tpl)



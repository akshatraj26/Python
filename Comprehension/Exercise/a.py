import random

# a_a generate all quadrant between (1, 1) to (5, 5)
coordinates = [(i, j) for i in range(1, 6) for j in range(1, 6)]
print(coordinates)

# a_b multiply each element by 10
a = [i * 10 for i in range(10)]
print(a)

# a_c first 20 fabonacii
lst = [0, 1]
[lst.append(lst[k - 1] + lst[k - 2]) for k in range(2, 20)]
print(lst)

# a_d first 20 even and odd
even = [n for n in range(40) if n % 2 == 0]
odd = [n for n in range(40) if n % 2 != 0]
print(even, odd)

# a_e list containing positive and negative
lis = [n for n in range(-20, 20)]
print(lis)

pos = [n for n in lis if n > 0]
neg = [n for n in lis if n < 0]
print(pos)

print(neg)

# a_f
lst = ['hsdghs', 'sjgfjs', 'nhkjde']
uppe = [n.upper() for n in lst]
print(uppe)


#  a_g convert celcius to farenhite

celcius = [35, 34, 50, 54, 20, 0]
# f = ((9/5) * cel) +32

farenhite = [(((9 / 5) * cel) + 32) for cel in celcius]
temperature = {cel: far for cel, far in zip(celcius, farenhite)}
print(temperature)

# f_h generate 2d matrix of size 4 x 5 containing random multiples of 4 in the range of 40 to 160.

rows, cols = 4, 5
matrix = [[(4 * random.randint(10, 40)) for r in range(cols)] for j in range(rows)]
print(matrix)

# f_j convert words presents into a list into uppercase and stores in a list
text = ['akjkjs', 'amog', 'sidh', 'rishi', 'mobile']
upper_text = set([s.upper() for s in text])
print(upper_text)


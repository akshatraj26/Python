import math

d = {'Oil': 230, 'Clip': 150, 'Stud': 175, 'Nut': 35}

# lambda takes a dictionary item and returns a value
d1 = sorted(d.items(), key=lambda kv: kv[1])
print(d1)

e = [1, 2, 3, 4, 5, 6, 7]
print(list(map((lambda x: x*x*x), e)))


def fun(n):
    return n * n

e = [1, 2, 3, 4, 5, 6, 7]
m1 = map(math.radians, e)
m2 = map(math.factorial, e)
m3 = map(fun, e)
print(list(m1))
print(list(m2))
print(list(m3))

lis = ['akshat', 'hin', ' pritesh', 'kjjds', 'jgsjd']
print(list(map(lambda x : x.upper(), lis)))


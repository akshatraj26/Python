lst1 = [5, 10, 15,2, 20, 25, 30, 43]
m = map(lambda x:x*x, lst1)
print(list(m))


# use filter
f = filter(lambda x: x%5==0, lst1)
print(list(f))

# use reduce
from functools import reduce
r = reduce(lambda x,y: x+y, lst1)
print(r)


p = reduce(lambda x,y:x*y, lst1)
print(p)


# map, reduce and filter can be used together
def fun(n):
    return n>1000

lst = [10, 20, 30, 40, 50]
l = filter(fun, map(lambda x: x*x, lst))
print(list(l))

#

# reduce(max, map(get_salary, filter(lambda x:x.grade() == 'Skilled', employees)))
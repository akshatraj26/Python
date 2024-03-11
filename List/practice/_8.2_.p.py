odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
a = odd + even
print(a)

d = [11, 17, 19] + a
print(d)
print(len(d))

d[-3:] = [100, 200, 300]
print(d)

d[:] = []
print(d)

del d
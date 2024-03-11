print((lambda n: n*n*n)(3))

print((lambda x, y, z: (x+y+z)/3)(4,56,6))

print((lambda s: s.strip().upper())('        akshat   '))


p = lambda n : n* n* n
q = lambda x, y, z : (x+y+z)/3
r = lambda s: s.strip().upper()

print(p(3))
print(q(2, 4,5))
print(r('  jhjdhf  mndhjbu mbbu   '))


# container types
lst1 = [1,2, 3, 4, 5,6, 7]
lst2 = [10, 20, 30, 40, 50]
print((lambda l:sum(l)/len(l))(lst1))
print(sum(lst1)/len(lst1))

print((lambda l:sum(l)/len(l))(lst2))



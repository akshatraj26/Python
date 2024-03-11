words = ['A', 'Amog', 'Akshat', 'Raj', 'Mallinath']
numbers = [12, 29, 23, 24, 54]
z = zip(words, numbers)
print(z)

print(list(z))
z = zip(words, numbers)
print(set(z))
z = zip(words, numbers)
print(tuple(z))


z = zip(words, numbers)

lst = list(z)
w, n = zip(*lst)
print()
print(w)
print(n)


print()
for ch in 'AmogSidh Malinath Desmukh':
    print(ch)

print()
for i in [12, 23, 45, 6, 78, 123]:
    print(i)
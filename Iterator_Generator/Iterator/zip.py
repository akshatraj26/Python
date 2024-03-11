words = ['A', 'Amog', 'Akshat', 'Raj', 'Mallinath']
numbers = [12, 29, 23, 24, 54]
z = zip(words, numbers)
print(z)


for i in z:
    print(*i)

print()
for i in z:
    print(i[0], i[1])
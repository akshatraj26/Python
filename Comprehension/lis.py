import random

print([random.randint(0, 100) for i in range(20)])

# square and cube between 0 to 10
print([(x**2, x**3) for x in range(1, 10)])

# convert list of string to integer
print([int(x) for x in ['12', '45', '56', '67', '23']])

# list of even number between 10 ,30
a = [x for x in range(20, 50) if x%2 ==0]
print(a)
a = [x for x in range(100)]
f = [x for x in a if x < 20 or x> 50]
print(f)

# replace vowel ! in a string
a = ['!' if alphabet in 'aeiou' else alphabet for alphabet in 'AmogsidhDeshmukh']
print(a)


# flatten a list of lists
arr = [[1,2,3], [4,5,6], [7,8,9, 11, 12]]
print([a for ele in arr for a in ele])

# another way
print([*arr[0], *arr[1], *arr[2]])


print([a+b for a in [1,2,3] for b in [3, 4, 5]])

# produces [[4,5,6], [5,6,7], [6,7,8]]
print([[a+b for a in [1,2,3]] for b in [3,4,5]])

# produces every possible sce

print([(i, j, k) for i in [1,2,3] for j in [1,2,3] for k in [1,2,3] if i!=j and j != k and i!=k])
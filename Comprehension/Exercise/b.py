# c_a

# s = set([int(n) for n in input("Enter values:").split()])
# # 1 2 3 4 5 6 7 2 4 5 0
# print(s)


print([n for n in range(10, 30) if n % 2 == 0])

print({n for n in range(10, 30) if n % 2 == 0})

a = [a + b for a in ['They ', 'We '] for b in ['are gone!', 'have come!']]
print(a)

# c_e
sent = "Pack my box with five dozen liquor jugs"
print(set(sent.split()))

# c_g
dic1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print({key: ele * 100 for key, ele in dic1.items()})

# c_h
lst = [2, 7, 8, 6, 5, 5, 4, 4, 8]
s = {True if n%2==0 else False for n in lst}
print(s)

# c_i
a = {'amol':400, 'anil':144, 'sunil':13, 'ramesh':10}

print({k.upper(): v for k, v in a.items()})

# c_j
lst = ['Amol', 'Ramesh', 'Vinay', 'Rahul', 'Sandeep']
print({i.upper() for i in lst})
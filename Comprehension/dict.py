import random

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# value cubed
d1 = {k: v ** 3 for k, v in d.items()}
print(d1)

# value > 3

d2 = {k: v ** 3 for k, v in d.items() if v > 3}
print(d2)

# identify odd and even entities in a dict
d3 = {k: ('Even' if v % 2 == 0 else 'Odd') for k, v in d.items()}
print(d3)



#
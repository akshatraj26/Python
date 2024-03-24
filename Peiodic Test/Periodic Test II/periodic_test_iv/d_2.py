lst1 = ['Guava', 'Mango', 'Grape', 'Banana']
lst2 = [150, 200, 15, 180]

dct = {}
for key, val in zip(lst1, lst2):
    dct[key] = val

print(dct)
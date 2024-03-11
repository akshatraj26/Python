lst = [1, 2, 3, -5, 4, 5, -1, -2, -3, -4, -5]

if 0 not in lst:
    lst.append(0)
lst = sorted(lst)
pos = lst.index(0)
print(pos)
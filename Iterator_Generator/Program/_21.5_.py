"""
Write a program to obtain transpose of a 3 x 4 matrix.
"""
mat = [[i for i in range(1, 5)], [i for i in range(5, 9)], [i for i in range(9, 13)]]
print(mat)
ti = zip(*mat)
print(list(ti))
lst = [[] for i in range(4)]
print(lst)
i = 0
ti = zip(*mat)
for t in ti:
    lst[i] = list(t)
    i += 1
print(lst)
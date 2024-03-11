"""
Suppose there are two lists, one containing numbers from 1 to 6 and other containing numbers from 6 to 1.
Write a program to obtain a list that contains element obtained by adding corresponding elements of the two lists.
"""

lis1 = [i for i in range(1,7)]
lis2 = [i for i in range(6, 0, -1)]
result = map(lambda x,y: x+y, lis1, lis2)
print(list(result))
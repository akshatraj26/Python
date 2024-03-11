"""
Write a program to multiply two matrices x(2 x 3) and y(2, 2) using list comprehension.
"""

x = [[1, 2, 3], 4, 5, 6]
y = [[11, 12], [21, 22], [31, 32]]

l1 = [xrow for xrow in x]
print(x)
l2 = [(xrow, ycol) for ycol in zip(*y) for xrow in x]
print(l2)

l3 = [[sum(a * b for a, b in zip(xrow, ycol))
       for ycol in zip(*y)]
      for xrow in x]
print(l3)


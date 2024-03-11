"""
Write a program that proves that list is iterable and not an iterator.
"""

lis = [10, 20, 30, 40, 50, 60]
print(dir(lis))

i = iter(lis)
print(dir(i))

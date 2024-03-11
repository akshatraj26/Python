"""
Suppose a list has 20 numbers. Write a program that removes all duplicates from list.
"""

lst =[1, 1, 1, 1, 1, 2, 2, 2, 3, 1, 4, 1, 3, 2, 1, 1, 2, 2, 5, 5]

unique = []
for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)
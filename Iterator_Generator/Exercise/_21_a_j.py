"""
Write a program to convert a list of tuples.
[(10, 20, 30), (150.55, 145.60, 157.65), ('A1', 'B1', 'C1')]

into another list of tuples
[(10, 150.55, 'A1'), (20, 145.6, 'B1'), (30, 157.65, 'C1')]
"""

lst = [(10, 20, 30), (150.55, 145.60, 157.65), ('A1', 'B1', 'C1')]
lst1 = []
for a, b, c in zip(*lst):
    lst1.append((a, b, c))

print(lst1)
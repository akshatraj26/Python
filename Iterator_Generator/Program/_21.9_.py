"""
Write a dictionary containing names of subjects and marks obtained by them in three subjects. Write a program to print
these names in tabular form with sorted names as columns and marks in three subjects listed below each student name
as below.

Rahul   Rakesh  Sameer
67      59      58
76      70      86
39      81      78
"""

d = {'Rahul': [67, 76, 39],
     'Sameer': [58, 86, 78],
     'Rakesh': [59, 70, 81]}

lst = [(k, *v) for k, v in d.items()]
print(lst)
sort = [(key, *value) for key, value in sorted(d.items())]
print(sort)

for row in zip(*lst):
    print(row)

for row in zip(*lst):
    print(*row, sep='\t')

for row in zip(*sort):
    print(*row, sep='\t')
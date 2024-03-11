"""
A list contains only positive and negative integers. Write a program to obtain the number of negative numbers present in
the list.
"""

lst1 = [-1, -2, -3, -345, 1, 2, 3]

print(len([num for num in lst1 if num<0]))
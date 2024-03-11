"""
Create two lists student and marks. Create  a dictionary from these two lists using dictionary comprehension.
Use name as key and marks as value.
"""

student = ['Amit', 'Ashok', 'Samrat', 'Amog', 'Saket']
marks = [32, 46, 56, 77, 45]

dic1 = {name:mark for name, mark in zip(student, marks)}
print(dic1)
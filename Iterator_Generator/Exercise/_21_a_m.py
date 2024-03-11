"""
Write a program that uses a generator to find out the maximum marks obtained by a student and his name from tuples of
multiple students.
"""
lst = [('Ajay', 45), ('Sujay', 55), ('Nirmal', 40), ('Vijay', 75)]




def get_name(lst):
    mm = max(student[1] for student in lst)
    for i, j in lst:
        if j == mm:
            return i, j

print(get_name(lst))
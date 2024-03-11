"""
Suppose a file contents student's records with each record containing name and age of a student.
Write a program to read these records and display them in sorted order by name .
"""
import operator
f = open('student.txt', 'r')

# f.write('Rishikesh 45\n')
# f.write('Samir 24\n')
# f.write('Navin 34\n')
# f.write('Amit 23\n')
# f.write("Pritesh 23\n")
# f.write("Suresh 25\n")
dct = {}
while True:
    data = f.readline()
    if data == '':
        break
    stud = data.split()
    print(stud)
    dct[stud[0]] = stud[1]
f.close()

for d in sorted(dct):
    print(d, dct[d])


# lst = sorted(dct.items(), key=operator.itemgetter(0))
#
# for item in lst:
#     print(item[0], item[1])






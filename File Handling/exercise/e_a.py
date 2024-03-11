"""
Write a program to read a file and display its content along with line numbers before each line.
"""


f = open('../messages', 'r')

data = f.readlines()
print(type(data))
# print(f.tell(), f.read())

for i, j in enumerate(data):
    print(i+1, j)


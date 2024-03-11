import os

file = os.listdir()
# print(file)


for fil in file:
    if fil.endswith('.log'):
        f = open(fil, mode='r')
        data = f.read()
        print(data)

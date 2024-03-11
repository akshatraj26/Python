import os

lis = os.listdir()
print(lis)

li = []
for file in lis:
    if file.startswith('mylog'):
        li.append(file)

log = []
for f in li:
    fi = open(f, 'r')
    data = fi.read()
    log.append(data)


for n in log:
    print(n)
    print()
    print()

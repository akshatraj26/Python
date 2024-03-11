"""
Write a program that reports the time of creation, time of last access and time of last modification
for a given file.
"""

import os, time

file = 'sampledata'
print(file)

created = os.path.getctime(file)
modified = os.path.getmtime(file)
accessed = os.path.getatime(file)

print("Date Created:" + time.ctime(created))
print("Date Modified:" + time.ctime(modified))
print("Date Accessed:" + time.ctime(accessed))

f = open('hi', 'w')
f.write("Testing")
f.close()

f = open('hi', 'r')
print(f.read())

f = open('hi', 'w')
f.write("Override")
f.close()

f = open('hi', 'r')
print(f.read())


f = open('rad', 'a')
f.write('kjdksdhfkjfhjkf')

f = open('rad', 'rb')
print(f.read())


f = open('mufile', 'wb')



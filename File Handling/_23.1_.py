"""
Write a program to read the contents of the file 'messages' one character at a time.
Print each character that is read.
"""

f = open('messages', 'r')
import time
s = time.time()
while True:
    data = f.read(1)
    if data == '':
        break
    print(data, end='')
e = time.time()

f.close()
print("\n", e-s)
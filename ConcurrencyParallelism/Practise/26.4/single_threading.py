"""
Write a program that reads the contents of 3 files a.txt, b.txt and c.txt sequentially and reports the number
of lines present in it as well as the total reading time. These files should be added to the project and filled with
some text. The program should receive the file names as command-line arguments. Suspend the program for 0.5 seconds
after reading a line from any file.
"""

import time, sys

start = time.time()
lst = sys.argv
print(lst)
lst = lst[1:]

for file in lst:
    f = open(file, 'r')
    count = 0
    while True:
        data = f.readline()
        time.sleep(0.5)
        if data == '':
            break
        count += 1

    print('File:-', file, 'Lines:-', count)

end = time.time()
print('Total reading time:-', end-start, 'sec')
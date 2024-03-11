"""
Write a program that reads the contents of 3 files a.txt, b.txt and c.txt in different threads and reports the number
of lines present in it as well as the total reading time. These files should be added to the project and filled with
some text. The program should receive the file names as command-line arguments. Suspend the program for 0.5 seconds
after reading a line from any file.
"""
import threading
import time, sys


def readfile(inputfile):

    f = open(inputfile, 'r')
    count = 0
    while True:
        data = f.readline()
        time.sleep(0.5)
        if data == '':
            break
        count += 1

    print('File:-', inputfile, 'Lines:-', count)


start = time.time()
lst = sys.argv
print(lst)
lst = lst[1:]

tharr = []
for file in lst:
    th = threading.Thread(target=readfile, args=(file,))
    th.start()
    tharr.append(th)

for th in tharr:
    th.join()

print("Tharr :-", tharr)
end = time.time()
print('Total reading time:-', end-start, 'sec')

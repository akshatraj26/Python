"""
Write a program that accomplishes the same task mentioned in Exercise [B]
(g) above by launching the conversion operations in 3 different threads.

"""

import threading
import sys
import time
import logging


# logging.basicConfig(level=logging.ERROR, filename='error.log',
#                     filemode='w',
#                     format="%(asctime)s - %(levelname)s - %(message)s")


def readfile(inputfile, outputfile):
    f1 = open(inputfile, 'r')
    f2 = open(outputfile, 'w')
    while True:
        data = f1.readline()
        if data == '':
            break
        data = data.upper()
        f2.write(data)
        time.sleep(0.5)


start = time.time()
lst1 = sys.argv[1:4]
lst2 = sys.argv[4:]
print("Lst1:-", lst1)
print("List2:- ", lst2)

if len(lst1) != 3 or len(lst2) != 3:
    print("Improper Usage")
    print("Correct Usage: convert a.txt b.txt c.txt aa.txt bb.txt cc.txt")
    exit()

tharr = []
for i in range(0, 3):
    th = threading.Thread(target=readfile, args=(lst1[i], lst2[i]))
    th.start()
    tharr.append(th)

for th in tharr:
    th.join()


end = time.time()
print("Total Time:- ", end - start, 'seconds.')
# It took 0.014001607894897461 seconds
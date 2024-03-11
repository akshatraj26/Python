"""
Write a program that calculates the squares and cubes of first 6 odd numbers through functions that are executed
in two independent threads. Incorporate a delay of 0.5 seconds after calculation of each square/cube value.
 Report the time required for execution of the program.
"""

import threading
import time


def squares(nos):
    print('Calculating Squares....')
    for n in nos:
        time.sleep(0.5)
        print(f"n:- {n}, Square:- {n * n}\t")


def cube(nos):
    print("Calculating Cubes...")
    for n in nos:
        time.sleep(0.5)
        print(f"n:- {n}, Cube:- {n ** 3}\t")


arr = [1, 3, 5, 7, 9, 11]
start = time.time()
th1 = threading.Thread(target=squares, args=(arr,))
th2 = threading.Thread(target=cube, args=(arr,))

th1.start()
th2.start()
th1.join()
th2.join()
end = time.time()
print("Time required=", end - start, 'sec')

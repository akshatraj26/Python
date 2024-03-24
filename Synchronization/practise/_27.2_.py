"""
Write a program that calculates the squares and cubes of first 6 odd numbers through functions that are executed
in two independent threads. Incorporate a delay of 0.5 seconds after calculation of each square/cube value.
Report the time required for execution of the program. Make sure that output of squares() and cubes() does not get
 mixed up.
"""
import time
import threading


def square(nos, lck):
    lck.acquire()
    print("Calculating Squares......")
    for i in nos:
        time.sleep(0.5)
        print(f"n:- {i}, Square is {i * i}\t")
    lck.release()


def cubes(nos, lck):
    lck.acquire()
    print("Calculating Cubes........")
    for i in nos:
        time.sleep(0.5)
        print(f"n:- {i}, Cube is {i ** 3}\t")
    lck.release()


arr = [i for i in range(13) if i % 2 != 0]

start = time.time()
lck = threading.Lock()
th1 = threading.Thread(target=square, args=(arr, lck))
th2 = threading.Thread(target=cubes, args=(arr, lck))
th1.start()
th2.start()
th1.join()
th2.join()

end = time.time()
print(f"Total Time to run this program:-", end - start)
print(f"Started at a time:- {start}")
print(f"Ended as a time:- {end}")

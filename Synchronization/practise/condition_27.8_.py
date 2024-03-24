"""
Write a program that implements a Producer - Consumer algorithm. The producer thread should generate random numbers in
the range 10 to 20. The consumer should print the square of the random number produced by the producer thread.
"""

import threading
import random
import time
import queue

def producer():
    for i in range(5):
        time.sleep(random.randrange(2, 5))
        cond.acquire()
        num = random.randrange(10, 20)
        print('Generated num:-', num)
        q.append(num)
        cond.notify()
        cond.release()


def consumer():
    for i in range(5):
        cond.acquire()
        while True:
            if len(q):
                num = q.pop()
                break
            cond.wait()
        print('Its square =', num * num)
        print()
        cond.release()


cond = threading.Condition()
q = []
th1 = threading.Thread(target=producer)
th2 = threading.Thread(target=consumer)
th1.start()
th2.start()
th1.join()
th2.join()
print("All Done")
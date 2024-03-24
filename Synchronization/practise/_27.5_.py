"""
Write a program that runs a recursive factorial() function in 2 threads. This function should receive an integer and
print all the intermediate products and final product.
"""

import threading


def factorial(n):
    lck.acquire()
    p = 0
    if n != 0:
        t = threading.current_thread()
        p = n * factorial(n-1)
        print(f"{t.name} :  {n}! = {p}")
    else:
        p = 1
    lck.release()
    return p


lck = threading.RLock()
th1 = threading.Thread(target=factorial, args=(7,))
th1.start()

th2 = threading.Thread(target=factorial, args=(5,))
th2.start()

th1.join()
th2.join()

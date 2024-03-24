"""
Write a program that runs fun1() and fun2() in two different threads. Using an event object, function fun1()
should wait for fun2 to signal it at random intervals that its wait is over. On receiving the signal report
the time and clear the event flag.
"""

import threading
import random
import time

def fun1(ev, n):
    for i in range(n):
        print(i+1, 'Waiting for the flag to be set...')
        ev.wait()
        print("Wait completed at:", time.ctime())
        ev.clear()
        print()


def fun2(ev, n):
    for i in range(n):
        time.sleep(random.randrange(2, 5))
        ev.set()


ev = threading.Event()
th = []
num = random.randrange(4, 8)
th.append(threading.Thread(target=fun1, args=(ev, num)))
th[-1].start()
th.append(threading.Thread(target=fun2, args=(ev, num)))
th[-1].start()
for t in th:
    t.join()

print("All done!!")
print(random.randrange(10, 20))
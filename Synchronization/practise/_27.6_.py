"""
Write a program that defines a function fun() that prints a message that it receives infinite times. Limit the number
of threads that can invoke fun() to 3. if 4th thread tries to invoke fun(), it should not get invoked.
"""

import threading

def fun(msg):
    s.acquire()
    t = threading.current_thread()
    while True:
        print(f"{t.name} : {msg}")
    s.release()


s = threading.BoundedSemaphore(3)
th1 = threading.Thread(target=fun, args=('Hello',))
th2 = threading.Thread(target=fun, args=('Hi',))
th3 = threading.Thread(target=fun, args=('Welcome',))
th4 = threading.Thread(target=fun, args=('Bye',))

th1.start()
th2.start()
th3.start()
th4.start()
th1.join()
th2.join()
th3.join()
th4.join()
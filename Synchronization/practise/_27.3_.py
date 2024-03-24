"""
Write a program that prints the following 3 messages through 3 different threads:
[What is this life...]
[We have no time...]
[To stand and stare]

Each thread should be passed the relevant message and should print '[', message and ']' through three different print()
calls.
"""

import time
import threading

def printMsg(msg, lck):
    lck.acquire()
    print(f"[{msg}]")
    time.sleep(0.5)
    lck.release()


lck = threading.Lock()
th1 = threading.Thread(target=printMsg, args=('What is this life...', lck))
th1.start()

th2 = threading.Thread(target=printMsg, args=('We have no time...', lck))
th2.start()

th3 = threading.Thread(target=printMsg, args=('To stand and stare', lck))
th3.start()

th1.join()
th2.join()
th3.join()
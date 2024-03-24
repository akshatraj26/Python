"""
Write a program that runs a recursive print_num() function in 2 threads. This function should receive an integer and
print all numbers from that number up to 1.
"""
import threading

def print_num(n, rlck):
    rlck.acquire()
    if n != 0:
        t = threading.current_thread()
        print(t.name, ':', n)
        n -= 1
        print_num(n, rlck)
    rlck.release()


rlck = threading.RLock()
th1 = threading.Thread(target=print_num, args=(20, rlck))
th1.start()
th2 = threading.Thread(target=print_num, args=(15, rlck))
th2.start()


th1.join()
th2.join()

import time
import threading

def fun1():
    print("Entering fun1")
    global g
    lck.acquire()
    g += 1
    g -= 1
    lck.release()
    print("In fun1 g= ", g)
    print('Exiting fun1')


def fun2():
    print("Entering fun2")
    global g
    lck.acquire()
    g += 2
    g -= 2
    lck.release()
    print("In fun2 g= ", g)
    print('Exiting fun2')


g = 10
lck = threading.Lock()
th1 = threading.Thread(target=fun1)
th2 = threading.Thread(target=fun2)
th1.start()
th2.start()
th1.join()
th2.join()
"""
Write a program through which you can prove that in this programming situation synchronization is really required
. Then write a program to demonstrate how synchronization can solve the problem.
"""
import threading
import time

def fun1():
    print("Entering fun1")
    global g
    g += 1
    time.sleep(10)
    g -= 1
    print("In fun1 g = ", g)
    print("Exiting fun1")


def fun2():
    print("Entering fun2")
    global g
    g += 2
    g -= 2
    print('In fun2 g= ', g)
    print('Exiting fun2')

g = 10
th1 = threading.Thread(target=fun1)
th2 = threading.Thread(target=fun2)
th1.start()
th2.start()
th1.join()
th2.join()
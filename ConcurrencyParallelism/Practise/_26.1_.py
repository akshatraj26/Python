"""
Write a program that launches three threads, assigns new names to two of them. Suspend each thread for 1 second after
it has been launched.
"""
import threading
import time


def func1():
    t = threading.current_thread()
    print("Starting :", t.name)
    time.sleep(1)
    print("Exiting:-", t.name)
    print()


def func2():
    t = threading.current_thread()
    print("Starting :- ", t.name)
    time.sleep(1)
    print("Exiting:- ", t.name)
    print()


def func3():
    t = threading.current_thread()
    print("Starting :- ", t.name)
    time.sleep(1)
    print("Exiting:- ", t.name)
    print()


t1 = threading.Thread(target=func1)
t2 = threading.Thread(name='Second thread', target=func2)
t3 = threading.Thread(name='Third thread', target=func3)
t1.start()
t2.start()
t3.start()

import threading
def fun1():
    while True:
        # wait for the flag to be set
        ev.wait()
        # once flag is set by thread 2, do the work in this thread
        ev.clear()
        # claer the flag

def fun2():
    while True:
        # perform some work
        # set the flag
        ev.set()

ev = threading.Event()
th1 = threading.Thread(target=fun1)
th2 = threading.Thread(target=fun2)

print(th1, '\n', th2)
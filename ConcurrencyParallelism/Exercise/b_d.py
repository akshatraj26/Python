"""
If Ex class extends the Thread class, then we can launch multiple threads for objects of Ex class? if yes, How?
"""
import threading

class Ex(threading.Thread):
    def __init__(self, s):
        threading.Thread.__init__(self)
        self.msg = s

    def run(self):
        while True:
            print("Message:-", self.msg, '\n')


th1 = Ex('Hello')
th1.start()
th2 = Ex("Akshat")
th2.start()

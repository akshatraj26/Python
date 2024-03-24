import threading

# producer thread
cond = threading.Condition()
cond.acquire()

# code here to produce on item
cond.notify()
cond.release()

# Consumer thread
cond.acquire()
while item_is_not_available():
    cond.wait()
# code here to consume the item
cond.release()
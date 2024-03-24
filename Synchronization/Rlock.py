import threading

rlck = threading.RLock()
rlck.acquire()
rlck.acquire()

rlck.release()
rlck.release()
import threading

lck = threading.Lock()
print(lck)
lck.acquire()
print(lck)
# lck.acquire()
# print("Second lock:-", lck)
lck.release()
print(lck)

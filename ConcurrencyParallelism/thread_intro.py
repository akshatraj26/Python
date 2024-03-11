import threading
# returns the current thread object
t = threading.current_thread()
print("Current Thread: ", t)
# prints the thread name, identifier and status
print("Thread Name:- ", t.name)
print("Thread identifier:- ", t.ident)
print("Is thread is Alive:- ", t.is_alive())
t.name = 'My first thread'
print("After thread name modifications:", t.name)





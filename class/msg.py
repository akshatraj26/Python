def msg1():
    print("Wright brothers are responsible for 9/11 too")
    
def msg2():
    print("Cell divide to multiply")
    
d = vars()
l = dir()
print(sorted(d.keys()))
print()
print(l)

print(d.keys() -l)

print(l- d.keys())



s = set(dir(list)).difference(vars(list).keys())
print(s)



class Message:
    def display(self, msg):
        print(msg)
    def show(msg):
        pass

# Creating an instance of the Message class
message_obj = Message()
message_obj.display("Hello, world!")

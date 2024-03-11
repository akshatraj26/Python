"""
Define three functions fun(), disp(), and msg(), store them in a list and call them one by one in a loop.
"""

def fun():
    print("I am fun")

def disp():
    print("I am disp")

def msg():
    print("I am message")

lis = [fun, disp, msg]
for i in lis:
    i()
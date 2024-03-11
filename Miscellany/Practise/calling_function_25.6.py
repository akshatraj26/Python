"""
Define a decorator that will decorate any function such that it pretends a call with a message indicating that the
function is being called and follows the call with a message indicating that the function has been called.
Also, report the name of the function being called, its arguments and its return value. A simple output is given
below:

Calling sum_num((10 , 20),{})
calling sum_num((10, 20), {}) got return value:30
"""


def calldecorator(func):
    def _decorated(*args, **kwargs):
        print()
        print(f"Calling {func.__name__}({args}, {kwargs})")
        ret = func(*args, **kwargs)
        print(f"Calling {func.__name__}({args},{kwargs}) got return value: {ret}")
        return ret
    return _decorated


@calldecorator
def sum_num(arg1, arg2):
    return arg1 +arg2


@calldecorator
def prod_num(arg1, arg2):
    return arg1 * arg2


@calldecorator
def message(msg):
    pass


sum_num(10, 20)
prod_num(23, 55)
message('Error should never pass silently')


import sys
print(sys.argv[0])
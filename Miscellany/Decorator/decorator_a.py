def my_decorator(func):
    def wrapper():
        print('********************************')
        func()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return wrapper


@my_decorator
def display():
    print("I stand decorated")


@my_decorator
def show():
    print('Nothing great. Me too!')


display()
show()
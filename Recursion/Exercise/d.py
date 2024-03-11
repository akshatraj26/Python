class Pet:
    name = 'Luna'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name}.'


class Dog(Pet):
    name = 'Max'

    def __init__(self, name):
        super().__init__(name)
rex = Dog('Rex')
print(rex.name)
print(Pet.name)
print(Dog.name)


junior = {'python', 'html', 'css', 'git'}
senior = {'python', 'html', 'css', 'django', 'javascript'}
print(senior.intersection(junior))
print(junior.intersection(senior))

print(junior & senior)


code = 'import math; print(math.pi)'
exec(code)


class Container:
    pass


class TemperatureControlledContainer(Container):
    pass


class RefrigeratedContainer(TemperatureControlledContainer):
    pass


for cls in RefrigeratedContainer.__mro__:
    print(cls.__name__)


# def calculate(a):
#     if a == 10:
#         return a
#     else:
#         return calculate(a - 1)
#
#
# print(calculate(8))


stocks = [
    "Apple",
    "Tesla",
    "Amazon",
    "Microsoft",
    "Netflix",
    "Alphabet",
]
tmp = stocks


print()
print(type(stocks), id(stocks))
print(type(tmp), id(tmp))

my_iterable = [True, True, True, False]
all_true = all(my_iterable)
print(all_true)  # Output will be False since not all elements are True


numbers = list(range(5))
numbers.insert(0, 1)
del numbers[3]
print(numbers)


import pandas as pd
print(pd.__path__)


# stream = ['0343', '5-355', '5452', None]
# print(stream.sort())

print(1e6)
print(0.0)
print(.0)
print(0.)


print(
    '''Python is a high-level, interpreted,\ngeneral-purpose '''
    '''programming language.'''
)


print(3 * True)
print(False * 2)
print('4' * 6)
print(['1', '0'] * 3)


var1 = False
var2 = True
var1 = var1 or var2
var2 = var1 and var2
var1 = var1 or var2
print(var1, var2)


d = {'a':2, 'b': 3, 'c':7}
print(set(d))


stocks_1 = {'CDR': 200.0, 'PLW': 420.0}
stocks_2 = {'11B': 510.0, 'CDR': 205.5}

print({**stocks_1, **stocks_2})

var = """

"""
print(len(var))



numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i % 2 != 0 and i < len(numbers):
        del numbers[i]

print(numbers)


stocks_1 = ['TSLA', 'MSFT', 'AMZN']
stocks_2 = ['AAPL', 'NVDA']
print(stocks_1+stocks_2)
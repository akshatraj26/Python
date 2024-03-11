l = [456, 2, 2, 5, 56, 34]
# l.clear()
print(any(l))
print(all(l))

print(sorted(l))
# del(l)

l.append('3')
print(l)


class Hi:
    pass

h = Hi()
print(id(h))
print(bool(h))
print(object())
print(type(h))


hashtags = ['sport', 'gym', 'cardio', 'workout']
result = '#' + ' #'.join(hashtags)
print(result)

techs = tuple('pandas') + ('sql', )
print(techs)


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
chessboard = [(i, j) for i, j in zip(letters, numbers)]
print(chessboard)


numbers = [i for i in range(-10, -15)]
print(type(numbers))
print(numbers)


nested = [[i for i in range(2)] for j in range(5)]
print(nested)

headers = ['open', 'high', 'low', 'close', 'volume']
print(','.join(headers))

x = 10 ** 2 + 10 / 2 + 10 // 5 + 13 % 5
print(x)

junior = {'python', 'html', 'css', 'git'}
senior = {'python', 'html', 'css', 'django', 'javascript'}
print(junior | senior)
print()
# print(junior + senior)
print(junior.union(senior))


class Vehicle:
    fleet = 0
    def __init__(self, brand):
        self.brand = brand
vehicle = Vehicle('Tesla')
print(hasattr(Vehicle, 'brand'))
print(hasattr(vehicle, 'brand'))


course_name = 'Python in Data Science'
tokens = course_name.split()
print(tokens[-2:])

company = 'Apple'
idx = 10
var = 0

try:
    print(company[idx / var])
except ZeroDivisionError:
    print('first')
except IndexingError:
    print('second')
except:
    print('third')
finally:
    print('end')


#
# number = input('Enter a number: ')
# print(1 / number)

x = '\\\\'
print(len(x))


net_profit = [-10.5, 4.5, 30.8, -3.5, 14.0]
print([value if value >=  0 else 0 for value in net_profit])
print([value if value >= 0 else abs(value) for value in net_profit ])

numbers = [[_ for _ in range(i + 1)] for i in range(5)]
print(numbers)

print(True > False, True < False, True == False)


class Vehicle:
    fleet = 0

    def __init__(self, category=None):
        self.category = category if category else 'vehicle'
        Vehicle.fleet += 1

    def __str__(self):
        return self.category


class LandVehicle(Vehicle):
    def __str__(self):
        return super().__str__() + ': land'


class AirVehicle(Vehicle):
    def __str__(self):
        return super().__str__() + ': air'


veh1 = Vehicle()
veh2 = AirVehicle()
veh3 = AirVehicle()

print(veh2 is veh2, veh2 is veh3)
print(veh1.fleet)


ds_techs = ('sql', ) + ('pandas', )
dev_techs = ('git', ) + ('aws', )
techs = ds_techs + dev_techs
print(techs)


class Person:
    def introduce(self):
        print('Person...')


class Department:
    def introduce(self):
        print('Departament...')


class Worker(Person, Department):
    def info(self):
        self.introduce()


w = Worker()
w.info()


# def func1(x, y):
#     result = x + y + 2 * x * y
#     return None
#
#
# def func2():
#     return func1(1, 2) * func1(2, 1)
#
#
# print(func2())
#
# x = '\'
# print(len(x))



var1 = var2 = 1
var3 = var4 = 0

result1 = var1 ^ var2
result2 = var1 ^ var3
result3 = var1 | var3
result4 = var3 | var4

print(result1, result2, result3, result4)


numbers = [0, 1, 2, 3, 4]
print(sorted(numbers) is numbers)


class Person:
    pass

p = Person()
print(p.__class__.__name__)


author = 'guido van rossum'
print(author.title())


def very_important_fuction():
    """This is a very important function that always returns 1."""
    return 1

print(very_important_fuction.__doc__)

# print(t)
numbers = [0, 4, 2, 3, 4]
print((numbers))


di = dict(f=34, c = 454)
print(di)

a = [1, 2, 3, 4, 5]
b = a
b[:] = [3, 6]
print(a)
print(b)

stocks = {'Apple': 166.42, 'Tesla': 922.8}

for stock in stocks:
    print(stock)

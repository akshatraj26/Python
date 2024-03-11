"""
Write a progression that defines a class Progression and inherits three class from it- AP, GP, and FP. standing for
Arithmetic Progression, Geometric Progression and Fibonacci Progression respectively. Progression should act as  a
user-defined iterator. By default, it should generate integers starting with 0 and advancing in steps of 1.
AP, GP and FP should make use of the iteration facility of Progression class. They should appropriately adjust themselves
to generate numbers in arithmetic progression, geometric progression and Fibonacci progression.
"""


class Progression:
    def __init__(self, start=0):
        self._cur = start

    def __iter__(self):
        return self

    def advance(self):
        self._cur += 1

    def __next__(self):
        if self._cur is None:
            raise StopIteration
        else:
            data = self._cur
            self.advance()
            return data

    def display(self, n):
        print(' '.join(str(next(self)) for i in range(n)))


class AP(Progression):
    def __init__(self, start=0, step=1):
        super().__init__(start)
        self.__step = step

    def advance(self):
        self._cur += self.__step


class GP(Progression):
    def __init__(self, start=1, step=2):
        super().__init__(start)
        self.__step = step

    def advance(self):
        self._cur *= self.__step


class FP(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self.__prev = second - first

    def advance(self):
        self.__prev, self._cur = self._cur, self.__prev + self._cur


print("Default Progression:")
p = Progression()
p.display(20)
print('AP with step 5:')
a = AP(5)
a.display(10)
print("AP with start 2 and step 4:")
a = AP(2, 4)
a.display(10)

print("GP with default multiple:")
g = GP()
g.display(10)

print()
print("GP with start 1 and multiple 3:")
g = GP(1, 3)
g.display(10)


print()
print("FP with default start values:=")
f = FP()
f.display(10)

print()
print("FP with start values 4 and 6:=")
f = FP(4, 6)
f.display(10)


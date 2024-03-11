class AvgAdj:
    def __init__(self, data):
        self.__data = data
        self.__len = len(data)
        self.__first = 0
        self.__sec = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__sec == self.__len:
            raise StopIteration
        self.__avg = (self.__data[self.__first] + self.__data[self.__sec]) / 2

        self.__first += 1
        self.__sec += 1
        return self.__avg


lis = [i for i in range(45, 65)]
coll = AvgAdj(lis)
print(coll)

print(coll.__next__())
print(coll.__next__())
print(coll.__next__())
print(coll.__next__())
print(coll.__next__())
print(coll.__next__())
print(coll.__next__())

lis = [i for i in range(45, 65)]
coll = AvgAdj(lis)
print(coll)

print()

for val in coll:
    print(val)

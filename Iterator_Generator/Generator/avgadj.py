def AvgAdj(list1):
    for i in range(len(list1)):
        yield (list1[i], list1[i+1]), (list1[i] + list1[i+1]) / 2


lis = [10, 20, 30, 40, 50, 60]
avg = AvgAdj(lis)
print(avg.__next__())
print(avg.__next__())
print(avg.__next__())
print(avg.__next__())
print(avg.__next__())

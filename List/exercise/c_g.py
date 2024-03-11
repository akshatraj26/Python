# look for median
lis = [1, 2, 3, 4, 5,  6, 7]

n = len(lis)
if n % 2 == 0:
    i = int(n/2 -1)
    j = int(n/2)
    median = (lis[i] + lis[j]) / 2
else:
    i = int(n / 2)
    median = lis[i]

print(median)


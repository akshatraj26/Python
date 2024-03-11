# mean, median and mode

l = [10, 20, 30, 30, 30, 30, 40, 60, 70, 80]

mean = sum(l) / len(l)

# median
n = len(l)
l.sort()
if n % 2 ==0:
    i = l[n // 2]
    j = l[n//2 -1]
    median = (i + j) / 2

else:
    median = l[n//2]


# Mode
lst1 = [0, 0]
for num in l:
    occ = l.count(num)
    if occ >lst1[0]:
        lst1 = [occ, num]

print("Mean:-", mean)
print("Median:-", median)
print('Mode:- ', lst1[1])

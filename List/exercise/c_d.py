lis = [-23, 45, 23, 78, 34, 64, -5, -8, -12]

pos = []
neg = []
for i in range(len(lis)):
    if lis[i]<0:
        neg.append(lis[i])
    else:
        pos.append(lis[i])


print(pos)
print(neg)
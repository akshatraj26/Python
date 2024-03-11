lis = [2, 2, 5,6, 23, 12, 12, 23, 55]

uni = []
for i in range(len(lis)):
    if lis[i] not in uni:
        uni.append(lis[i])

print(uni)
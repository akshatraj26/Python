def create_list(lis1, lis2):
    lis = []
    for i in range(len(lis1)):
        for j in range(len(lis2)):
            if lis1[i] == lis2[j]:
                lis.append(lis1[i])

    return lis

l = [10, 20, 30, 40,60,  50]
l2 = [50, 60, 70 ,90, 100]
print(l)
print(l2)

intersect = create_list(l, l2)
print(intersect)
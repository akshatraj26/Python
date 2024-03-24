lst	=[10, 20,	30,	10,	40,	30,	20,	50,	60,	50,	60]
s = set(lst)
for num in s:
    c = lst.count(num)
    if c == 1:
        print(num, "occurs only once")
        break

for i in lst:
    c = lst.count(i)
    if c == 2:
        print(i, 'occurs twice')
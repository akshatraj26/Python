import json5
lst = [i for i in range(10, 100, 10)]
tpl = ('Akshat', 23, 235465)
dct = {'Amogsidh': 29, 'Akshat':23, 'Ujjwal': 23}

str1 = json5.dumps(lst)
str2 = json5.dumps(tpl)
str3 = json5.dumps(dct)

l = json5.loads(str1)
t = tuple(json5.loads(str2))
d = json5.loads(str3)

print(l)
print(t)
print(d)
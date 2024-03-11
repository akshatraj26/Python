# When inserting tuple, list we have to convert it to a string

tpl = ('Akshat', 23, 235465)
lst = {23, 45, 56, 7, 4, 56}
d = {'Name': 'Amogsidh', 'Age': 29}

f = open('write_ds', 'w')
f.write(str(tpl))
f.write(str(lst))
f.write(str(d))

f = open('write_ds', 'r')
data = f.read(10)
# for character


#  Ways to read the data
for data in f:
    print(data, end='')

print("\nSecond way")
# second way
while True:
    data = f.readline()
    if data == '':
        break
    print(data, end='')




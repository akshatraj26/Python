donars = {
    'Amog': ['Nagpur', 29, 1],
    'Amit': ['Bhopal', 18, 2],
    'Akshat': ['Loha', 19, 3],
    'Chandan': ['India', 23, 2],
    'Pritesh': ['China', 25, 2],
    'Palak': ['Russia', 23, 3],

}
f = open('c_g', 'w+')
for k, v in donars.items():
    s = '{0:20s}{1:40s}{2:2s}{3:1s}\n'.format(k, v[0], str(v[1]), str(v[2]))
    f.write(s)

f.seek(0, 0)
while True:
    data = f.readline()
    if data == '':
        break

    name = data[:20]
    address = data[20:59]
    age = int(data[60:62:])
    bloodtype = int(data[62:])
    if age<=25 and bloodtype == 2:
        print(name, address, age, bloodtype)

f.close()

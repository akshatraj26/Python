f = open('a.dat', 'wb+')
d = b'\xee\x86\xaa'   # series of 3 bytes, \x indicates hexadecimal
f.write(d)

f = open('a.dat')
d = f.read()
print(d)

f.close()
f = open('numberstxt', 'w+')
f.write(str(233)+ '\n')
f.write(str(13.56))
f.seek(0)

a = int(f.readline())
b= float(f.readline())

print(a +b)
print(a- b)


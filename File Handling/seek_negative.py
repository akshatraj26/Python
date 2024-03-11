f = open('data.txt', 'w')
msg = b'Code is like humor. When you have to explain it, its bad.'
f.close()


f = open('data.txt', 'rb')
f.seek(0, 2)

file_size = f.tell()
f.seek(file_size - 10)

print(f.tell())
print(f.readline().decode('utf-8'))
f.close()
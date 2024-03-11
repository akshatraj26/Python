f= open('messages', 'rb')
# f.seek(0)
# f.seek(15, 0)
f.seek(6, 1)

print(f.tell())


print("")
print(f.readline())
f.close()
names = ['Sagar', 'Sameer', 'Amogsidh', 'Pritesh', 'PHoole', 'Akshat']
# f = open('c_h', 'w+')
f = open('c_h', 'r')
# for name in names:
#     f.write(name + '\n')

# My way of approaching problems
# n = int(input('Enter the student number:- '))
# try:
#     data = f.readlines()
#     print(n, data[n])
# except Exception as e:
#     print("Please put the index in range of", len(data))

# Book ways

f.seek(0, 0)
print(f.tell())
n = int(input("Enter Student Number:- "))
f.seek(0, 0)
i = 1
while i < n:
    data = f.readline()
    i += 1
data = f.readline()
print("Num:", n, 'Name=', data)
f.close()

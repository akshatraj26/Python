# CReate a new file


# try:
#     f = open('sample2', 'w+')
#     f.write('akshat raj 23\n')
#     f.write('amogsidh 29\n')
#     f.write('pritesh 32\n')
#     f.write('aarti 23\n')
#     # f.close()

#     # f = open('File Handling/exercise/sample2', 'r')
#     print(f.readline())
#     f.close()
# except FileNotFoundError:
#     print("File Not found")


f1 = open('student2.txt', 'r')
f2 = open('sample2', 'r')
combined = open('combined.txt', 'w')

while True:
    data1 = f1.readline()
    if data1 == '':
        break
    combined.write(data1)
    data2 = f2.readline()
    if data2 == '':
        break
    combined.write(data2)

    if data1 != '':
        while True:
            data1 = f1.readline()
            if data1 == '':
                break
            combined.write(data1)

    if data2 != '':
        while True:
            data2 = f2.readline()
            if data2 == '':
                break
            combined.write(data2)

f1.close()
f2.close()
combined.close()

#
# combine = open('combined.txt', 'r')
# data = combine.readline()
# print(data)

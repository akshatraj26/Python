# file = open('first', 'w')
#
# file.write("How Are You Doing? My Friend.")
# file.close()

# file = open('first', 'r+')
# data = file.readline()
#
# text_upper = ''
# for d in data:
#     text_upper += d.upper()
#
# print(text_upper)
#
# f = open('first_upper', 'w')
# f.write(text_upper)
#
# f = open('first_upper', 'r')
# data = f.read()
# print(data)

f = open('student.txt', 'r')
a = open('student2.txt', 'w')

while True:
    data = f.readline()
    if data == '':
        break
    data = data.upper()
    a.write(data)

f.close()
a.close()
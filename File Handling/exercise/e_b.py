"""
Write a program to append the contents of one file at the end of another.
"""
f = open("../messages", 'r')
d = open("../read_write", 'r+')

paragraph = ''
while True:
    data = f.readline()
    if data == '':
        break
    paragraph += data

paragraph2 = ''
while True:
    data = d.readline()
    if data == '':
        break
    paragraph2 += data

paragraph2 += paragraph
print(paragraph2)
d.seek(0, 0)
d.write(paragraph2)
f.close()
d.close()


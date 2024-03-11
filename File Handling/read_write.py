# Read/Write Operations

msg = 'Bad officials are elected by good citizens who do not vote.\n'
msgs = ['Humpty\n', 'Dumpty\n', 'Sat\n', 'On\n', 'a\n', 'wall\n']
f = open('read_write', 'w')
f.write(msg)
f.writelines(msgs)

f.close()
f = open('read_write', 'r')
data = f.read()
print(data)
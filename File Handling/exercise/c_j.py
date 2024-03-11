"""
Given a text file, write a program to create another text file deleting the words 'a', 'the', 'an' and replacing each
one of them with a blank space.
"""

f = open('c_j.txt', 'w+')
f.write('Honesty is the pillar of success. a man should never lie and always eat an apple.')
f.write("The world is full of duplicates.")
f.write('I want an apple a day.')
f.write('I cannot do the stuff that you want me to do.')

f.close()

f = open('c_j.txt', 'r')
data = f.read()

data = data.replace(' the ', '  ')
data = data.replace(' a ', '  ')
data = data.replace(' an ', '  ')



t = open('c_j_delete.txt', 'w+')
t.write(data)
t.close()

t = open('c_j_delete.txt', 'r')

data = t.read()
print(data)



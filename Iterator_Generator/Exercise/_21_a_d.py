"""
Suppose there are two lists, each holding 5 strings. Write a program to generate a list that consists of strings that
are concatenated by picking corresponding elements from thr two lists.
"""
li = ['A', 'A', 'H', 'P', 'R']
li1 = ['kshat', 'mog', 'imanshu', 'ritesh', 'aj']
l = []
for first, name in zip(li, li1):
    full_name = first + '' + name
    l.append(full_name)

print(l)

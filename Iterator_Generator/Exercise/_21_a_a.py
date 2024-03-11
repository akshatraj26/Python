"""
Write a program to create a list of 5 odd integers. Replace the third element with a list of 4 even integers.
Flatten, sort and print the list.
"""

odd = [n for n in range(10) if n % 2 != 0]
even = [n for n in range(1, 10) if n % 2 ==0]

odd[2] = even
print(odd)


lis = []
for l in odd[2]:
    lis.append(l)


lis1 = odd[0:2] + lis + odd[3:]
print(lis1)
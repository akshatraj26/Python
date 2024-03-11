"""
Write a program to receive an 8-bit number into a variable and then set its odd bits to 1
"""

def display_bits(n):
    for i in range(7, -1, -1):
        andmask = 1 << i
        k = n & andmask
        print('0', end='') if k == 0 else print('1', end='')

def modify_bits(n):
    for i in range(7, -1, -2):
        ormask = 1 << i
        n = n | ormask

    return n

num = int(input('Enter a number between 0 to 255 :-'))
display_bits(num)
num = modify_bits(num)
print('\n')
display_bits(num)

"""
Consider an unsigned integer in which rightmost bit is numbered as 0. Write a function checkbits(x, p, n) which returns
True if all 'n' bits starting from position 'p' are on, False otherwise. For example, checkbits(x, 4, 3) will return true
if bits 4, 3, and 2 are in 1 in number x.

"""


def display_bits(n):
    for i in range(7, -1, -1):
        andmask = 1 << i
        k = n & andmask
        print("0", end='') if k == 0 else print('1', end='')
    print()


def checkbits(x, p, n):
    no = 0
    for i in range(0, n):
        if ((x >> (p-1)) & 1) != 1:
            return 0
        p -= 1
    return -1


num = int(input("Enter a number between 0 and 255:- "))
display_bits(num)
p = int(input("Enter Position :- "))
n = int(input("Enter number of bits:- "))
flag = checkbits(num, p, n)
if flag == 1:
    print(n, 'bits starting from position', p, 'are on')
else:
    print(n, 'bits starting from position', p, 'are off')

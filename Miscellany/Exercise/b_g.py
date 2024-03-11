"""
Write a program to receive 8 bit number into a variable and then exchange its higher 4 bits with lower 4 bits.
"""

def display_bits(n):
    for i in range(7, -1, -1):
        andmask = 1 << i
        k = n & andmask
        print('0', end='') if k == 0 else print('1', end='')

num = int(input('Enter a number between 0 to 255 :-'))
display_bits(num)
n1 = num << 4
n2 = num >> 4
num = n1 | n2
print("\nAfter exchanging bits:")
display_bits(num)
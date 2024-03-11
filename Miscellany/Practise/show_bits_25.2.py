"""
Define a function show_bits() which display binary equivalent of the integer passed to it. Call it to display binary
equivalent of 45.
"""


def show_bits(n):
    for i in range(32, -1, -1):
        andmask = 1 << i
        k = n & andmask
        # print(k)
        print('0', end='') if k == 0 else print('1', end='')


show_bits(45)
print()
print(bin(45))

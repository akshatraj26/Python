import sys

def dec_to_binary(n):
    r = n % 2
    print(r)
    n = n // 2
    # print(n)
    if n != 0:
        dec_to_binary(n)
    print(r, end='')

sys.setrecursionlimit(10**6)
dec_to_binary(56)
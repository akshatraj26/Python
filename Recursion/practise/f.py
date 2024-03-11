def dec_bin(n):
    r = n % 2
    n = n // 2
    print(r, end='')

    if n != 0:
        dec_bin(n)

dec_bin(7)

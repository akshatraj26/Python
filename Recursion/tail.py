def tailprint(n):
    if n == 22:
        return
    else:
        print(n)
        tailprint(n+1)
print()
tailprint(10)
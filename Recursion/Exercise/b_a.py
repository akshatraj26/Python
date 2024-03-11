def headsum(n):
    if n != 0:
        s= n + headsum(n-1)
    else:
        return 0
    return s


n = headsum(5)
print(n)
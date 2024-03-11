def fab(n):
    if n > 100 :
        return
    else:
        f = [0, 1, fab(n-1)+fab(n-2)]

        return f

print(0, 1)
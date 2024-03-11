def p(n):
    if n<1:
        return
    else:
        print(n)
        p(n//2)

p(100)
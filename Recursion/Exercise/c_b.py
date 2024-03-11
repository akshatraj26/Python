def fun(num):
    if num > 100:
        return num - 10
    return fun(fun(num + 11))


print(fun(75))

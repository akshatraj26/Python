def fun(n):
    if n%5 ==0:
        return True
    else:
        False

lst = ['A', 'X', 'Y', '5', 'M', 'D', "Y"]
f1 = filter(str.isalpha, lst)
print(list(f1))

ls2 = [5, 10, 18, 27, 25]
f2 = filter(fun, ls2)
print(list(f2))
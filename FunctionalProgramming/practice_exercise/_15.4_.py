def my_map(fun, seq):
    result = []
    for ele in seq:
        result.append(fun(ele))

    return result


lis1 = [5, 7, 9, 8, 3, 12]
ls2 = my_map(lambda x: x * x, lis1)
print(ls2)

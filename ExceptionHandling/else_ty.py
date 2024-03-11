try:
    lst = [i for i in range(10, 70, 10)]
    lst = [10, 20, 30, 40, 50, 'abc']
    for num in lst:
        i = int(num)
        j = i * i
        print(i, j)
        
except ValueError:
    print(ValueError.args)
else:
    print("Total numbers processed", len(lst))
    del(lst)
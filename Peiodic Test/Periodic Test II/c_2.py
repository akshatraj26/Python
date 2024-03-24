# sum of natural till 25
def sum_till(n):
    if n == 1:
        return n
    return n + sum_till(n-1)


print(sum_till(25))
def sum(n):
    if n == 0:  # base case
        return 1
    else: # recursive case
        return n + sum(n-1)


f = sum(10)
print(f)

def sum_dig(n):
    if n == 0:
        return 0
    else:
        n % 10 + sum_dig(n/10)


s= sum_dig(121675)
print(s)


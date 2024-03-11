def running_sum(n):
    if n == 0:
        return 0
    else:
        return n + running_sum(n-1)


print(running_sum(25))
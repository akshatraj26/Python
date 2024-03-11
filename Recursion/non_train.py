def non_tail(p):
    if p<1:
        return 0
    else:
        return 1 + non_tail(p/2)


p = non_tail(10)
print(p)
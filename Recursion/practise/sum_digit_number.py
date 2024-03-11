def rsum(num):
    if num != 0:
        digit = num % 10
        print("Digit:- ", digit)
        num = num // 10
        print("Leftover:- ", num)
        sum = digit + rsum(num)
    else:
        return 0
    return sum


print(rsum(345))

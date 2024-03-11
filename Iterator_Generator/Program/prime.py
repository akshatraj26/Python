def prime_num(num):
    count = 0
    for i in range(1, num+1):
        if num % i ==0:
            count += 1
    print(count)
    if count == 2:
        return "Prime"
    else:
        return "Not Prime"

print(prime_num(13))


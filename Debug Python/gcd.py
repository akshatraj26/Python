def find_gcd(num1, num2):
    min_num = min(num1, num2)
    for i in range(min_num, 1, -1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    return gcd


n1 = int(input('Enter the first number:-'))
n2 = int(input('Enter the second number:-'))
print(find_gcd(n1, n2))


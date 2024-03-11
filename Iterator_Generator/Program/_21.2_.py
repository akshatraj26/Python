"""
Write a program that generates prime numbers below 3 million. Print sum of these prime numbers.
"""

def generates_primes():
    num = 1
    while True:
        if isprime(num):
            yield  num
        num += 1

def isprime(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(2, n//2):
            return False
        else:
            return True
    else:
        return False



total = 0
for next_prime in generates_primes():
    if next_prime < 300000:
        total += next_prime
        print(total)
    else:
        print(total)

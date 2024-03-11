'''
Two numbers are received through the keyboard into variables a and b. Write a recursive function that calculate the value of a ** b.
'''
def calculate(a, b):
    if b == 0:
        return 1

    if b == 1:
        return a

    prod = a * calculate(a, b-1)
    return prod


print(calculate(4, 2))
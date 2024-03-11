"""
Write a recursive function that receives a number as an input and returns the square of the number.
Use the mathematical identity (n-1)^2 = n^2 + n + 1
"""


def square(s):
    if s < 0:
        s = s * -1

    if s == 1:
        return 1
    sq = square(s - 1) + 2*s - 1
    return sq


print(square(5))

print(square(-4))
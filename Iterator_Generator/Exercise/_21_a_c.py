"""
Write a program to generate a list of numbers in the range 2 to 50 that are divisible by 2 and 4.
"""

lis = [num for num in range(2, 50) if num % 2 == 0 and num % 4 == 0]
print(lis)

lis = []
for num in range(2, 50):
    if num % 2 == 0 and num% 4 ==0:
        lis.append(num)


print(lis)
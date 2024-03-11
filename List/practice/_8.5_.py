"""
Generate and store in a list 20 random numbers in the range of 10, 100. From the list delele all those entries which are
value between 20 and 50
"""
import random
a = []
i = 1
while i<=15:
    num = random.randint(10, 100)
    a.append(num)
    i += 1

print(a)

for num in a:
    if num > 20 and num < 50:
        a.remove(num)

print(a)
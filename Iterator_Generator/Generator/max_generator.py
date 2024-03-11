# generate 20 random number in the range of 10 to 200 and obtain maximum out of them
import random
print(max(random.randint(10, 100) for i in range(20)))


# print sum of cubes of all numbers less than 20
print(sum(n ** 3 for n in range(20)))
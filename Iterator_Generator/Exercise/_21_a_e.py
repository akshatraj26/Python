"""
Suppose a list contains 20 integers generated randomly. Receive a number from the keyboard and report position of all
occurrences of this number in the list.
"""
import random
lst = [int(10 * random.random()) for n in range(20)]
print(lst)

num = int(input("Enter the number in the range of 1 to 10:-"))
indxlist = [i for i in range(len(lst)) if lst[i] == num]

print(indxlist)
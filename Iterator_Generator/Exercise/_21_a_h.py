"""
Write a program to obtain a median value of a list of numbers, without disturbing the order of the numbers in the list.
"""

l = [1,2,3, 4,5, 6]
length = len(l)
s = sorted(l)
# print(length //2 - 1)
# print(length //2 + 1)

# s = sum(s[length//2 - 1: length//2 + 1]) /2
# print(s)

id = s[length // 2 - 1 : length //2 + 1]
print((s[length // 2 -1] + s[length // 2 + 1]) / 2)
print("id", id)
# print(s[id])



lst2 = [7, 6, 5, 4, 3, 2, 1]
sor = sorted(lst2)
length = len(lst2)



# m = (sum(s[length // 2 -1 : length // 2 + 1]) / 2.0, s[length // 2])[length % 2]
print(sor[length // 2])
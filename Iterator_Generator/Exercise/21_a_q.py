"""
Stores  36 combination of two dice
"""

combination = [(d1, d2) for d1 in range(1,7) for d2 in range(1, 7)]
print(combination)





a = [[], "abc", [0], 1, 0]
print(list(filter(bool, a)))
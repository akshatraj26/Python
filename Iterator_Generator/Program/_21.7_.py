"""
Suppose we have a list of 5 integer ana a tuple of 5 floats. Can we zip them and obtain an iterator? if yes, how?
"""

list1 = [2, 56, 6, 7, 3]
float1 = [23.3, 45.3, 356., 656., 35.]

ite = zip(list1, float1)
print(list(ite))
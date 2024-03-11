"""
A list contains some negative and some positive numbers. Write a recursive function that sanitizes the list by replacing
 all negative numbers with 0
"""

def sanitize(lst, start, end):
    if start > end:
        return
    if lst[start] < 0:
        lst[start] = 0
    start += 1
    sanitize(lst, start, end)
    return lst


num = [-20, 55, 23, 89, -45, -12]
print(sanitize(num, 0, len(num)-1))

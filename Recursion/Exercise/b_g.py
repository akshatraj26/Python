"""
Write a recursive function that receives the list of numbers that it receives.
"""

def reverse(lst, start, end):
    if start > end:
        return
    lst[start], lst[end] = lst[end], lst[start]
    reverse(lst, start + 1, end -1)
    return lst


a = [10, 20, 30, 50, 60]
print(reverse(a, 0, len(a)-1))

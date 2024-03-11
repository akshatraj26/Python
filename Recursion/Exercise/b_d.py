"""
A string is entered through the keyboard. Write a recursive function that removes any tabs present in this string.
"""

def replace(source, i, n):
    global target
    if i == n:
        return
    if source[i] == '\t':
        pass
    else:
        target += source[i]
    i += 1
    replace(source, i, n)

s = "Raindrops on Roses and whiskers on kittens"
target = ''
replace(s, 4, len(s)-1)
print(target)

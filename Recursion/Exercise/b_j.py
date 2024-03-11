"""
Write a recursive function to obtain length of a given string.
"""
def get_length(s):
    if s == '':
        return 0
    else:
         return 1 + get_length(s[1:])

print(get_length('akshatraj fd'))


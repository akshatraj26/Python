"""
Write a Python program that accepts a hyphen-seprated sequence of words as input and cells a function convert()
which converts it into a hyphen-seprated sequence after sorting them alphabetically. For exxample, it the input string is


'here-come-the-dots-followed-by-dashes'

then, the converted string should be

'by-come-dashes-dots-followed-here-the'
"""

def convert(s):
    sp = s.split('-')
    sort_s = sorted(sp)
    return '-'.join(sort_s)


print(convert("here-come-the-dots-followed-by-dashes"))

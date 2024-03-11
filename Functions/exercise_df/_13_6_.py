"""
Write a program that defines a function convert() that receives a string containing a sequence of whitespace
seprated words and returns a string after removing all duplicate words and sorting them alphanumarically.

s = 'Sakhi was a singer because her mother was a singer, and Sakhi'\s mother was a singer because her father was a singer.'
"""
s = 'Sakhi was a singer because her mother was a singer, and Sakhi\'s mother was a singer because her father was a singer.'


def convert(text):
    words = [word for word in text.split()]
    print(words)
    s = set(words)
    l = list(s)
    sor = sorted(l)
    j = ' '.join(sor)
    # j = ' '.join(sorted(list(set(words))))
    return j

s = 'I felt happy because I saw the others were happy and because I knew I should feel happy, but I was\'t really happy'
print(convert(s))

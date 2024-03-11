"""
Pangram is a sentence that uses every letter of the alphabet. Write a program that checks whether a given string is
pangram or not, through a user-defined function ispangram().
"""

def ispangram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(s.lower())

print(ispangram('The quick brown fox jumps over the lazy dog.'))
print(ispangram("jgfbjdgtjuybe  "))
print(ispangram("Carzy Fredrick bought many very exquisite opal jewels."))

"""
Write a program that uses a generator to create a set of unique words from a line input through keyboard
"""

user = input("Enter a sentence:-")
s = set(user.split())

print(s)
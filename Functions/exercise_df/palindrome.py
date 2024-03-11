"""
A palindrome is a word or phrase which reads the same in both directions. Given below some palindrome strings.
deed
level
Malayalam
Rats live on no evil star
Murder for a jar of red rum

Write a program that defines a function ispalindrome() which checks whether a given string is a palindorme or not.
Ignore spaces and case mismatch while checking for palindrome.
"""


def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1

    while right >= left:
        if s[left] == '':
            left += 1
        if s[right] == '':
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("deed"))

s = 'hi hell'

#
# def palindrome(s):
#     s = s.lower()
#     length = len(s)
#
#     for i in range(0, length):
#         if s[i] == '':
#             pass
#         if s[length -1-i] == "":
#             pass
#         if s[i] != s[length - i - 1]:
#             return False
#     return True

#
# print(palindrome("Murder for a jar of red rum"))
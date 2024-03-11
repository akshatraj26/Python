'''
A String is entered through the keyboard. Write a recursive function that checks whether the string is a palindrome or not.
'''

def is_palindrome(s, start, end):
    if start > end:
        return True

    if s[start] != s[end]:
        return False
    status = is_palindrome(s, start+1, end-1)
    return status


st1 = 'malayalam'
print(is_palindrome(st1, 0, len(st1)-1))
st2 = 'amogham'
print(is_palindrome(st2, 0, len(st2)-1))
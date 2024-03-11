# # count that number
# def count_vowel(s, idx, count):
#     if s in 'aeiou':

def is_vowel(s):
    return s.lower() in ['a', 'e', 'i', 'o', 'u']


# using iteration
def count_vowels(s):
    count = 0
    for i in range(len(s)):
        if is_vowel(s[i]):
            count += 1
    return count


# using recursion
def count_vowel(s, n):
    if n == 1:
        return is_vowel(s[n-1])

    return count_vowel(s, n-1) + is_vowel(s[n-1])


string = 'Hey, Where did you leave your friend'
print(count_vowels(string))


s = "Hi, How are You doing?"
d = count_vowel(string, len(string))
print('Vowels', d)
print("Length :-", len(string))


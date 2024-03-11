def count_alphabets_digits(s):
    d = {'Alphabets': 0, 'Digits': 0}
    for i in s:
        if i.isalpha():
            d['Alphabets'] += 1
        if i.isdigit():
            d['Digits'] += 1
    return d

print(count_alphabets_digits('akshat raj3454'))

d = count_alphabets_digits("James Bond 007")
print(d)
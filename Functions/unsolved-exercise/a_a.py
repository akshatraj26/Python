def count_lower_upper(text):
    d = {'lower': 0, 'upper': 0}
    for char in text:
        if char.islower():
            d['lower'] += 1
        if char.isupper():
            d['upper'] += 1

    return d

s =count_lower_upper("Hi howe ARe you")
print(s)
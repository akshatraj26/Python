def sanitize_list(lis):
    return list(set(lis))


lis = [45, 23,23, 12, 12, 45, 89, 89]
d = sanitize_list(lis)
print(d)
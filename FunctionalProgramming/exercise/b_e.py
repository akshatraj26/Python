lst = ['Malayalam', 'Drawing', 'madamlamadam', '1234321']

res = list(filter(lambda x: x[::-1].lower() == x.lower(), lst))
print(res)
def print_it(a, b, c, d, e):
    print(a, b, c, d, e)

lst = [12, 20, 30, 40, 345]
tpl = (23, 45,67,34,89)
s = {23, 45,678,9,43}
print_it(*lst)
print_it(*tpl)
print_it(*s)
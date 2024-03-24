a = 22
b =23
if a < b:

    result = 'a is greater'
    print(result)

s = '  hi  '
print(s.strip().center(21, 'i'))
print(s.center(21, 'i').strip())


def fun(lst = []):
    lst.append('Hi')
    print(lst)


fun()
fun()
fun()


def fun(lst= None):
    if lst is None:
        lst = []
    lst.append('HiCorrected')
    print(lst)


fun()
fun()

# age = -13
# assert age >= 0, 'Negative Age'

# Attribute Error
s = 'Hi'
# s.convert()

lst = [10, 20, 30]
# print(lst[3])


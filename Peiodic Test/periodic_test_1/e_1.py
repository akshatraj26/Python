ans = 'y'
pos = neg = zero = 0
while ans == 'y' or ans == 'Y':
    num = int(input("Enter a number:-"))
    if num == 0:
        zero += 1
    elif num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    ans = input("Do you want to continue:-")

print('You	entered',	pos,	'positive	numbers')
print('You	entered',	neg,	'negative	numbers')
print('You	entered',	zero,	'zeros')
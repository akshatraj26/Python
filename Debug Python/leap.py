def isleap(y):
    return year % 100 == 0 or year % 4 ==0 or year % 400 == 0


year = int(input('Enter any year:-'))
result = 'Leap' if isleap(year) else 'Not Leap'
print(result)
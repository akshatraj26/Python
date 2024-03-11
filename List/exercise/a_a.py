import random

msg = list('www.kicit.com')
print(msg[-1])


num1 = [10, 20, 30, 40, 50]
num2 = num1
print(id(num1))
print(type(num2))
print(isinstance(num1, list))
print(num1 is num2)


num1[2:4] = []
print(num1)


num1 = [10, 20, 30, 40, 50]
num2 = [60 ,70, 80]
num1.append(num2)
print(num1)

# num1 = [10, 20, 30, 40, 50]
# a = ['a', 'b', 'c', 'y', 'z']
# b = ['a', 'b', 'c', *num1, 'y', 'z']
# print(b)


i = 1
lis = []
for i in range(20):
    num = random.randint(0 ,50)
    lis.append(num)

num = 4
for i in range(len(lis)):
    if lis[i] == num:
        print("Number found at position:-", i)
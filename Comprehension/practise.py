import random

# 12.1 Using a list comprehension, wap to generate a list of numbers in the range of 2 to 50 that are divisible by 2 and 4

a = [a for a in range(2, 50) if a % 2 == 0 and a % 4 == 0]
print(a)

# 12.2 flatten list using list comprehenssion
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print([num for lis in mat for num in lis])

# create a set containing some randomly generated number in range of 15 to 45. count how many number are less than 30
# delete all number less than  30

a = {random.randint(15, 45) for n in range(20)}
print(a)

count = len({n for n in a if n < 30})
print(count)
s = {n for n in a if n < 30}
print(s)
print(a - s)

# 12.4 eliminate empty list
lst = [(), (), (10), (10, 20), (","), (10, 20, 30), (40, 50), (), (50)]

tpl = [tpl for tpl in lst if tpl]
print(tpl)

# 12.5
s = 'dreams may change, but friends are forever'
a = [" ".join(w.upper() for w in s.split())]
print(a[0])

# 12.5 remove vowels from key
words = {'Tub': 1, 'Towel': 2, 'Nailcutter': 4, 'Soap': 23}

w = {''.join(key for key in k if key not in 'aeiou'): v for (k, v) in words.items()}
print(w)


# 12.7 add 3x 4 list using list and list comprehension

mat1 = [[n for n in range(1,5)] ,[j for j in range(5, 9)] ,[k for k in range(9, 13)]]
mat2= [[n for n in range(1,5)] ,[j for j in range(5, 9)] ,[k for k in range(9, 13)]]
mat3 = [[0 for i in range(4)],[0 for i in range(4)], [0 for i in range(4)]]
print(mat1)
print(mat2)
print(mat3)

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat3[i][j] = mat1[i][j] + mat2[i][j]

print(mat3)


# using list comprehension

print([[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))])


# 12.8
emp = {
    'A101': {'name': 'Ashish', 'age':23, 'salary':21000},
    'B102': {'name': 'Dinesh', 'age': 22, 'salary': 12200},
    'A103': {'name': 'Ramesh', 'age': 28, 'salary': 11000},
    'D104': {'name': 'Akheel', 'age': 30, 'salary': 18000},
    'A105': {'name': 'Akaash', 'age': 32, 'salary': 20000}
}
# key starts with a
a = {k: v for k, v in emp.items() if k.startswith('A')}
print(a)

# all codes and names
b = {k:v['name'] for k, v in emp.items()}
print(b)



# all code and age
c = {k:v['age'] for k, v in emp.items()}
print(c)

# code and ages where age > 30
d = {k:v['age'] for k, v in emp.items() if v['age'] >30}
print(d)

# code and name where name starts with A
c = {k:v['name'] for k, v in emp.items() if v['name'].startswith('A')}
print(c)


# salary beteeen 13000 to 20000
f = {k:v['salary'] for k, v in emp.items() if v['salary'] > 13000 and v['salary'] < 20000}
print(f)


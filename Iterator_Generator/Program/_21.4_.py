"""
Create 3 lists --  a list of names, a list of ages and a list of salaries. Generate and print a list of tuples containing
name, age, salary from the 3 lists. From list generates 3 tuples -- one containing all names, another containing all
ages and third containing all salaries.
"""

names = ['Amol', 'Anil', 'Aksah']
ages = [25, 23, 27]
salaries = [345555, 674433, 900000]

iterator = zip(names, ages, salaries)
for ite in iterator:
    print(ite)


iterator = zip(names, ages, salaries)
lis = list(iterator)
print(lis)

# unzip
n, a, s = zip(*lis)
print(n)
print(a)
print(s)

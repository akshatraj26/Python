class Employee:
    pass

obj = Employee()
obj.Name = 'Amogsidh'
obj.age = 23
obj.Salary = 244555
obj.Address = 'Ratnagiri by pass'
obj.Hobbies = ['Playing', 'Akshat']

print(obj.__dict__)
del obj.Hobbies

print(obj.__dict__)
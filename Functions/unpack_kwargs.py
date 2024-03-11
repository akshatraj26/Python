def print_it(name = 'Sanjay', marks =34):
    print(name, marks)

d = {'name':'Amogsidh', 'marks':100}
print_it(*d)
print_it(**d)
employees = {'Pritesh', 'Amogsidh' , 'Akshat', 'Rishikesh', 'Ujjwal', 'Krishnapurb', 'SaurabhSuman'}

res = list(filter(lambda x: len(x)>8, employees))
print(res)
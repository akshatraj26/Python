lst = {'Pritesh': 45, 'Amogsidh' : 50, 'Akshat':60, 'Rishikesh': 35}

res = list(filter(lambda x: x[1]>=40, lst.items()))
print(res)
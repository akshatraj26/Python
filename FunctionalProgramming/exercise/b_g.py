d = {
    'Dinesh': {'last_name': 'Sahare', 'age': 30, 'Grade': 'Skilled'},
    'Ram': {'last_name': 'Jog', 'age': 35, 'Grade': 'Semi-Skilled'},
    'S.': {'last_name': 'Sam', 'age': 25, 'Grade': 'Highly-Skilled'},
    'Adi': {'last_name': 'Lim', 'age': 25, 'Grade': 'Highly-Skilled'},
    'Ann': {'last_name': 'Mir', 'age': 25, 'Grade': 'Highly-Skilled'}
}

res = list(filter(lambda x: x[1]['Grade'] == 'Highly-Skilled', d.items()))
print(res)

# serialize/deserialize a dictionary
import json5
f = open('dictionary', 'w+')
dct = {'Amogsidh': 29, 'Akshat':23, 'Ujjwal': 23}
json5.dump(dct, f)

f.seek(0)

indict = json5.load(f)
print(indict)
f.close()
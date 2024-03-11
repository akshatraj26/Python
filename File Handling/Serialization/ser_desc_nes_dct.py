# serialize/deserialize nested dict
import json5
contacts = {
    'Anil' : {'DOB': '17/11/98', 'Favorite': "Igloo"},
    'Amog' : {'DOB': '15/10/99', 'Favorite': 'Arctic'},
    'Akshat': {'DOB': '26/07/2000', 'Favorite': "Language"}
}

f = open('nested_dict', 'w+')
json5.dump(contacts, f)
f.seek(0)

nes_dct = json5.load(f)
print(nes_dct)
f.close()
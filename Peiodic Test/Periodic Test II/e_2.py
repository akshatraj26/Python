import operator
dct = {'A101'	:	('Rahul',	'Ajay',	'Joshi'),
        'A102'	:	('Ramesh',	'Atul',	'John'),
        'A121'	:	('Ritesh',	'Abhin',	'Kate'),
        'A111'	:	('Rajesh',	'Akash',	'Zade')}

d2 = dict(sorted(dct.items(), key=operator.itemgetter(1)))
print(d2)
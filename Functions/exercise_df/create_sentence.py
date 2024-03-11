subjects = ['He', 'She']
verbs = ['loves', 'hates']
objects = ['TV Serials', 'Netflix']

def create_sent1(sub, ver, obj):
    lst = []
    for i in range(len(sub)):
        for j in range(len(ver)):
            for k in range(len(obj)):
                lst.append(sub[i] + ' ' + ver[j] + ' ' + obj[k])

    return lst

def create_sent2(sub, ver, obj):
    lst = [(sub[i] + ' ' + ver[j] + ' ' + obj[k]) for i in range(len(sub)) for j in range(len(ver)) for k in range(len(obj))]
    lst2 = [(i + ' ' + j + ' ' + k) for i in sub for j in ver for k in obj]

    return lst2

s = create_sent1(subjects, verbs, objects)
print(s)

print()
f = create_sent2(subjects, verbs, objects)
print(f)
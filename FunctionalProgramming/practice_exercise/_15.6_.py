d = {'x': 500, 'y':76387463, 'z': 560}
key_max = max(d.keys(), key=(lambda k: d[k]))
key_min = min(d.keys(), key=(lambda k: d[k]))

print(d[key_max], d[key_min])
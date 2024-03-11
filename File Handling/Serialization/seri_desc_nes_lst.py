# serialize/deserialize a nested list

import json5
lst = [10, [12, 34, 44], [23, 65, 26]]

f = open('nested_list', 'w+')
json5.dump(lst, f)
f.seek(0)

inlofl = json5.load(f)
print(inlofl)
f.close()
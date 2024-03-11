# serialize/deserialize a tuple

import json5
f = open('sampledata1', 'w+')
tpl = ('Akshat', 23, 235465)
json5.dump(tpl, f)
f.seek(0)

intpl = json5.load(f)
print(tuple(intpl))
f.close()

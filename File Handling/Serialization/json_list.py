# converting python data into json format is serialization and json to python is deserialization

# serialize/deserialize a list
import json5
f = open('files/sampledata', 'w+')
lst = [i for i in range(10, 100, 10)]
json5.dump(lst, f)
f.seek(0)

inlist = json5.load(f)
print(inlist)
f.close()

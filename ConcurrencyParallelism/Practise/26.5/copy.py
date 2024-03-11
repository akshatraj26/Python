import shutil, os

files = os.listdir('../26.4')
print(files)
source = os.path.join("../26.4/")
print(source)

source_path = []
for file in files:
    if file.endswith('.txt'):
        source_path.append(os.path.join(source, file))

print(source_path)
destination = r'C:\Users\AkshatRaj\Python\Let Us Python Yashwant Kanetkar\ConcurrencyParallelism\Practise\26.5'
print("Destination :- ", destination)

for s in source_path:
    shutil.copy(s, destination)

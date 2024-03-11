import shutil
import os

d = os.listdir()
print(d)

for i in range(0, len(d)):
    if d[i] == 'move.py' and d[i] == 'Iterator' :
        continue
    else:
        shutil.move(d[i], 'Iterator')
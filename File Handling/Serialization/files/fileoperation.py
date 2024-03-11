import os
import shutil
# os.mkdir('file')

# for i in range(100):
#     # os.mkdir('file'+ str(i))
#     os.rmdir('file' + str(i))
print(os.name)
print(os.getcwd())
print(os.listdir('.'))  # for current directory
print(os.listdir("..")) ## for parent directory

if os.path.exists('mydir'):
    print("mydir already exists")
else:
    os.mkdir('mydir')

os.chdir('mydir')
if os.path.exists('dir1'):
    print("dir already exists")
else:
    os.makedirs(".\\dir1\\dir2\\dir3")


f = open('myfile', 'w')
f.write("Having one child makes you a parents...")
f.write("Having two you are a referee")
f.close()

stats = os.stat('myfile')
print('Size= ', stats.st_size)

# os.removedirs('yourfile')
# os.rename('myfile', 'yourfile')
# shutil.copy('yourfile', 'ourfile')
# os.remove('yourfile')
curpath = os.path.abspath('.')
os.path.join(curpath, 'yourfile')
print(curpath, 'yourfile')

if os.path.isfile(curpath):
    print('your file exists')
else:
    print('yourfile file  dosen\'t exist')

os.listdir()



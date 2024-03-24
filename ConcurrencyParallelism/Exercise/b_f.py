"""
Write a multithreaded program that copies contents of one folder into another. The source and target folder paths
should be input through keyboard.
"""
import threading, sys
import os
import shutil

def copy_file(input_file, output_file):
    shutil.copy(input_file, output_file)
    s = input_file + 'copied\n'
    print(s)


source = sys.argv[1]
target = sys.argv[2]

if not os.path.exists(source):
    print("Source path does not exist")
    exit()

if not os.path.exists(target):
    os.mkdir(target)

os.chdir(source)
lst = os.listdir('.')
tharr = []
for file in lst:
    source_path = source + '\\' + file
    target_path = target + '\\' + file
    th = threading.Thread(target=copy_file, args=(source_path, target_path))
    th.start()
    tharr.append(th)


for th in tharr:
    th.run()




ls = sys.argv
ls = ls[1:]

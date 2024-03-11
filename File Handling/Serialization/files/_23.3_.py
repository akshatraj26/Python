"""
Write a Python program that searches for a file, obtains its size and reports the size in bytes
/KB/MB/GB/ as appropriate.
"""

import os

def convert(num):
    for x in ['bytes', 'KB', 'MB', "GB", 'TB']:
        if num < 1024.0:
            return "%3.1f %s" %(num, x)
        num /= 1024.0

def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert(file_info.st_size)

file_path = r"D:\Russian Movie\Attraction.2.Invasion.2019.BDRip.1.46Gb.MegaPeer.avi"
print(os.stat(file_path).st_size / (1024.0*1024.0* 1024.0))
print(file_size(file_path))
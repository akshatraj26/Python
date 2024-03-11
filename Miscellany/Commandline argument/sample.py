import sys
import shutil
argc = len(sys.argv)
if argc != 3:
    print("Incorrect Usage")
    print("Correct usage: filecopy source target")

else:
    source = sys.argv[0]
    target = sys.argv[1]
    shutil.copy(source, target)
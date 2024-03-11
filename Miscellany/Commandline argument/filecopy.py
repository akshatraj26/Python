"""
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

"""

import sys, getopt
import shutil
argc = len(sys.argv)
if argc == 1:
    print("Incorrect Usage")
    print("Correct usage: filecopy.py -s <source> -t <target>")
    sys.exit()

source = ''
target = ''
try:
    options, arguments = getopt.getopt(sys.argv[1:], 'hs:t:')
    print("Options:-", options)
    print("Arguments:-", arguments)
except getopt.GetoptError:
    print("filecopy.py -s <source> -t <target>")

else:
    for opt, arg in options:
        if opt == '-h':
            print("filecopy.py -s <source> -t <target>")
            sys.exit(2)

        elif opt == '-s':
            source = arg
        elif opt == '-t':
            target = arg

        else:
            print('source file:', source)
            print('target file:', target)
            if source and target:
                shutil.copy(source, target)

# python filecopy.py -s sample.py -t f
# python -h
# python filecopy.py -s phone -t newphone word1 word2


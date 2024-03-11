"""
Write a program using command-line arguments to search for a word in a file and replace it with the specified word.
The usage of the program is shown below.

change -o oldword -n newword -f filename

"""

import sys
import getopt
sys.argv = ['change_b_b.py', '-o', 'Unit', '-n', 'UNIT', '-f', 'syllabus.txt']
if len(sys.argv) != 7:
    print("Incorrect usage")
    print('change -o oldword -n newword -f filename')
    sys.exit(1)

try:
    options, arguments = getopt.getopt(sys.argv[1:], 'ho:n:f')
except getopt.GetoptError as e:
    print("change -o oldword -n newword -f filename ",str(e))
else:
    for opt, arg in options:
        if opt == '-h':
            print('change -o oldword -n newword -f filename')
            sys.exit(2)
        elif opt == '-o':
            oldword = arg

        elif opt == '-n':
            newword = arg

        elif opt == '-f':
            filename = arg
        else:
            print("Oldword :-", oldword)
            print("Newword :-", newword)
            print("Filename :-", filename)
            if oldword and newword and filename:
                f = open(filename, 'r')
                data = f.read()
                f.close()
                data = data.replace(oldword, newword)
                f = open(filename, 'w')
                f.write(data)
                f.close()
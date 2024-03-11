"""
Write a program that display all files in current directory. It can receive option -h or -l or -w from command-line.
If -h is received display help about the program. If -l is received, display files one line at a time. If -w is received,
display  files separated by tab character.
"""
import os, sys, getopt

if len(sys.argv) == 1:
    print(os.listdir('../'))
    sys.exit(1)

try:
    options, arguments = getopt.getopt(sys.argv[1:], 'h|w')
    print("Options:-", options)
    print("Arguments:-", arguments)
    for opt, arg in options:
        print("Opt:-", opt)
        if opt == '-h':
            print("Usage: mydir.py [-h] [-l] [-w]")
            print("-h: Display this help message.")
            print("-l: List files one per line.")
            print("-w: List files separated by tabs.")
            print('User defined help :::: mydir.py -h -l -w')
            sys.exit(2)

        elif opt == '-l':
            lst = os.listdir('../')
            print(*lst, sep='\n')
        elif opt == '-w':
            lst = os.listdir('../')
            print(*lst, sep='\t')

except getopt.GetoptError as e:
    print(e)
    print("mydir.py -h -l -w")

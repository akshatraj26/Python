"""
Write a program to find the range of a set of numbers that are input through the keyboard. Range is the difference
between the smallest and biggest number in the list.
"""
import sys
total = int(input("Enter total no. of numbers:-"))
i = 0
small = sys.maxsize
big = -sys.maxsize
print(small, big)

while i < total:
    n = int(input("Enter a number:- "))
    if n < small:
        small = n
    if n > big:
        big = n
    i += 1


    range = big - small
    print("Range:-", range)
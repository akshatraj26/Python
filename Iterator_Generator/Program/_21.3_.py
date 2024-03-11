"""
Write a program that uses dictionary comprehension to print sin, cos and tan tables for angles ranging  from 0 to 360
in step of 15 degrees. Write generator expressions to find out the maximum value of sin and cos.
"""

import math
pi = 3.14
sine_table = {ang: math.sin(ang * pi/180) for ang in range(0, 360, 15)}
cose_table = {ang: math.cos(ang * pi/180) for ang in range(0, 360, 15)}
tan_table = {ang: math.tan(ang * pi/180) for ang in range(0, 360, 15)}
print(sine_table)
print(cose_table)
print(tan_table)

maxsin = max((math.sin(ang * pi / 180) for ang in range(0, 360, 90)))
maxcos = max((math.cos(ang * pi / 180) for ang in range(0, 360, 90)))
maxtan = max((math.tan(ang * pi / 180) for ang in range(0, 360, 90)))

print(maxsin)
print()
print(maxcos)
print()
print(maxtan)
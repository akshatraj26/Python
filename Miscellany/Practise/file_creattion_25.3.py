"""
Windows stores date of creation of a file as 2-byte number with the following bit distribution.
left most 7 bits: year 1980
middle 4 bits: month
right most 5 bits - day
write a program that converts 9766 into a date 6/1/1999.
"""

dt = 9766
y = (dt >> 9) + 1980
print(y)
m = (dt & 0b111100000) >> 5
print("exp:-", (dt & 0b111100000))
print(m)
d = (dt & 0b11111)
print(0b11111)
print(d)
print(str(d) + '/' + str(m) + '/' + str(y))
"""
Windows stores time of creation of a file as a 2-byte number. Distribution of different bits which account for hours,
minutes and seconds is as follows.
left-most 5 bits: hours
middle 6 bits: minutes
right-most 5 bits - seconds / 2

Write a program to convert time represented by a number 26031 into 12:45:30.
"""
tm = 26031
hr = tm >> 11
print(hr)
min = (tm >> 5) & 0x3F
min = (tm & 0b11111100000) >> 5
print(min)
sec = (tm & 0b11111) * 2
print(sec)

print(str(hr) + ':' + str(min) + ':' + str(sec))

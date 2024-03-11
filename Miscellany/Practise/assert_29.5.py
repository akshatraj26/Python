"""
Write assert statements for the following with suitable messages:
- Salary multiplier sm must be non-zero
- Both p and q are the same type
- Value present in num is part of the lst
- Length of combined string is 45 characters
- Gross salary is in the range 30,000 to 45,000
"""

sm = 45
assert sm != 0


class Sample:
    pass


class NewSample:
    pass


p = Sample()
q = NewSample()
# assert type(p) == type(q), 'Type mismatch'

lst = [34, 56, 23, 67, 23]
num = 33
# assert num in lst, 'num is missing from lst'

s1 = 'A successful marriage requires falling in love many times...'
s2 = 'Always with the same person!'
s = s1 + s2
# assert len(s) <= 45, 'String is too long'

gs = 30000 + 20000 * 15 / 100 + 20000 * 12 / 100
assert gs >= 30000 and gs <= 45000, 'Gross salary is out of range'
"""
Write a program that defines a function pascal_traingle() that displays a Pascal triangle of level received as parameter
to the function. A Pascal's Triangle of level 5 is shown below.
"""


def pascal_triangle(n):
    row = [1]
    z = [0]
    for x in range(n):
        print(row)
        row = [l + r for l, r in zip(row + z, z + row)]


# pascal_triangle(8)


row = [1]
z = [0]
for i in range(5):
    print(row)
    row = [l+r for l,r in zip(row + z, z + row)]


f = zip(row + z, z + row)
print(list(f))

print([l+r for l,r in zip(row+z, z+row)])
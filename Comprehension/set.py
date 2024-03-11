# set comprehension
a = {n**2 for n in range(10)}
print(a)

# delete all number from 20 to 50

print({n for n in a if n < 20 or n > 50})

# look for odd in a set
print({n for n in a if n%2 != 0})

# even
print({n for n in a if n%2 ==0})


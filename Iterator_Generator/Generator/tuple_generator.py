import sys
lst = [i*i for i in range(150)]
gen = (i*i for i in range(150))
print(lst)
print(gen)

# print("Generator:-", list(gen))
print(sys.getsizeof(lst))
print(sys.getsizeof(gen))


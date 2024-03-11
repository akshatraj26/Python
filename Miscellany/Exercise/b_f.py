"""
Write a program to receive a number as input and check whether its 3rd, 6th and 7th bit is on.
"""
def display_bits(n):
    for i in range(7, -1, -1):
        andmask = 1 << i
        k = n & andmask
        print("0", end='') if k==0 else print('0', end='')


num = int(input("Enter a number between 0 and 255:-"))
display_bits(num)
j= num & 0x08
print()
print("Its third bit is off") if j ==0 else print("Its third bit is on")
j = num & 0x40
print("Its sixth bit is off") if j ==0 else print("Its sixth bit is on")
j = num & 0x80
print("Its seventh bit is off") if j ==0 else print("Its seventh bit is on")

# num = 65
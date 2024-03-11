'''

Write a program that receives an integer as input. If a string is entered instead of an integer, then report an error
and give another chance to user to enter na integer. Continue this process till correct input is supplied.

'''

while True:
    try:
        n = int(input("Enter a Number:- "))
        break
    except ValueError:
        print("Incorrect input")

print("You have entered:- ", n)

# n  = input("Enter a number :- ")
# while type(n) == 'int':
#     if isinstance(n, int):
#         print("You have entered:- ", n)




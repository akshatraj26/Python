"""
Write a program that infinitely receives positive integer as input and print its square. If a negative number is entered 
then  raise an exception, display a relevent error message and make a graceful exit.
"""

try:
    while True:
        n = int(input("Enter the Number::"))
        if n >= 0:
            print( n * n)
            
        else:
            raise ValueError('Negative Number')
except ValueError as e:
    print(e.args)
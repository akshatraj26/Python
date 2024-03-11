"""
Write a program to calculate factorial values of numbers in the range 10 to 15. Log the results into a file.
"""
import logging
logging.basicConfig(level=logging.INFO,
                    filename='factorial.log',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

d = 1

for j in range(10, 15):
    for i in range(1, j):
        d *= i

    logging.info(f"Factorial of {j} is {d}")
    d = 1









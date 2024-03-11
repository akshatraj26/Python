"""
Write a program to read name, age, salary of 5 persons from keyboard. Log the data into a file 'mylog.log' in the
following format, along with any erroneous data entered by the user:

"""

import logging
logging.basicConfig(level=logging.INFO,
                    filename='mylog.log',
                    filemode='w',
                    format='%(asctime)s - %(message)s')

for num in range(5):
    data = input("Enter the Name, Age and Salary:").split()
    try:
        name = data[0]
        age = int(data[1])
        salary = float(data[2])
        logging.info(f"Correct data: {name} {age} {salary}")
    except ValueError as e:
        logging.exception('ValueError')
"""
Write a program that has two modules main and function. The function module should define a function squareroot_square_cube
. This function should receive a number as an argument, obtain its square and cube values and log them. This function
should be called from main modules foe values in the range of 0 to 9 and log them calls into a separate log file.
"""

import logging
import math

# create a logger and setLevel
logger2 = logging.getLogger(__name__)
logger2.setLevel(logging.INFO)

# configure handler and formatter for logger2
handler2 = logging.FileHandler(f"{__name__}.log", mode='w')
formatter2 = logging.Formatter("%(name)s %(levelname)s %(message)s")

# add formatter to handler
handler2.setFormatter(formatter2)

# add handler to logger
logger2.addHandler(handler2)

logger2.info(f"Logs for module {__name__}")

def squareroot_square_cube(num):
    root = math.sqrt(num)
    sqr = num * num
    cube = num ** 3
    logger2.info(f"Result: {num} {round(root, 4)} {sqr} {cube}")
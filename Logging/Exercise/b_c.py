"""
How will you log the values  of variable rollno, name, age at the INFO level on the console.?
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)

data = input("Enter rollno, name, age:-").split()
roll = data[0]
name = data[1]
age = data[2]
logger.info(f"Console message by {__name__} and {roll}, {name}, {age}")
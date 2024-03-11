"""
Write a program that infinitely generates 500 random numbers, in the range 100 to 200, one every half a second.
Log the numbers generated into rollover log files. Rollover should happen every 4 seconds and a maximum of 5 log files
should get created. Terminates the program if the user hits Ctrl + C in the middle of random number generation and
log that as a warning.
"""

import time
import logging
from logging import handlers as h
import random


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = h.TimedRotatingFileHandler('rollover.log',
                                                    when= 'S',
                                                    interval=4,
                                                    backupCount=5)


formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

try:
    while True:
        time.sleep(0.4)
        number = random.randint(100, 200)
        logger.debug('A debug message')
        logger.info(f"Printing {number}")
        logger.error(f"An Error message")
        logger.warning(f"If use hit ctrl + c then I will stop")
        logger.critical(f"Don't ignore me")
except KeyboardInterrupt as e:
    logger.warning('Stopped by the user')



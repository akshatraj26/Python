"""
Write a program that logs messages to consoles as well as a file 'myapp.log'. Messages including and above ERROR level
should be logged to the console. Messages including and above DEBUG level should be logged to the file.
"""
import logging

# create logger and set level
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('myapp.log')
fh.setLevel(logging.DEBUG)

# create console handler with higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create a formatter and add it to the handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)


# add the handler to logger
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('A DEBUG message')
logger.info('A info message')
logger.error('An Error message')
logger.warning('A warning message')
logger.critical('A message of critical severity')

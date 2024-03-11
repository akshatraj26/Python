import logging
logging.basicConfig(level=logging.INFO,
                    filename='time_stamp.log',
                    filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')
logging.debug('A debug message')
logging.info('An information')
logging.warning('A warning message')
logging.error('An error message')
logging.critical('A message of critical severity')


f = open('time_stamp.log', 'r')
data = f.read()
print(data)

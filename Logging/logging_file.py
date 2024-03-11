import logging
logging.basicConfig(level=logging.INFO,
                    filemode='a',
                    filename='mylog.log')
logging.debug('A debug message')
logging.info('An information')
logging.warning('An warning message')
logging.error('An error message')
logging.critical('An critical message')
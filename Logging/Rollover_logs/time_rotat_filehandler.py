import time
import logging
from logging import handlers as h

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = h.TimedRotatingFileHandler('mylog.log', when='S',
                                     interval=5, backupCount=6)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

try:
    for num in range(50):
        time.sleep(0.5)
        logger.debug(f'num = {num}')
        logger.info(f'num - {num}')
        logger.error(f'num - {num}')
        logger.warning(f"num - {num}")
        logger.critical(f"num - {num}")
except KeyboardInterrupt:
    # handle ctr + c
    logging.warning("Cancelled by user")

except Exception as e:
    # handle unexpected errors
    logging.exception(f"Unhandled Error\n{e}")

finally:
    # stop  logging activity
    logging.shutdown()
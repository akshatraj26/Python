import logging

# create a logger and set logging level
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

def division(num, den):
    try:
        val = num / den
        logger2.info(f'division result: {val}')
    except ZeroDivisionError as e:
        logger2.exception('ZeroDivisionError')

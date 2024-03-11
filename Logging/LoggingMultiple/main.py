import logging
import function

# create logger and set logging level
logger1 = logging.getLogger(__name__)
logger1.setLevel(logging.INFO)

# configure handler and formatter
handler1 = logging.FileHandler(f"{__name__}.log", mode='w')
formatter1 = logging.Formatter("%(name)s %(levelname)s %(message)s")

# add formatter to the handler
handler1.setFormatter(formatter1)

# add handler to the loger
logger1.addHandler(handler1)

logger1.info(f"Logs for module {__name__}")

num_vals = [21, 3, 60, 32, 14]
den_vals = [3, 2, 0, 6, 7]

for num, den in zip(num_vals, den_vals):
    function.division(num, den)
    logger1.info(f"Call division with args {num} and {den}")
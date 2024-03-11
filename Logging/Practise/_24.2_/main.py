import logging
import function

# create logger and set logging level
logger1 = logging.getLogger(__name__)
logger1.setLevel(logging.INFO)

# configure handler and formatter
handler1 = logging.FileHandler(f"{__name__}.log", mode='w')
formatter1 = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

# add formatter to the handler
handler1.setFormatter(formatter1)

# add handler to the logger
logger1.addHandler(handler1)

logger1.info(f"Logs for module {__name__}")

for num in range(9):
    function.squareroot_square_cube(num)
    logger1.info(f"Call square_root_cube with arg {num} ")

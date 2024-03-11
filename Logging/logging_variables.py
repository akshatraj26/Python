import logging
logging.basicConfig(level=logging.INFO,
                    filename='variable_logging.log',
                    filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")
num_vals = [21, 32, 60, 32, 14]
den_vals = [3, 2, 0, 16, 0]
for num, den in zip(num_vals, den_vals):
    logging.info(f"The values of num and den are {num} and {den}")
    try:
        val = num / den
        logging.info(f'division successful with result: {val}')
    except ZeroDivisionError as er:
        logging.exception('ZeroDivisionError')

f = open('variable_logging.log', 'r')
data = f.read()
print(data)

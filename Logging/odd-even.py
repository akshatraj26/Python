import logging
f = [23, 34, 56, 22, 45, 667, -234, 45, 423]

logging.basicConfig(level=logging.INFO,
                    filename='even_odd.log',
                    filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")

for i in f:
    try:
        if i % 2 == 0:
            logging.info(f"this number {i} is divisible by 2")
        else:
            logging.info(f"this number {i} is not divisible by 2 means odd number.")

    except Exception as e:
        logging.exception(e)

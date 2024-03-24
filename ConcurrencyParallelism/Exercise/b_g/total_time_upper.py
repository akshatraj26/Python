import threading
import os
import sys
import time
import logging


logging.basicConfig(level=logging.ERROR, filename='error.log',
                    filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")

start = time.time()
lst = sys.argv
lst = lst[1:]

for file in lst:
    f = open(file, 'r')
    data = f.read()
    data = data.upper()
    logging.info(f"data: {data}")

    if data == '':
        break
    time.sleep(0.5)
    target = ['aa.txt', 'bb.txt', 'cc.txt']
    for tar in target:
        f = open(tar, 'w')
        logging.error(f"Error for the data variable :- {data}")
        f.write(data)



end = time.time()
print("Total Time:- ", end - start, 'seconds.')
# It took 0.014001607894897461 seconds
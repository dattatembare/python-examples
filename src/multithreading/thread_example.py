# A thread stops when :
#
# run() method terminates normally. [or]
# an unhandled exception causes run() method to terminate abruptly.

import logging
import threading
import time
from time import sleep

logging.getLogger()


def execute(val):
    print(f'Executing thread..{val}')


for i in range(3):
    # t = threading.Thread(target=execute, args=(i,), name=f'Thread# {i}')  # This works
    t = threading.Thread(target=execute(i), name=f'Thread# {i}')  # This works too
    t.start()
    if i == 1:
        print(time.ctime(), t.is_alive(), t.name)
        sleep(5)
    print(time.ctime(), t.is_alive(), t.name)

# Result:
# Executing thread..0
# Wed Aug  7 16:24:52 2019 False Thread# 0
# Executing thread..1
# Wed Aug  7 16:24:52 2019 False Thread# 1
# Wed Aug  7 16:24:57 2019 False Thread# 1
# Executing thread..2
# Wed Aug  7 16:24:57 2019 False Thread# 2

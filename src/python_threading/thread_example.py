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

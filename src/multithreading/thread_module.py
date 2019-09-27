import time


# import thread  # python 2, depricated in python 3 use threading


# Define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{threadName} : {time.ctime(time.time())}")


# Create two threads as follows
try:
    print('Create new threads')
    # thread.start_new_thread(print_time, ("Thread-1", 2,))
    # thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: unable to start thread")

while 1:
    pass

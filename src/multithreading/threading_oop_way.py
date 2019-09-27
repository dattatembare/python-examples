import threading
import time

threadLock = threading.Lock()
threads = []


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)  # TODO check why need this
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print(f"Starting - {self.name}")
        # Get lock to synchronize threads
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print(f"{thread_name}:{time.ctime(time.time())}")
        counter -= 1


# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete, The join() waits for threads to terminate.
for t in threads:
    t.join()
print("Exiting Main Thread")

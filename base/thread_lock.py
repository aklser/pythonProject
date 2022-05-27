import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self) -> None:
        print("start thread:" + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 1)
        threadLock.release()


def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print(f"{threadName}:{time.ctime(time.time())}")
        counter -= 1


threadLock = threading.Lock()
threads = []
thread1 = myThread(1, "thread-1", 10)
thread2 = myThread(2, "thread-2", 3)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)
for i in threads:
    i.join()
print("exit!")

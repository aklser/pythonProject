import threading
import time

# exitFlag = 0


def print_time(threadName, delay, counter):
    while counter:
        # if exitFlag:
        #     threadName.exit()
        time.sleep(delay)
        print(f"{threadName}:{time.ctime(time.time())}")
        counter -= 1


class myTread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print(f"开始线程：{self.name}")
        print_time(self.name, self.delay, 10)
        print(f"结束线程：{self.name}")


thread1 = myTread(1, "tread-1", 1)
thread2 = myTread(2, "tread-2", 1)
thread1.start()
thread2.start()
# thread1.join()
# thread2.join()
for i in range(5):
    print(threading.current_thread().getName())

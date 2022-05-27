import threading
import queue
import time

exit_flag = 0


class my_thread(threading.Thread):
    def __init__(self, thread_id, name, que):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.que = que

    def run(self) -> None:
        print("start:" + self.name)
        process_data(self.name, self.que)
        print("end:" + self.name)


def process_data(thread_name, que):
    while not exit_flag:
        queueLock.acquire()
        if not workQueue.empty():
            data = que.get()
            queueLock.release()
            print(f"{thread_name}:processing:{data}")
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["thread-1", "thread-2", "thread-3", "thread-4"]
nameList = ["one", "two", "three", "four", "five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1
for t_name in threadList:
    thread = my_thread(threadID, t_name, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass
exit_flag = 1
for t in threads:
    t.join()
print("exit main!")

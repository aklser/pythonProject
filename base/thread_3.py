import queue
import time
import threading

q = queue.Queue(3)


def product(name):
    count = 1
    while True:
        q.put(f"气球兵-{count}")
        print(f"{name}训练气球兵-{count}")
        count += 1
        time.sleep(1)


def consume(name):
    while True:
        print(f"{name}使用了{q.get()}")
        time.sleep(6)
        q.task_done()


t1 = threading.Thread(target=product, args=("p-1",))
t2 = threading.Thread(target=consume, args=("c-1",))
t3 = threading.Thread(target=consume, args=("c-2",))
t1.start()
t2.start()
t3.start()

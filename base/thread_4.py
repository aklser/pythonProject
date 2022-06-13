from threading import Thread
from time import sleep


def threadFunc(arg1, arg2):
    print("start")
    print(f"arg:{arg1},{arg2}")
    sleep(5)
    print("end")


thread = Thread(
    target=threadFunc,
    args=("1", "2")
)
thread1 = Thread(
    target=threadFunc,
    args=("2-1", "2-2")
)

thread.start()
thread1.start()
thread.join()
thread1.join()
print("all end")

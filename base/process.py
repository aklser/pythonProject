import os
import time
from multiprocessing import Process, Array, Manager


def func(name, data, all_data):
    all_data[0] = data
    print(name)
    print(all_data[0])
    print("子：", os.getpid())
    print("父：", os.getppid())
    print(name)
    time.sleep(3)


if __name__ == "__main__":
    all_data = Array("i", 1)
    p = Process(target=func, args=("!!!!!!!!!", 21, all_data))
    p1 = Process(target=func, args=("!!!!!!!!!", 21, all_data))
    p.start()
    p1.start()
    p.join()
    p1.join()
    print("主：", os.getpid(), all_data[0])

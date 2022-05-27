import threading


def action(*add):
    for item in add:
        print(threading.current_thread().getName() + "" + item)


my_tuple = ("item_1", "item_2", "item_3")
thread_my = threading.Thread(target=action, args=my_tuple)
thread_my.start()

for i in range(5):
    print(threading.current_thread().getName())

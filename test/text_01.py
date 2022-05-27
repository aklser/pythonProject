import random
import re
import datetime

# m = re.search('[0-9]{2}', 'adas32dsf35dfa')
# print(m.group(0))
# n = re.match('[a-zA-Z]{2,3}', 'asf')
# print(n)

#######################################
# output_1981.10.21.txt   to  output_1981-10-21-3.txt
# a = "output_1981.10.21.txt"
# b = re.sub("\.(?=[0-9])", "-", a)
# d = re.split(r"-|\.|_", b)
# c = datetime.datetime(int(d[1]), int(d[2]), int(d[3]))
# e = re.sub("(?=\.)", "-" + str(c.weekday() + 1), b)
# print(e)
######################################

# import  time
# # print("start")
# # time.sleep(10)
# # print("end")
# st = time.gmtime()
# print(st)
# stru = time.localtime()
# print(stru)
# structt = time.mktime(stru)
# print(structt)
# import datetime
#
# t = datetime.datetime(2012, 2, 3, 21, 32)
# s = datetime.datetime(2021,2,4,12,32)
# deltal1 = datetime.timedelta(seconds=500)
# deltal2 =datetime.timedelta(weeks=3)
# print(t + deltal1)
# print(s + deltal2)
# print(s > t)
#
# from datetime import datetime
#
# format = "output_%Y.%m.%d.txt"
# str = "output_1981.10.21.txt"
# t = datetime.strptime(str, format)
# print(t)
# print(t.strftime(format))
# import os.path
#
# path = '/home'
#
# print(os.path.basename(path))
# print(os.path.dirname(path))
# info = os.path.split(path)
# print(info)
# path2 = os.path.join("/", 'home', 'doc')
# import os, shutil
#
# shutil.copy("a,txt", "b.txt"
from itertools import repeat

import math

# random.seed()
# b = random.choice(range(10))
# print(b)
# b = random.sample(range(10), 10)
# print(b)
# c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# random.shuffle(c)
# print(c)
# # print(random.random())
# # print(random.uniform(1, 43))
# # print(random.gauss(12, 122))
#
# every_one = ["asd", "asddqwq", "qwfewv", "qwde"]
# random.shuffle(every_one)
# for i, name in enumerate(every_one):
#     print(i, ":" + name)


a = random.sample(range(1, 23), 5)
print(a)
b = random.choice(range(1, 7))
c = ""
for i in range(8):
    c += str(random.choice(range(1, 7)))
print(int(c))


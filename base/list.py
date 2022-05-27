my_list = ["asd", 12, [], "ad"]

print(my_list[0:2])
print(my_list[:2])
print(my_list[1:])
print(my_list[:-1])
print(type(my_list))
my_list += [123, 1314, 124]
print(my_list)

my_list.append("qwer")
print(my_list)

my_list.extend(["end"])
print(my_list)

my_list.insert(0, "start")
print(my_list)

print(my_list.count("end"))

print("end" in my_list)

print(my_list.index("end"))

print(len(my_list))

try:
    print(my_list.index("asfasfda"))
except:
    print("error")

my_list.remove("qwer")
print(my_list)

del my_list[1]
print(my_list)

my_list.pop()
print(my_list)

from collections import deque

que = deque(["qw", "er", "ty"])
que.popleft()
print(que)
print(list(map(lambda x: x ** x, range(1, 6))))
print([x * 2 for x in range(12)])
print(list(["1", 123]))
print((1, 2, 3, 4) < (1, 2, 4))

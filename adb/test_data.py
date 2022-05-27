import random
from collections import Counter

def random_data():
    data1 = [
        ["第一", 1, 1],
        ["第二", 2, 2],
        ["第三", 1, 4],
        ["第四", 2, 8]
    ]
    n = 0
    for i in data1:
        n += i[2]
    an = random.randint(1, n)
    # print(an)
    for i in range(len(data1)):
        an -= data1[i][2]
        if an <= 0:
            an = i
            break
    return data1[an][0]


answer = []
for i in range(10000):
    answer.append(random_data())
print(answer)
answer_a = dict(Counter(answer))
print(answer_a)
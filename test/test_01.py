from functools import reduce

import main


class sublist(list):
    def __sub__(self, other):
        self_list = self[:]
        other_list = other[:]
        while len(other_list):
            now_pop = other_list.pop()
            if now_pop in self_list:
                self_list.remove(now_pop)
        return self_list


def func(**dict):
    print(dict)
    return dict


def func1(*dict):
    print(dict)


def gen():
    a = 100
    yield a
    a = a * 8
    yield a
    yield 100000


def gen1():
    for i in range(4):
        yield i


if __name__ == "__main__":
    pass
    # print(list(filter(lambda a: True if a > 10 else False, [10, 34, 346, 3, 56])))
    # funcl = lambda x, y: x + y
    # print(funcl(3, 43))
    # a = [1, 324, 634, 7]
    # remap = list(map(lambda x: x + 3, a))
    # print(remap)
    # print(reduce(lambda x, y: x + y, [12, 2, 8, 7]))
    # x1 = [1, 3, 5]
    # y1 = [9, 12, 432]
    # L = [x ** 2 for (x, y) in zip(x1, y1) if y > 10]
    # print(L)
    # for i in gen():
    #     print(i)
    # print(list(x for x in range(4)))

# users = {'a': 'aa', 'b': 'bb', 'c': 'cc'}
# f = open('test.txt', 'r')
# content = f.readlines()
# for a in content:
#     print(a)
# print(content)
# print(type(content))
# f.close()
# print(main.a())
# print(func(a=1, b=1, c=3, d=4))
# args = (1, 2, 4)
# print(func1(*args))
# S = 'asdfvd31d3'
# for i in range(0, len(S), 2):
#     print(S[i])
# print(enumerate(S))
# for k,v in enumerate(S):
#     print(k,v)
# ta = [1, 3, 5]
# tb = [7, 8, 9]
# tc = ['a', 'b', 'c']
# a = zip(ta, tb, tc)
# print(a)
# na, nb, nc = zip(*a)
# print(na, nb, nc)

# for (a, b, c) in zip(ta, tb, tc):
#     print(a, b, c)

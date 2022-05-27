# class Student(object):
#     __slots__ = ("study", "name")
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
#     __repr__ = __str__
#
#
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 1000:
#             raise StopIteration()
#         return self.a
#
#     def __getitem__(self, item):
#         a, b = 1, 1
#         if isinstance(item, int):
#             for x in range(item):
#                 a, b = b, a + b
#             return a
#         if isinstance(item, slice):
#             start = item.start
#             stop = item.stop
#             if start is None:
#                 start = 0
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a+b
#             return L
# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
import enum
from enum import Enum


def a():
    print('a')
    return 0


# num =enum.Enum('num', ("11", "21", "31", "41", "51", "61", "71", "81", "91", "01"))
@enum.unique
class weekday(Enum):
    Sun = 1
    Mon = 2
    Tue = 3
    Web = 4
    Thu = 5
    Fri = 6
    Sat = 7


if __name__ == '__main__':
    pass
    # print(Student("sad"))
    # for n in Fib():
    #     print(n)
    # f = Fib()
    # print(f[5])
    # print(f[2:4])
    # print(Chain().a.da.da.a)
    # for n, member in num.__members__.items():
    #     print(n, "->", member, ",", member.value)
    # for name, member in weekday.__members__.items():
    #     print(name, "-》", member, member.value)
    # print(weekday.Web)

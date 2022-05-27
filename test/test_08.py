from sys import getrefcount

if __name__ == "__main__":
    # a = 1234567890132456789
    # b = 1234567890132456789
    # print(a is b)
    # c = "very good morning"
    # d = 'very good morning'
    # print(c is d)
    # e = []
    # f = []
    # print(e is f)
    # m = 11289
    # a = [1, 2, 3]
    # print(getrefcount(m))
    # print(getrefcount(a))
    # n = m
    # print(getrefcount(n))
    # b = [a, a]
    # print(getrefcount(b))
    # c = a
    # print(getrefcount(a))
    # print(getrefcount(c))
    # del c
    # print(getrefcount(a))
    #
    import  gc
    # print(gc.get_threshold())
    # gc.collect()
    # a = [12, 314]
    #
    # a.append(a)
    # print(a[2])
    # print(getrefcount(a))
    # print(getrefcount(c))
    #
    # class from_obj(object):
    #     def __init__(self, to_obj):
    #         self.to_obj = to_obj
    #
    #
    # b = [1, 2, 3]
    # a = from_obj(b)
    # print(id(a.to_obj))
    # print(id(b))
    # print(globals())

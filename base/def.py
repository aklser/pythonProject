def a(i, s=[]):
    s.append(i)
    return s


def b(i, s=None):
    if s is None:
        s = []
    s.append(i)
    return s


def c(n, *m, **l):
    print(n)
    for i in m:
        print(i)
    for i in l:
        print(l[i])


def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)


def foo(name, **kwargs):
    return "name" in kwargs


def fo(name, /, **kwargs):
    return "name" in kwargs


print(a(1))
print(a(2))
print(a(3))
print(b(1))
print(b(2))
print(b(3))
n = []
print(b(1, n))
print(b(2, n))
print(b(3, n))
print("**********" * 2)
c(1, 23, 23, 6456, 45, j=2, k=123)
f(1, 2, 3, kwd1=4, kwd2=5)
print(foo(1, **{"nam": 2}))
print(fo(1, **{"name": 2}))

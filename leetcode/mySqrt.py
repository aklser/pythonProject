def mySqrt(x: int) -> int:
    # a = 0
    # for i in range(1, x // 2 + 2):
    #     if i * i <= x:
    #         a = i
    #     else:
    #         break
    # return a
    if x <= 1:
        return x
    r = x
    c = x / r
    while r > c:
        r = (r + c) // 2
        c = x / r
    return int(r)


print(mySqrt(1))
print(mySqrt(2))
print(mySqrt(3))
print(mySqrt(4))
print(mySqrt(2147395599))

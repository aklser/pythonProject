def addBinary(a: str, b: str) -> str:
    # a = int(a)
    # b = int(b)
    # c = [int(i) for i in str(a + b)]
    # d = ""
    # for i in range(len(c) - 1, -1, -1):
    #     if c[i] > 1:
    #         c[i] = c[i] % 2
    #         if i - 1 < 0:
    #             c.insert(0, 1)
    #         else:
    #             c[i - 1] += 1
    #
    # for i in c:
    #     d += str(i)
    # return d

    # return bin(int(a, 2) + int(b, 2))[2:]
    return a+b

a_bit = "1010"
b_bit = "1011"
print(addBinary(a_bit, b_bit))
print(type(addBinary(a_bit, b_bit)))

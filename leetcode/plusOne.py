from typing import List


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    # result = ""
    # for i in digits:
    #     result += str(i)
    # result = int(result) + 1
    # return [int(i) for i in str(result)]

    n = len(digits)
    for i in range(n - 1, -1, -1):
        digits[i] += 1
        digits[i] %= 10
        if digits[i]:
            return digits
    a = [0 for i in range(n + 1)]
    a[0] = 1
    return a


a = [1, 9, 9]
print(plusOne(a))


print(10 % 10)
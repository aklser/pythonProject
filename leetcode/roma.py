# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        s_reverse = s[::-1]
        result = 0
        last = 0
        now = 0
        sta = 1
        a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for s in s_reverse:
            now = a[s]
            if now > last:
                sta = 1
                result += now
                last = now
            elif now == last:

                result += sta * now
                last = now
            else:
                sta = -1
                result += -now
                last = now

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("IIV"))

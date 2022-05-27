from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []
        for i in range(numRows):
            if i == 0:
                a.append([1])
            elif i == 1:
                a.append([1, 1])
            else:
                b = []
                for m in range(i - 1):
                    b.append(a[i - 1][m] + a[i - 1][m + 1])
                a.append([1, *b, 1])
        return a

    def getRow(self, rowIndex: int) -> List[int]:
        a = 1
        res = []
        for i in range(rowIndex):
            res.append(a)
            a = int(a * (rowIndex-1 - i) / (i + 1))
        return res


answer = Solution().generate(5)
answer2 = Solution().getRow(5)
print(answer)
print(answer2)

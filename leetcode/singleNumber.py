from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a = a ^ i
        return a


n = Solution().singleNumber([2, 2, 1])
print(n)

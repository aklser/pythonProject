from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = [0] * (len(nums) + 1)
        print(a)
        for i in nums:
            a[i] = 1
        for i in range(len(a)):
            if a[i] == 0:
                return i


print(Solution().missingNumber([3, 0, 1]))

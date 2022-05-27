from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if a == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    a = nums[i]
                    count = 1
        return a


print(Solution().majorityElement([1, 23, 4, 1, 1]))

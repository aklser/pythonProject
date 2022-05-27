from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = {}
        for i in range(len(nums)):
            if a.get(nums[i]) is not None and abs(a[nums[i]] - i) <= k:
                return True
            else:
                a[nums[i]] = i
        return False


a = Solution().containsNearbyDuplicate([1, 2, 4, 5, 1], 4)
print(a)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_n, max_res = prices[0], 0
        for i in range(1, len(prices)):
            max_res = max(max_res, prices[i] - min_n)
            min_n = min(min_n, prices[i])
        return max_res


num = Solution().maxProfit([2, 4, 1, 2])
print(num)

class Solution:
    def climbStairs(self, n):
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # a, b, c = 1, 2, 0
        # for i in range(3, n + 1):
        #     c = a
        #     a = b
        #     b = c + a
        # return b
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else n


sol = Solution().climbStairs(6)
print(sol)
# 1 2 3 5 8 13
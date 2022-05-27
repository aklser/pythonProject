class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

print(Solution().canWinNim(9))
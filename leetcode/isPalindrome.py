class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        b = ""
        for i in s:
            if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
                b = b + i.lower()
            if 48 <= ord(i) <= 57:
                b = b + i
        if len(b) == 0:
            return True
        for n in range(len(b) // 2 + 1):
            if b[n] != b[-(n + 1)]:
                return False
        return True


a = Solution().isPalindrome("0P")

print(a)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = [i for i in pattern]
        b = s.split()
        if len(a) != len(b) or len(set(a)) != len(set(b)):
            return False
        c = {}
        for i in range(len(pattern)):
            if c.get(pattern[i]):
                if c[pattern[i]] != b[i]:
                    return False
            else:
                c[pattern[i]] = b[i]
        return True


# "aba"
# "cat cat cat dog"
print(Solution().wordPattern("abba", "dog dog dog dog"))

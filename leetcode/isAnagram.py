class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        for i in s:
            if a.get(i):
                a[i] += 1
            else:
                a[i] = 1
        for i in t:
            if a.get(i):
                a[i] -= 1
                if a[i] < 0:
                    return False
            else:
                return False
        return True

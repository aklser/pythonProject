def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s1[:i]
    return s1


if __name__ == "__main__":
    print(longestCommonPrefix(["asdad", "asdffffff", "aasdass"]))
    a = list(map(set, zip(*["asdad", "asdffffff", "aasdass"])))
    print(a)
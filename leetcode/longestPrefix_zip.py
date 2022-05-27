def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    a = list(map(set, zip(*strs)))
    result = ""
    for i, x in enumerate(a):
        x = list(x)
        if len(x) > 1:
            break
        result += x[0]

    return result


if __name__ == "__main__":
    print(longestCommonPrefix(["asdad", "asdffffff", "asasdass"]))

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    # for i in s.split(" ")[::-1]:
    #     print(i)
    #     if i != "":
    #         return len(i)
    return len(s.strip(" ").split(" ")[-1])


s = "   luffy is still  joyboy  "
print(lengthOfLastWord(s))

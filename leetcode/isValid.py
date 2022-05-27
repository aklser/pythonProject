def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 == 0:
        while "{}" in s or "[]" in s or "()" in s:
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "")
        return s == ""
    else:
        return False


if __name__ == "__main__":
    print(isValid("[]{{}{}"))

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    st = []
    for item in s:
        if item == "(":
            st.append(")")
        elif item == "[":
            st.append("]")
        elif item == "{":
            st.append("}")
        elif not st or st[-1] != item:
            return False
        else:
            st.pop()
    return True if not st else False


if __name__ == "__main__":
    print(isValid("[{]}{}"))

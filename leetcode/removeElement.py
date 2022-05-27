def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k, nums


if __name__ == '__main__':
    num = [12, 4, 6, 64, 54745, 64, 64]
    v = 64
    print(removeElement(num, v))

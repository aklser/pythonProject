def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])
    return max(nums), nums
    # for i in range(1, len(nums)):
    #     nums[i] = nums[i] + max(nums[i - 1], 0)
    # return max(nums)


print(maxSubArray([1, -132, 213, -23, 111, -12133]))
#                   [1, -131, 213, 190, 301, -11832]

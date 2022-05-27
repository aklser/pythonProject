def a(nums):
    i = 0
    for l in range(len(nums)):
        # print("******")
        # print(nums[l])
        # print(l)
        # print(nums[i])
        # print(i)
        if nums[l] != nums[i]:
            nums[i + 1] = nums[l]
            i += 1
    return i + 1,nums, nums[:2]


if __name__ == '__main__':
    nums = [1, 1, 1, 2]
    print(a(nums))

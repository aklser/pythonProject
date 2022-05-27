from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    i = len(nums)
    if i == 0:
        return 0
    i = i - 1
    if nums[0] >= target:
        return 0
    if nums[i] < target:
        return i + 1
    elif nums[i] == target:
        return i
    min_num = 0
    max_num = i
    i = round((len(nums) - 1) / 2)

    while True:

        if nums[i] == target:
            return i
        elif nums[i] < target:
            if nums[i + 1] >= target:
                return i + 1
            min_num = i
            i = round((i + max_num) / 2)
        elif nums[i] > target:
            if nums[i - 1] == target:
                return i - 1
            elif nums[i - 1] < target:
                return i
            max_num = i
            i = round((min_num + i) / 2)


print(searchInsert([1, 2], 1309))

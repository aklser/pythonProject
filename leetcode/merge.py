from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m + n - 1
    while n > 0:
        if m <= 0 or nums1[m - 1] <= nums2[n - 1]:
            n -= 1
            nums1[i] = nums2[n]
            i -= 1
        else:
            m -= 1
            nums1[i] = nums1[m]
            i -= 1

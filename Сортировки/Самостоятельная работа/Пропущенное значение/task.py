from typing import List


def missing_number(nums: List[int]) -> int:
    min_ = 0
    max_ = len(nums)
    for i in range(min_, max_):
        if i not in nums:
            return i
    return max_

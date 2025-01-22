from typing import List


def majority_element(nums: List[int]) -> int:
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

nums = [3,2,2,2,2,3,5,6,3]
print(majority_element(nums))

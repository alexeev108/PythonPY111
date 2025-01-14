from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    ...
    list_ = [target - el for el in nums]
    for i, v in enumerate(nums):
        if v in list_ and list_.index(v) != i:
            return [i, list_.index(v)]

if __name__ == '__main__':
    data = [1, 2, 3, 7, 5]
    print(two_sum(data, 6))
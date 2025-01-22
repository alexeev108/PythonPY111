from typing import List


def maximum_gap(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    container_lenght = len(nums)
    for el in range(container_lenght):
        for el_2 in range(0, container_lenght - el - 1):
            if nums[el_2] > nums[el_2 + 1]:
                nums[el_2], nums[el_2 + 1] = nums[el_2 + 1], nums[el_2]

    max_ = 0
    for i in range(1, len(nums)):
        max_ = max(max_, nums[i] - nums[i - 1])
    return max_

if __name__ == '__main__':
    data = [3,6,9,1]
    print(maximum_gap(data))
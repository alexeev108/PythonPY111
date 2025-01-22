from typing import List


def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    """
    container_lenght = len(nums)
    for el in range(container_lenght):
        for el_2 in range(0, container_lenght - el - 1):
            if nums[el_2] > nums[el_2 + 1]:
                nums[el_2], nums[el_2 + 1] = nums[el_2 + 1], nums[el_2]

# if __name__ == '__main__':
#     data = [2, 2, 2, 1, 1, 0, 0, 0]
#     print(sort_сolors(data))
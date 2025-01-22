import random
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализуйте сортировку слиянием
    if len(container) > 1:
        mid = len(container) // 2
        left_list = sort(container[:mid])
        right_list = sort(container[mid:])
        left_index, right_index, container_index = 0, 0, 0
        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] <= right_list[right_index]:
                container[container_index] = left_list[left_index]
                left_index += 1
            else:
                container[container_index] = right_list[right_index]
                right_index += 1
            container_index += 1
        while right_index < len(right_list):
            container[container_index] = right_list[right_index]
            right_index += 1
            container_index += 1
        while left_index < len(left_list):
            container[container_index] = left_list[left_index]
            left_index += 1
            container_index += 1
    return container

if __name__ == '__main__':
    data = [random.randrange(-50, 50) for _ in range(50)]
    print(sort(data))
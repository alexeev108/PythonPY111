"""
This module implements some functions based on linear search algo
"""
import random
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # TODO реализовать итеративный линейный поиск

    if not all(map(lambda x: isinstance(x, int), arr)):
        raise TypeError
    if not arr:
        raise ValueError

    min_el = sorted(arr)[0]
    for pos, el in enumerate(arr):
        if el == min_el:
            return pos


if __name__ == '__main__':
    # data = [-10, -9, 0]
    # data = [0, 1, 2, 3]
    # data = [i for i in range(3, 10)] + [1]
    # data = [i for i in range(10, -3, -1)]
    data = [random.randint(-100, 100) for _ in range(300)]
    print(data)
    print(min_search(data))
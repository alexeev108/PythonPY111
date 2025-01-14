import random
from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать итеративный алгоритм бинарного поиска
    left_border = 0
    right_border = len(seq) - 1

    if not all(map(lambda x: isinstance(x, int), seq)):
        raise TypeError

    while left_border <= right_border:
        mid = (right_border + left_border) // 2
        if value == seq[mid]:
            while 0 < mid < len(seq) and seq[mid - 1] == value:
                mid -= 1
            return mid
        elif value > seq[mid]:
            left_border = mid + 1
        else:
            right_border = mid - 1
    raise ValueError(f'Элемент {value} не найден')

if __name__ == '__main__':
    data = [random.randint(1, 7) for _ in range(20)]
    data.sort()
    print(data)
    print(binary_search(5, data))

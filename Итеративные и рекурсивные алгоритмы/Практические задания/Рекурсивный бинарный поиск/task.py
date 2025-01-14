import random
from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать алгоритм бинарного поиска
    if not all(map(lambda x: isinstance(x, int), seq)):
        raise TypeError
    if not right_border:
        right_border = len(seq) - 1
    if right_border < left_border:
        raise ValueError
    mid = (right_border + left_border) // 2
    if value == seq[mid]:
        while 0 < mid < len(seq) and seq[mid - 1] == value:
            mid -= 1
        return mid
    elif value < seq[mid]:
        right_border = mid - 1
        return binary_search(value, seq, left_border, right_border)
    else:
        left_border = mid + 1
        return binary_search(value, seq, left_border, right_border)

if __name__ == '__main__':
    data = [random.randint(1, 7) for _ in range(20)]
    data.sort()
    print(data)
    print(binary_search(5, data))
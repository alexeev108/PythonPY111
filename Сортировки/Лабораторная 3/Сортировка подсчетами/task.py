import random
from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами
    if len(container) > 1:
        max_value = max(container)
        min_value = min(container)
        range_of_el = max_value - min_value + 1
        counting_list = [0] * range_of_el
        print_list = [0] * len(container)

        for el in range(len(container)):
            counting_list[container[el] - min_value] += 1

        for el in range(1, len(counting_list)):
            counting_list[el] += counting_list[el - 1]

        for el in range(len(container) - 1, -1, -1):
            print_list[counting_list[container[el] - min_value] - 1] = container[el]
            counting_list[container[el] - min_value] -= 1

        return print_list
    return container


if __name__ == '__main__':
    data = [random.randrange(-50, 50) for _ in range(10)]
    print(sort(data))
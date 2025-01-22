import random
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    ...  # TODO реализовать алгоритм быстрой сортировки
    if len(container) > 1:
        first_elem = container[0]
        left_list = []
        equal_list = []
        right_list = []
        for el in container:
            if el < first_elem:
                left_list.append(el)
            elif el == first_elem:
                equal_list.append(el)
            else:
                right_list.append(el)
        return sort(left_list) + equal_list + sort(right_list)
    return container

if __name__ == '__main__':
    data = [random.randrange(-50, 50) for _ in range(50)]
    print(sort(data))
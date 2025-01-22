import random
from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки пузырьком
    if len(container) > 1:
        container_lenght = len(container)
        for el in range(container_lenght):
            flag = False
            for el_2 in range(0, container_lenght - el - 1):
                if container[el_2] > container[el_2 + 1]:
                    container[el_2], container[el_2 + 1] = container[el_2 + 1], container[el_2]
                    flag = True
            if not flag:
                break
        return container
    return container

if __name__ == '__main__':
    data = [random.randrange(-50, 50) for _ in range(50)]
    print(sort(data))

from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO реализовать прямой метод расчета

    if not stairway:
        raise ValueError
    if len(stairway) == 1:
        return stairway[0]
    if len(stairway) == 2:
        return stairway[1]

    steps = []
    steps.append(stairway[0])
    steps.append(stairway[1])
    for i in range(2, len(stairway)):
        steps.append(min(steps[i - 1], steps[i - 2]) + stairway[i])

    return steps[-1]


if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5]))  # 7

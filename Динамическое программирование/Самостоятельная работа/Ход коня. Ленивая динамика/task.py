from typing import Tuple
from functools import lru_cache


def calculate_paths(shape: Tuple[int, int]) -> int:
    """
    Дано поле с размером rows*cols посчитать количество ходов коня из верхнего левого угла в нижний правый

    :param shape: размер доски в виде кортежа
    :return: количество путей согласно заданным условиям
    """
    ... # TODO реализуйте подсчет ходов коня
    n, m = shape
    @lru_cache
    def horse_move(i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or i >= n:
            return 0
        if j < 0 or j >= m:
            return 0
        return sum([horse_move(i - 2, j + 1),
                    horse_move(i - 2, j - 1),
                    horse_move(i - 1, j - 2),
                    horse_move(i + 1, j - 2)])
    return horse_move(n - 1, m - 1)


if __name__ == '__main__':
    print(calculate_paths((4, 4)))  # 2
    print(calculate_paths((7, 15)))  # 13309

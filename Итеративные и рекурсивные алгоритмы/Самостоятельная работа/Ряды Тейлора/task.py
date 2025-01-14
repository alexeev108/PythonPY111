import math
from typing import Union
from itertools import count
from math import factorial


DELTA = 0.000001


def get_item_n(x, n):
    """
    Очередной элемент бесконечного ряда по общей формуле:
    sin(x) -> ((-1) ** (n-1) * x ** (2n - 1)) / (2n - 1)!
    """
    return ((-1) ** (n - 1) * x ** (2 * n - 1)) / factorial(2 * n - 1)

def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    ...  # TODO вычислить sin(x) с помощью разложения сумму бесконечного ряда
    sum_ = 0
    for n in count(1):
        current_item = get_item_n(x, n)
        sum_ += current_item
        if abs(current_item) <= DELTA:
            break
    return sum_

if __name__ == '__main__':
    value_for_sin = 60 * math.pi / 180
    print(math.sin(value_for_sin))
    print(sinx(value_for_sin))
def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # TODO реализовать итеративный алгоритм нахождения факториала
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

if __name__ == '__main__':
    print(factorial_iterative(0))
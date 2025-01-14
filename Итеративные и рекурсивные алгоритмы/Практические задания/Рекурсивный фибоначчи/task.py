def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError
    fib0, fib1 = 0, 1
    if n <= 0:
        return fib0
    elif n == 1:
        return fib1
    return fib_recursive(n - 2) + fib_recursive(n - 1)


if __name__ == '__main__':
    print(fib_recursive(10))

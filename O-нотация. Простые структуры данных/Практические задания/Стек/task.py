from typing import Any


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, elem: Any) -> None:
        """
        Добавление элемента в вершину стека

        :param elem: Элемент, который должен быть добавлен
        """
        ...  # TODO реализовать операцию push

        self._stack.append(elem)

    def pop(self) -> Any:
        """
        Извлечение элемента из вершины стека.

        :raise: IndexError - Ошибка, если стек пуст

        :return: Извлеченный с вершины стека элемент.
        """
        ...  # TODO реализовать операцию pop

        if not self._stack:
            raise IndexError('Ошибка! Стек пуст')
        return self._stack.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в стеке, без его извлечения.

        :param ind: индекс элемента (отсчет с вершины, 0 - вершина, последний добавленный элемент, 1 - предпоследний элемент, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ стека

        :return: Значение просмотренного элемента
        """
        ...  # TODO реализовать операцию peek

        if not isinstance(ind, int):
            raise TypeError('Ошибка типа! Индекс должен быть int')
        if ind >= len(self._stack) or ind < 0:
            raise IndexError('Ошибка индекса! Переполнение')
        return self._stack[-1 - ind]

    def clear(self) -> None:
        """ Очистка стека. """
        ...  # TODO реализовать операцию clear

        self._stack.clear()

    def __len__(self) -> int:
        """ Количество элементов в стеке. """
        ...  # TODO реализовать операцию __len__

        return len(self._stack)

    def __str__(self):
        return f'{self._stack}'

if __name__ == '__main__':
    stack = Stack()
    stack.push('hello')
    stack.push(1)
    print(stack.peek(1))
    stack.pop()
    print(stack)

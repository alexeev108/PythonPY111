"""
My little Queue
"""
from typing import Any
from random import randint


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        ...  # TODO инициализировать список

        self._queue = [randint(-10, 10) for i in range(50)]

    def enqueue(self, elem: Any) -> None: # O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        ...  # TODO реализовать метод enqueue

        self._queue.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        ...  # TODO реализовать метод dequeue

        for i in range(len(self._queue)): # O(1)
            if self._queue[i]:
                return self._queue.pop(0)
        raise IndexError

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        ...  # TODO реализовать метод peek

        if not isinstance(ind, int):
            raise TypeError
        if ind >= len(self._queue) or ind < 0:
            raise IndexError
        return self._queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        ...  # TODO реализовать метод clear

        self._queue.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        ...  # TODO реализовать метод __len__

        return len(self._queue)

    def __str__(self):
        return f'{self._queue}'


if __name__ == '__main__':
    queue = Queue()
    print(queue)
    queue.enqueue(1993)
    print(queue.dequeue())
    print(queue)
    print(queue.peek(1))
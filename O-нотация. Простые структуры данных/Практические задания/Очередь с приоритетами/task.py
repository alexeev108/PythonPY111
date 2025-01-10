"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        ...  # TODO использовать deque для реализации очереди с приоритетами

        self._queue = [list() for _ in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1)]

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        ...  # TODO реализовать метод enqueue

        if not isinstance(priority, int):
            raise TypeError
        if priority not in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1):
            raise IndexError
        self._queue[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        ...  # TODO реализовать метод dequeue

        for i in range(len(self._queue)):
            if self._queue[i]:
                return self._queue[i].pop(0)
        raise IndexError

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        ...  # TODO реализовать метод peek

        if not isinstance(priority, int):
            raise TypeError
        if priority not in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1):
            raise IndexError
        if not isinstance(priority, int):
            raise TypeError
        if ind >= len(self._queue[priority]) or ind < 0:
            raise IndexError
        return self._queue[priority][ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        ...  # TODO реализовать метод clear

        for el in self._queue:
            el.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        ...  # TODO реализовать метод __len__

        count = 0
        for el in self._queue:
            count += len(el)
        return count

if __name__ == '__main__':
    queue = PriorityQueue()
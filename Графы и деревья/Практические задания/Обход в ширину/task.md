
Обойти все вершины невзвешенного графа,
к каждой из которых придя кратчайшим путем
![](https://camo.githubusercontent.com/73761db9068bf4c9de4a23209da587a29e8cc672558534d4ff40ac0480854047/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f352f35642f427265616474682d46697273742d5365617263682d416c676f726974686d2e676966)

## Начальные условия
1. Нужен список (множество) посещенных вершин,
куда изначально добавляем начальную вершину
2. Нужна очередь, в которую добавляем начальную вершину

## Алгоритм
1. Взять вершину из очереди.
2. Взять всех соседей этой вершины.
3. Для всех соседей соседа: если вершина не посещена, то добавить ее в конец очереди и
в список посещенных.
   
## Задача
1. Написать алгоритм обхода в ширину
2. Записать граф и получить список узлов, в порядке из посещения. Стартовый узел `A`
![img.png](img.png)

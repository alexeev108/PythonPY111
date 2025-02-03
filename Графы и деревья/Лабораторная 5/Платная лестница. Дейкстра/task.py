from typing import Union
from matplotlib import pyplot
import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    starting_node = 0
    list_ = []
    _, min_weights = nx.dijkstra_predecessor_and_distance(graph, starting_node)
    for node in graph.nodes:
        if node not in min_weights:
            min_weights[node] = float('inf')
    for key in min_weights.keys():
        list_.append(key)
    max_number = max(list_)

    return min_weights[max_number]

def g_create(data):
    list_ = []
    for i in range(len(data) - 1):
        x = (i, i + 1, data[i])
        y = (i, i + 2, data[i + 1])
        list_.append(x)
        list_.append(y)
    return list_[:-1]


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = nx.DiGraph()  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    new = stairway_graph.add_weighted_edges_from(g_create(stairway))
    print(stairway_path(stairway_graph))  # 72


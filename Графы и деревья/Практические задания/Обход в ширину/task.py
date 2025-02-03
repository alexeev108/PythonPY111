from typing import Hashable, List
from matplotlib import pyplot

import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в ширину
    visited = set()
    queue_for_visit = [start_node]
    path_ = []
    visited.add(start_node)

    while queue_for_visit:
        current_node = queue_for_visit.pop(0)
        path_.append(current_node)
        for n in g[current_node]:
            if n not in visited:
                queue_for_visit.append(n)
                visited.add(n)
    return path_

if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    graph = nx.Graph()
    graph.add_edges_from([('A', 'B'),
                          ('A', 'F'),
                          ('B', 'G'),
                          ('F', 'G'),
                          ('G', 'C'),
                          ('G', 'H'),
                          ('G', 'I'),
                          ('C', 'H'),
                          ('H', 'I'),
                          ('H', 'J'),
                          ('H', 'E'),
                          ('H', 'D'),
                          ('D', 'E')])
    nx.draw_spring(graph, node_color='orange', node_size=700, with_labels=True)
    pyplot.show()
    print(bfs(graph, 'A'))
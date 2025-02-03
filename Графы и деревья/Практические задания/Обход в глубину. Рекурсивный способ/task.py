from typing import Hashable, List
import networkx as nx
from matplotlib import pyplot


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в глубину
    visited = set()
    path_ = []

    def rec_dfs(current_node):
        visited.add(current_node)
        path_.append(current_node)
        for n in g[current_node]:
            if n not in visited:
                rec_dfs(n)
    rec_dfs(start_node)
    return path_

if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    graph = nx.Graph()
    graph.add_edges_from([('A', 'B'),
                          ('A', 'C'),
                          ('A', 'D'),
                          ('B', 'E'),
                          ('B', 'F'),
                          ('C', 'G'),
                          ('D', 'H'),
                          ('D', 'I'),
                          ('E', 'J'),
                          ])
    nx.draw_spring(graph, node_color='orange', node_size=700, with_labels=True)
    pyplot.show()
    print(dfs(graph, 'A'))
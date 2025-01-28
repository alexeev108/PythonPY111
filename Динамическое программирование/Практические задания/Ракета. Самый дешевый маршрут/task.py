from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    ...  # TODO рассчитать таблицу стоимостей перемещений
    table_sum = table.copy()
    for i in range(1, len(table_sum)):
        table_sum[i][0] += table_sum[i - 1][0]
    for i in range(1, len(table_sum[0])):
        table_sum[0][i] += table_sum[0][i - 1]

    for i in range(1, len(table_sum)):
        for j in range(1, len(table_sum[i])):
            table_sum[i][j] += min(table_sum[i][j - 1], table_sum[i - 1][j])
    return table_sum

if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    for el in total_coasts:
        print(*el)
    print(total_coasts[-1][-1])  # 21

def unique_paths(m: int, n: int) -> int:
    table = [[0] * n for _ in range(m)]

    for i in range(m):
        table[i][0] = 1

    for i in range(n):
        table[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[-1][-1]


if __name__ == '__main__':
    paths = unique_paths(4, 2)
    print(paths)


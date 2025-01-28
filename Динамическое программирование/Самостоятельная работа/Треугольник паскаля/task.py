from typing import List


def generate(num_rows: int) -> List[List[int]]:
    if num_rows == 0:
        return []
    pascal_ = [[1]]
    for i in range(1, num_rows):
        row = [1]
        for j in range(1, i):
            row.append(pascal_[i - 1][j - 1] + pascal_[i - 1][j])
        row.append(1)
        pascal_.append(row)
    return pascal_

if __name__ == '__main__':
    n = 10
    for el in generate(n):
        print(el)

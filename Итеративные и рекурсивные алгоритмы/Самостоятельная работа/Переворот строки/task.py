from typing import List


def reverse_string(s: List[str]) -> None:
    ...
    for i in range(len(s) // 2):
        s[i], s[-1 - i] = s[-1 - i], s[i]

if __name__ == '__main__':
    data = list('hello')
    reverse_string(data)
    print(data)
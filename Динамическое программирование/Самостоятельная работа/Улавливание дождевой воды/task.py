from typing import List


def trap(height: List[int]) -> int:
    n = len(height)
    left = [0] * n
    right = [0] * n

    res = 0

    left[0] = height[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], height[i])

    right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])

    for i in range(1, n - 1):
        min_ = min(left[i - 1], right[i + 1])
        if min_ > height[i]:
            res += min_ - height[i]

    return res

if __name__ == '__main__':
    data = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(data))

import sys
from functools import lru_cache

sys.setrecursionlimit(2000)


def exp_sum(a, k):
    @lru_cache(None)
    def dfs(index, prev_value):
        if index == k:
            return 0
        current_sum = 0.0
        for face in a:
            if index == 0 or face != prev_value:
                current_sum += (face + dfs(index + 1, face)) / 6
            else:
                current_sum += dfs(index + 1, face) / 6
        return current_sum

    return dfs(0, -1)


a = list(map(int, input().split()))
k = int(input())

print(f"{exp_sum(tuple(a), k):.10f}")

def min_cost(n, k, a):
    count = [0] * (k + 1)
    left = 0
    found = 0
    min_cost = float('inf')
    current_cost = 0
    for right in range(n):
        current_cost += a[right]
        if 1 <= a[right] <= k:
            if count[a[right]] == 0:
                found += 1
            count[a[right]] += 1
        while found == k:
            min_cost = min(min_cost, current_cost)
            current_cost -= a[left]
            if 1 <= a[left] <= k:
                count[a[left]] -= 1
                if count[a[left]] == 0:
                    found -= 1
            left += 1
    return min_cost


n, k = map(int, input().split())
a = list(map(int, input().split()))

print(min_cost(n, k, a))

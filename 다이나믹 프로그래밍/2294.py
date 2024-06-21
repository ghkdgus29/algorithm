# k를 구성하는 동전 최소 개수

# d[n] = min(d[n-c1], d[n-c2], ...) + 1
# d[c] = 1

n, target = map(int, input().split())
coins = [int(input()) for _ in range(n)]
d = [float('inf')] * (target + 1)
for c in coins:
    if c <= target:
        d[c] = 1

for i in range(target + 1):
    for c in coins:
        if i - c >= 0:
            d[i] = min(d[i], d[i - c] + 1)

print(d[-1] if d[-1] != float('inf') else -1)

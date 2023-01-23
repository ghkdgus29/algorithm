# d[n][k] = sum(d[n-i][k-1])  (0 <= i <= n)

n, k = map(int, input().split())

d = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    d[i][1] = 1

for i in range(n + 1):  # n -> i
    for j in range(2, k + 1):  # k -> j
        for l in range(i + 1):  # i -> l
            d[i][j] += d[i - l][j - 1]
        d[i][j] %= 1000000000

print(d[n][k] % 1000000000)

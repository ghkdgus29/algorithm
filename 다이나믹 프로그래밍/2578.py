# 전 수보다 2배 이상
import sys

# d[i][j] -> i번째 수에 j가 들어갈 때의 경우의 수
# d[i][j] = d[i-1][k] (k <= j//2)

for _ in range(int(input())):
    n, limit = map(int, sys.stdin.readline().split())
    d = [[0] * (limit + 1) for _ in range(n)]

    for i in range(limit + 1):
        d[0][i] = i

    for i in range(1, n):
        for j in range(limit + 1):
            d[i][j] += d[i][j - 1] + d[i - 1][j // 2]

    print(d[-1][-1])

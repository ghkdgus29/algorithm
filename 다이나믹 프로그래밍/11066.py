# 최소비용으로 합치기
import sys

# i 부터 j 까지를 합치는 데 필요한 비용
# d[i][j] = min(d[i][k] + d[k+1][j] + 합치는 비용) , (i <= k < j)

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    d = [[-1] * n for _ in range(n)]


    def go(i, j):
        if i == j:
            return 0

        if d[i][j] != -1:
            return d[i][j]

        cost = float('inf')
        merge_cost = 0
        for k in range(i, j + 1):
            merge_cost += a[k]
        for idx in range(i, j):
            cost = min(cost, go(i, idx) + go(idx + 1, j) + merge_cost)

        d[i][j] = cost
        return d[i][j]


    go(0, n - 1)

    print(d[0][-1])

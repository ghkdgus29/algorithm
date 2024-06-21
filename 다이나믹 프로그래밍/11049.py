# 곱셈 연산 횟수의 최솟값 구하기

# d[i][j] -> i번째 행렬부터 j번째 행렬까지의 곱을 할 때의 연산 횟수 최솟값
# d[i][j] = d[i][k] + d[k+1][j] + (m[i][0] * m[k][1] * m[j][1]), (i <= k <= j-1)

def go(i, j):
    if i == j:
        d[i][j] = 0
        return 0

    if d[i][j] != float('inf'):
        return d[i][j]

    for k in range(i, j):
        d[i][j] = min(d[i][j], go(i, k) + go(k + 1, j) + (matrix[i][0] * matrix[k][1] * matrix[j][1]))

    return d[i][j]


n = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(n)]
d = [[float('inf')] * n for _ in range(n)]

print(go(0, n - 1))

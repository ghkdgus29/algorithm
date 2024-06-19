# d[n][k] = max(d[n-1][k-1], d[n-1][k]) + p[k]  중간
# d[n][0] = d[n-1][0] + p[0]                    왼쪽끝
# d[n][n-1] = d[n-1][n-2] + p[n-1]              오른쪽끝

n = int(input())
d = [[0] * (n + 1) for _ in range(n + 1)]

d[1][0] = int(input())
for i in range(2, n + 1):
    p = list(map(int, input().split()))

    d[i][0] = d[i - 1][0] + p[0]                # 왼쪽끝
    d[i][i - 1] = d[i - 1][i - 2] + p[i - 1]    # 오른쪽끝

    for j in range(1, i - 1):                                   # 중간
        d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + p[j]

print(max(d[n]))

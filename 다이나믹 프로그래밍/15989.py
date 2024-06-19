# d[n][1] = sum(d[n-1])
# d[n][2] = d[n-2][2] + d[n-2][3]
# d[n][3] = d[n-3][3]

t = int(input())
for _ in range(t):
    n = int(input())
    d = [[0] * 4 for _ in range(n + 3)]

    d[1][1] = 1  # 1
    d[2][1] = 1  # 1 + 1
    d[2][2] = 1  # 2
    d[3][1] = 2  # 2 + 1, 1 + 1 + 1
    d[3][3] = 1  # 3

    for i in range(4, n + 1):
        d[i][1] = sum(d[i - 1])
        d[i][2] = d[i - 2][2] + d[i - 2][3]
        d[i][3] = d[i - 3][3]

    print(sum(d[n]))

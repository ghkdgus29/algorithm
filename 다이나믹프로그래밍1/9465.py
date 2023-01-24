# d[n][0] = max(d[n-1][1], d[n-1][2])
# d[n][1] = max(d[n-1][0], d[n-1][2]) + p1[n]
# d[n][2] = max(d[n-1][0], d[n-1][1]) + p2[n]

t = int(input())
for _ in range(t):
    n = int(input())
    d = [[0] * 3 for _ in range(n + 1)]

    p1 = [0] + list(map(int, input().split()))
    p2 = [0] + list(map(int, input().split()))

    for i in range(1, n + 1):
        d[i][0] = max(d[i-1][1], d[i-1][2])
        d[i][1] = max(d[i-1][0], d[i-1][2]) + p1[i]
        d[i][2] = max(d[i-1][0], d[i-1][1]) + p2[i]

    print(max(d[n]))

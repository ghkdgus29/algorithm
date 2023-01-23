# d[n][2] = min(d[n-1][0], d[n-1][1]) + p[2]
# d[n][1] = min(d[n-1][0], d[n-1][2]) + p[1]
# d[n][0] = min(d[n-1][1], d[n-1][2]) + p[0]

n = int(input())
d = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n+1):
    p = list(map(int, input().split()))

    d[i][0] = min(d[i-1][1], d[i-1][2]) + p[0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + p[1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + p[2]

print(min(d[n]))
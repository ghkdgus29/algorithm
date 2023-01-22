# d[n][1] = d[n-1][2] + d[n-1][3]
# d[n][2] = d[n-2][1] + d[n-2][3]
# d[n][3] = d[n-3][1] + d[n-3][2]

d = [[0, 0, 0, 0] for _ in range(100001)]

d[1][1] = 1

d[2][2] = 1

d[3][1] = 1
d[3][2] = 1
d[3][3] = 1

for i in range(4, 100001):
    d[i][1] = (d[i - 1][2] + d[i - 1][3]) % 1000000009
    d[i][2] = (d[i - 2][1] + d[i - 2][3]) % 1000000009
    d[i][3] = (d[i - 3][1] + d[i - 3][2]) % 1000000009

t = int(input())
for _ in range(t):
    print(sum(d[int(input())]) % 1000000009)

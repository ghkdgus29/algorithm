# d[n][0] = d[n-1][1]
# d[n][1] = d[n-1][0] + d[n-1][2]
# ...
# d[n][8] = d[n-1][7] + d[n-1][9]
# d[n][9] = d[n-1][8]

d = [[0 for _ in range(10)] for i in range(101)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, 101):
    d[i][0] = d[i - 1][1] % 1000000000
    d[i][9] = d[i - 1][8] % 1000000000
    for j in range(1, 9):
        d[i][j] = (d[i - 1][j - 1] + d[i - 1][j + 1]) % 1000000000

n = int(input())
print(sum(d[n]) % 1000000000)

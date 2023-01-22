# d[n][1] = d[n-1][0]   (n > 2)
# d[n][0] = d[n-1]      (n > 2)

n = int(input())

d = [[0] * 2 for _ in range(n + 2)]

d[1][1] = 1
d[2][0] = 1

for i in range(3, n + 1):
    d[i][0] = d[i - 1][0] + d[i - 1][1]
    d[i][1] = d[i - 1][0]

print(sum(d[n]))

# d[n] = max(d[n-1], d[n-2]+p[n], d[n-3]+p[n-1]+p[n])

n = int(input())
p = [0] + [int(input()) for _ in range(n)]
d = [0] * (n + 3)

d[1] = p[1]
if len(p) > 2:
    d[2] = p[1] + p[2]

for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + p[i], d[i - 3] + p[i - 1] + p[i])

print(d[n])

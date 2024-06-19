# d[n] = d[n-1] + d[n-2] + d[n-3]

limit = 1000000
mod = 1000000009

d = [0] * (limit + 1)

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, limit+1):
    d[i] = d[i-1] + d[i-2] + d[i-3]
    d[i] %= mod

t = int(input())

for _ in range(t):
    print(d[int(input())])


n = int(input())
p = list(map(int, input().split()))

d = [0] * n

d[0] = p[0]

for i in range(1, n):
    d[i] = max(d[i - 1] + p[i], p[i])

print(max(d))

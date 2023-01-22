# d[n] = min(d[n-1] + p[1] , d[n-2] + p[2] , ... , p[n])

d = [1000 * 10000] * 1001
d[0] = 0

n = int(input())
p = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = min(d[i], d[i - j] + p[j])

print(d[n])

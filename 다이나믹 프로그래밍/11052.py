# d[n] = max(d[n-1] + p[1], d[n-2] + p[2], ... , p[n])

d = [0] * 1000

n = int(input())
p = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    j = i
    while j > 0:
        if d[i] < d[i - j] + p[j]:
            d[i] = d[i - j] + p[j]
        j -= 1

print(d[n])

# d[n] = d[n-1] + 1
# d[n] = min(d[n-k^2]) + 1

n = int(input())
d = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, int(i ** (1 / 2)) + 1):
        if d[i] > d[i - j * j] + 1:
            d[i] = d[i - j * j] + 1

print(d[n])

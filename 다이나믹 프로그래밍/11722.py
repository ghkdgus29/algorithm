n = int(input())
a = [0] + list(map(int, input().split()))

d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = 1
    for j in range(i):
        if a[i] < a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))

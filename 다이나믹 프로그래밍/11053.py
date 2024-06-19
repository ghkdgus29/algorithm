n = int(input())
a = [0] + list(map(int, input().split()))

d = [1] * (n + 1)
for i in range(2, n + 1):
    for j in range(1, i):
        if a[j] < a[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1

print(max(d))
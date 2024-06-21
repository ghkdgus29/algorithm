# n번 눌러 출력된 A개수 최대로

# d[i] = max(d[i-1] + 1, d[i-(j+2)] * (j+1)) , (1 <= j <= i-3)


n = int(input())
d = [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = d[i - 1] + 1
    for j in range(1, i - 3 + 1):
        d[i] = max(d[i], d[i - (j + 2)] * (j + 1))

print(d[-1])

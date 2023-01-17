n = int(input())

d = [0] * (n + 4)       # n 이 3보다 작은 경우를 대비하여 4를 더함
d[1] = 0
d[2] = 1
d[3] = 1

for i in range(4, n + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1

    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1

print(d[n])
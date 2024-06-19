n = int(input())
a = [0] + list(map(int, input().split()))

LIS = [1] * (n + 1)
LDS = [1] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i):
        if a[j] < a[i] and LIS[j] + 1 > LIS[i]:
            LIS[i] = LIS[j] + 1

for i in range(n, 0, -1):
    for j in range(n, i, -1):
        if a[j] < a[i] and LDS[j] + 1 > LDS[i]:
            LDS[i] = LDS[j] + 1

LBS = [i + j for i, j in zip(LIS, LDS)]

print(max(LBS) - 1)

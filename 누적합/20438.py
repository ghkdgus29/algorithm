import sys

n, k, q, m = map(int, input().split())
sleep = [0 for _ in range(n + 3)]
check = [0 for _ in range(n + 3)]

for i in map(int, sys.stdin.readline().split()):
    sleep[i] = 1

for i in map(int, sys.stdin.readline().split()):
    if sleep[i]:
        continue

    for j in range(i, n + 3, i):
        if not sleep[j]:
            check[j] = 1

pre = [check[0]]
for i in range(1, n + 3):
    pre.append(pre[-1] + check[i])

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(e - s + 1 - (pre[e] - pre[s - 1]))

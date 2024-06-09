import sys

n, m = map(int, input().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s = [[0] * (n + 1) for _ in range(n + 1)]
for y in range(1, n + 1):
    for x in range(1, n + 1):
        s[y][x] = a[y - 1][x - 1] + s[y][x - 1] + s[y - 1][x] - s[y - 1][x - 1]

for _ in range(m):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    print(s[y2][x2] - s[y2][x1 - 1] - s[y1 - 1][x2] + s[y1 - 1][x1 - 1])


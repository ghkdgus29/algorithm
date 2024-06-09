# a[y][x] = s[y][x] - s[y][x-1] - s[y-1][x] + s[y-1][x-1]

import sys

h, w, q = map(int, input().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
s = [[0] * (w + 1) for _ in range(h + 1)]

for y in range(1, h + 1):
    for x in range(1, w + 1):
        s[y][x] = a[y - 1][x - 1] + s[y][x - 1] + s[y - 1][x] - s[y - 1][x - 1]

for _ in range(q):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())

    cnt = (y2 - y1 + 1) * (x2 - x1 + 1)
    summ = s[y2][x2] - s[y1 - 1][x2] - s[y2][x1 - 1] + s[y1 - 1][x1 - 1]
    print(summ // cnt)

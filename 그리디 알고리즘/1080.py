import sys

h, w = map(int, input().split())

given = [list(map(int, list(input()))) for _ in range(h)]
target = [list(map(int, list(input()))) for _ in range(h)]


def change(sx, sy):
    for y in range(sy, sy + 3):
        for x in range(sx, sx + 3):
            given[y][x] = 1 ^ given[y][x]


count = 0
for y in range(h - 3 + 1):
    for x in range(w - 3 + 1):
        if given[y][x] != target[y][x]:
            count += 1
            change(x, y)

for y in range(h):
    for x in range(w):
        if given[y][x] != target[y][x]:
            print(-1)
            sys.exit()

print(count)

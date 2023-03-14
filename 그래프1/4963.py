import sys


def dfs(x, y):
    visit[y][x] = True

    if graph[y][x] == '0':
        return 0

    for i in range(8):
        if 0 <= x + dx[i] < w and 0 <= y + dy[i] < h:
            if not visit[y + dy[i]][x + dx[i]]:
                dfs(x + dx[i], y + dy[i])

    return 1


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph = [sys.stdin.readline().split() for _ in range(h)]
    visit = [[False] * w for _ in range(h)]

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    ans = 0
    for y in range(h):
        for x in range(w):
            if not visit[y][x]:
                ans += dfs(x, y)

    print(ans)

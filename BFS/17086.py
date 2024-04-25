import collections


def bfs(x, y):
    queue = collections.deque()
    queue.append((x, y, 0))
    dist[y][x] = 0

    while queue:
        cx, cy, cost = queue.popleft()
        for i in range(8):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < w and 0 <= ny < h:
                if dist[ny][nx] > cost + 1:
                    dist[ny][nx] = cost + 1
                    queue.append((nx, ny, cost + 1))


h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

shark = []
for y in range(h):
    for x in range(w):
        if board[y][x] == 1:
            shark.append((x, y))

dist = [[float('inf')] * w for _ in range(h)]
for sx, sy in shark:
    bfs(sx, sy)

ans = 0
for y in range(h):
    for x in range(w):
        ans = max(ans, dist[y][x])

print(ans)

import collections

n = int(input())
board = [list(input()) for _ in range(n)]
NOT_VISIT = float('inf')
dist = [[[NOT_VISIT] * 4 for _ in range(n)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 아래 오른 위 왼
door = []

for y in range(n):
    for x in range(n):
        if board[y][x] == '#':
            door.append((x, y))

queue = collections.deque()
sx, sy = door[0]
queue.append((sx, sy, 0))
queue.append((sx, sy, 1))
queue.append((sx, sy, 2))
queue.append((sx, sy, 3))
dist[sy][sx][0] = 0
dist[sy][sx][1] = 0
dist[sy][sx][2] = 0
dist[sy][sx][3] = 0

while queue:
    x, y, dir = queue.popleft()

    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n:
        if board[ny][nx] != '*' and dist[ny][nx][dir] > dist[y][x][dir]:
            dist[ny][nx][dir] = dist[y][x][dir]
            queue.appendleft((nx, ny, dir))

        if board[ny][nx] == "!":
            if dist[ny][nx][(dir - 1) % 4] > dist[y][x][dir] + 1:
                dist[ny][nx][(dir - 1) % 4] = dist[y][x][dir] + 1
                queue.append((nx, ny, (dir - 1) % 4))

            if dist[ny][nx][(dir + 1) % 4] > dist[y][x][dir] + 1:
                dist[ny][nx][(dir + 1) % 4] = dist[y][x][dir] + 1
                queue.append((nx, ny, (dir + 1) % 4))

ex, ey = door[1]
print(min(dist[ey][ex]))

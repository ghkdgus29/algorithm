import collections
import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, h, d = map(int, input().split())
board = [list(input()) for _ in range(n)]
visit = [[-1] * n for _ in range(n)]

sx = sy = 0
for y in range(n):
    for x in range(n):
        if board[y][x] == 'S':
            sx = x
            sy = y

queue = collections.deque()
queue.append((sx, sy, h, 0, 0))
visit[sy][sx] = h

while queue:
    x, y, health, umb_health, cnt = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[ny][nx] == 'E':
                print(cnt + 1)
                sys.exit(0)

            cur_health = health
            cur_umb_health = umb_health

            if board[ny][nx] == 'U':
                cur_umb_health = d

            if cur_umb_health == 0:
                cur_health -= 1
            else:
                cur_umb_health -= 1

            if cur_health > 0 and visit[ny][nx] < cur_umb_health + cur_health:
                visit[ny][nx] = cur_umb_health + cur_health
                queue.append((nx, ny, cur_health, cur_umb_health, cnt + 1))

print(-1)

import collections

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(sx, sy):
    queue = collections.deque()
    queue.append((sx, sy))
    visit[sy][sx] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[ny][nx] and board[ny][nx] == board[y][x]:
                    queue.append((nx, ny))
                    visit[ny][nx] = True


n = int(input())
board = [list(input()) for _ in range(n)]
visit = [[False] * n for _ in range(n)]

normal = 0

for y in range(n):
    for x in range(n):
        if not visit[y][x]:
            normal += 1
            bfs(x, y)

for y in range(n):
    for x in range(n):
        if board[y][x] == 'R':
            board[y][x] = 'G'

visit = [[False] * n for _ in range(n)]

abnormal = 0
for y in range(n):
    for x in range(n):
        if not visit[y][x]:
            abnormal += 1
            bfs(x, y)

print(normal, abnormal)

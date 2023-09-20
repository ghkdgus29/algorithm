import collections

NOT_VISIT = 1_0000_0000
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

h, w, k = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(h)]
dist = [[[NOT_VISIT] * (k + 1) for _ in range(w)] for _ in range(h)]

queue = collections.deque()
queue.append((0, 0, 0))
dist[0][0][0] = 1

while queue:
    x, y, z = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if board[ny][nx] == 0 and dist[ny][nx][z] == NOT_VISIT:
                queue.append((nx, ny, z))
                dist[ny][nx][z] = dist[y][x][z] + 1

            if z < k and board[ny][nx] == 1 and dist[ny][nx][z + 1] == NOT_VISIT:
                queue.append((nx, ny, z + 1))
                dist[ny][nx][z + 1] = dist[y][x][z] + 1

print(min(dist[-1][-1]) if min(dist[-1][-1]) != NOT_VISIT else -1)

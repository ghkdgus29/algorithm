import collections

ddx = [1, 2, 2, 1, -1, -2, -2, -1]
ddy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
NOT_VISIT = float('inf')

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
dist = [[[NOT_VISIT] * (k + 1) for _ in range(w)] for _ in range(h)]

queue = collections.deque()
queue.append((0, 0, k))
dist[0][0][k] = 0

while queue:
    x, y, cnt = queue.popleft()

    if cnt > 0:
        for i in range(8):
            nx = ddx[i] + x
            ny = ddy[i] + y
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] == 0 and dist[ny][nx][cnt - 1] == NOT_VISIT:
                    dist[ny][nx][cnt - 1] = dist[y][x][cnt] + 1
                    queue.append((nx, ny, cnt - 1))

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < w and 0 <= ny < h:
            if board[ny][nx] == 0 and dist[ny][nx][cnt] == NOT_VISIT:
                dist[ny][nx][cnt] = dist[y][x][cnt] + 1
                queue.append((nx, ny, cnt))

print(min(dist[-1][-1]) if min(dist[-1][-1]) != NOT_VISIT else -1)

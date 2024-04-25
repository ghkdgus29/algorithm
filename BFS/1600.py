# k 번은 나이트처럼 움직이고, 그 이후에는 한 칸씩만 움직인다.
# 왼쪽 위에서 오른쪽 아래까지 가는 최소한의 동작 수는?
# 말은 장애물을 넘지만, 원숭이는 못 넘는다.

# (이동 좌표, 말 모드 횟수, 이동 횟수)

import collections

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ddx = [1, 2, 2, 1, -1, -2, -2, -1]
ddy = [-2, -1, 1, 2, 2, 1, -1, -2]

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
NOT_VISIT = float('inf')
dist = [[[NOT_VISIT] * (k + 1) for _ in range(w)] for _ in range(h)]
queue = collections.deque()
queue.append((0, 0, k))
dist[0][0][k] = 0

while queue:
    x, y, cnt = queue.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < w and 0 <= ny < h:
            if board[ny][nx] == 0 and dist[ny][nx][cnt] == NOT_VISIT:
                dist[ny][nx][cnt] = dist[y][x][cnt] + 1
                queue.append((nx, ny, cnt))

    if cnt > 0:
        for i in range(8):
            nx = ddx[i] + x
            ny = ddy[i] + y
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] == 0 and dist[ny][nx][cnt - 1] == NOT_VISIT:
                    dist[ny][nx][cnt - 1] = dist[y][x][cnt] + 1
                    queue.append((nx, ny, cnt - 1))

print(min(dist[-1][-1]) if min(dist[-1][-1]) != NOT_VISIT else -1)

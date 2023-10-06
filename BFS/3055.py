import collections

NOT_VISIT = -1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
h, w = map(int, input().split())

board = [list(input()) for _ in range(h)]
water = [[NOT_VISIT] * w for _ in range(h)]         # 물이 도달하는 시간
dist = [[NOT_VISIT] * w for _ in range(h)]          # 고슴도치의 이동거리

hedgehog_x = hedgehog_y = cave_x = cave_y = -1

queue = collections.deque()
for y in range(h):
    for x in range(w):
        if board[y][x] == '*':              # 물을 큐에 집어 넣는다.
            queue.append((x, y))
            water[y][x] = 0             # 물이 0초부터 존재
        elif board[y][x] == 'S':            # 고슴도치 좌표 기록
            hedgehog_x, hedgehog_y = x, y
        elif board[y][x] == 'D':            # 동굴 좌표 기록
            cave_x, cave_y = x, y


while queue:                                    # 물이 도달하는 시간을 bfs 로 계산
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if water[ny][nx] != NOT_VISIT:          # 만약 이미 물이 도착한 곳이라면 물을 이동시키지 않는다.
                continue
            if board[ny][nx] in 'XD':               # 돌이나 동굴은 물이 이동할 수 없다.
                continue
            water[ny][nx] = water[y][x] + 1         # 물이 정상적으로 이동하는 경우
            queue.append((nx, ny))


queue.append((hedgehog_x, hedgehog_y))        # 고슴도치 이동을 bfs 로 계산
dist[hedgehog_y][hedgehog_x] = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if dist[ny][nx] != NOT_VISIT:       # 고슴도치가 이미 한 번 이동했던 곳인 경우, 고슴도치를 이동시키지 않는다.
                continue
            if board[ny][nx] == 'X':            # 돌로는 이동할 수 없다.
                continue
            if water[ny][nx] != NOT_VISIT and dist[y][x] + 1 >= water[ny][nx]:      # 물이 언젠가 도착할 수 있는 곳이고,
                continue                                                            # 고슴도치 이동 시점에 물에 잠기거나 잠길 경우 이동할 수 없다.

            dist[ny][nx] = dist[y][x] + 1       # 고슴도치가 정상적으로 이동하는 경우
            queue.append((nx, ny))

if dist[cave_y][cave_x] == NOT_VISIT:
    print('KAKTUS')
else:
    print(dist[cave_y][cave_x])

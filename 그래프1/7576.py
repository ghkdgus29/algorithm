import collections


def bfs():
    queue = collections.deque([])

    x = []
    y = []

    for i in range(h):  # 썩은 토마토가 있는지 체크
        for j in range(w):
            if graph[i][j] == 1:
                y.append(i)
                x.append(j)

    for i in range(len(x)):  # 썩은 토마토들을 모두 큐에 저장
        queue.append((x[i], y[i], 0))
        visit[y[i]][x[i]] = True

    cnt = 0
    while queue:  # bfs 탐색
        x, y, cnt = queue.popleft()
        graph[y][x] += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if not visit[ny][nx] and graph[ny][nx] != -1:
                    visit[ny][nx] = True
                    queue.append((nx, ny, cnt + 1))

    for i in range(h):  # 전부 썩었는지 확인
        for j in range(w):
            if graph[i][j] == 0:
                return -1

    return cnt


w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

visit = [[False] * w for _ in range(h)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(bfs())

import collections

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

w, h = map(int, input().split())
graph = [list(input()) for _ in range(h)]

dist = [[-1] * w for _ in range(h)]

deque = collections.deque([(0, 0)])
dist[0][0] = 0

while deque:
    x, y = deque.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < w and 0 <= ny < h and dist[ny][nx] == -1:
            if graph[ny][nx] == '0':
                dist[ny][nx] = dist[y][x]
                deque.appendleft((nx, ny))

            else:
                dist[ny][nx] = dist[y][x] + 1
                deque.append((nx, ny))

print(dist[h - 1][w - 1])

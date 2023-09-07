import collections

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
NOT_VISIT = -1


def bfs(sx, sy):
    queue = collections.deque([(sx, sy)])
    dist[sy][sx] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[ny][nx] == NOT_VISIT:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((nx, ny))


n = int(input())

dist = [[NOT_VISIT] * n for _ in range(n)]
sx, sy, tx, ty = map(int, input().split())

bfs(sx, sy)

print(dist[ty][tx])

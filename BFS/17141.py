# 모든 빈칸에 바이러스를 퍼뜨리는 최소 시간 구하기
import collections
import itertools


def bfs(sx, sy):
    dist = [[float('inf')] * n for _ in range(n)]
    queue = collections.deque()
    queue.append((sx, sy))
    dist[sy][sx] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] != 1 and dist[ny][nx] == float('inf'):
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((nx, ny))

    return dist


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, virus_cnt = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = []
for y in range(n):
    for x in range(n):
        if board[y][x] == 2:
            virus.append((x, y))

distance = {}
for idx, start_point in enumerate(virus):
    sx, sy = start_point
    distance[idx] = bfs(sx, sy)

ans = float('inf')
combinations = itertools.combinations(distance.keys(), virus_cnt)
for combi in combinations:
    min_dist = [[float('inf')] * n for _ in range(n)]
    for idx in combi:
        dist = distance[idx]
        for y in range(n):
            for x in range(n):
                min_dist[y][x] = min(min_dist[y][x], dist[y][x])
    need_time = -1
    for y in range(n):
        for x in range(n):
            if board[y][x] != 1:
                need_time = max(need_time, min_dist[y][x])
    ans = min(ans, need_time)

print(ans if ans != float('inf') else -1)

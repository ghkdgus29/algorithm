import collections
import itertools


def bfs(x, y, points):
    dist = [[float('inf')] * w for _ in range(h)]
    queue = collections.deque()
    queue.append((x, y))
    dist[y][x] = 0
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] != 'x' and dist[ny][nx] == float('inf'):
                    dist[ny][nx] = dist[cy][cx] + 1
                    queue.append((nx, ny))

    result = {}
    for i, j in points:
        if x == i and y == j:
            continue
        result[(i, j)] = dist[j][i]

    return result


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    board = [list(input()) for _ in range(h)]
    start_distance = {}
    distance = {}
    sx = sy = -1
    dirty = []
    for y in range(h):
        for x in range(w):
            if board[y][x] == 'o':
                sx = x
                sy = y
            elif board[y][x] == '*':
                dirty.append((x, y))

    start_distance = bfs(sx, sy, dirty)                         # 시작 지점에서 각 더러운 지점간의 거리를 구한다.

    for x, y in dirty:
        distance[(x, y)] = bfs(x, y, dirty + [(sx, sy)])            # 미리 각 더러운 지점간의 거리를 구한다 (시작 지점까지의 거리도 구한다)

    permutations = itertools.permutations(distance.keys(), len(distance))

    ans = float('inf')
    for each in permutations:                               # 각 지점들의 순서를 정한다
        tmp = start_distance[each[0]]                       # 각 지점간의 거리는 미리 구함으로써 큰 시간을 소요하지 않는다.
        current_point = each[0]

        for next_point in each[1:]:
            tmp += distance[current_point][next_point]
            current_point = next_point

        ans = min(ans, tmp)

    print(ans if ans != float('inf') else -1)

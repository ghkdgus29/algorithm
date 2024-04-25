# 연결된 덩어리의 최대 크기 구하기
import collections


def bfs(x, y):
    visit = set()
    queue = collections.deque()
    queue.append((x, y))
    visit.add((x, y))

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] == 1 and (nx, ny) not in visit:
                    visit.add((nx, ny))
                    queue.append((nx, ny))

    return len(visit)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
ans = 0
for y in range(h):
    for x in range(w):
        if board[y][x] == 0:
            board[y][x] = 1
            ans = max(ans, bfs(x, y))
            board[y][x] = 0

print(ans)

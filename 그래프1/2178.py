import collections


def bfs(x, y):
    queue = collections.deque([])

    queue.append((x, y, 1))         # x, y 좌표와 몇 번째 거리인지를 저장
    visit[y][x] = True

    while queue:
        x, y, cnt = queue.popleft()

        if y == h - 1 and x == w - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if graph[ny][nx] == "1" and not visit[ny][nx]:
                    queue.append((nx, ny, cnt + 1))             # 거리를 추가
                    visit[ny][nx] = True


h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]
visit = [[False] * w for _ in range(h)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(bfs(0, 0))
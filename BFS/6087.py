import collections

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

NOT_VISIT = 1000_0000

w, h = map(int, input().split())
board = [list(input()) for _ in range(h)]
razor = []

for y in range(h):
    for x in range(w):
        if board[y][x] == 'C':
            board[y][x] = '.'
            razor.append((x, y))

count = [[NOT_VISIT] * w for _ in range(h)]

sx, sy = razor.pop()
queue = collections.deque()
queue.append((sx, sy))
count[sy][sx] = -1

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < w and 0 <= ny < h:      # 해당 방향으로 이동할 수 있는 지점까지 모두 방문한다.
            if board[ny][nx] == '*':
                break

            if count[ny][nx] == NOT_VISIT:
                count[ny][nx] = count[y][x] + 1     # 현재 방향에서 이동할 수 있는 모든 칸이 필요로하는 거울수는 이전 방향의 거울 수 + 1 이다.
                queue.append((nx, ny))

            nx += dx[i]
            ny += dy[i]

tx, ty = razor.pop()

print(count[ty][tx])

import collections

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

h, w = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(h)]


def bfs(sx, sy, copy_board):
    queue = collections.deque([(sx, sy)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if copy_board[ny][nx] == 0:
                    copy_board[ny][nx] = 2
                    queue.append((nx, ny))


def calculate():
    copy_board = [row[:] for row in board]

    for y in range(h):
        for x in range(w):
            if board[y][x] == 2:
                bfs(x, y, copy_board)

    safe_place = 0
    for y in range(h):
        for x in range(w):
            if copy_board[y][x] == 0:
                safe_place += 1

    return safe_place


ans = 0

for i1 in range(h * w - 2):
    if board[i1 // w][i1 % w] != 0:
        continue

    board[i1 // w][i1 % w] = 1
    for i2 in range(i1 + 1, h * w - 1):
        if board[i2 // w][i2 % w] != 0:
            continue

        board[i2 // w][i2 % w] = 1
        for i3 in range(i2 + 1, h * w):
            if board[i3 // w][i3 % w] != 0:
                continue

            board[i3 // w][i3 % w] = 1
            ans = max(ans, calculate())
            board[i3 // w][i3 % w] = 0

        board[i2 // w][i2 % w] = 0
    board[i1 // w][i1 % w] = 0

print(ans)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def go_regular(index, x, y, summ):
    if index >= 4:
        global max_val
        max_val = max(max_val, summ)
        return

    summ += board[y][x]
    visit[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < w and 0 <= ny < h:
            if not visit[ny][nx]:
                go_regular(index + 1, nx, ny, summ)

    visit[y][x] = False


def ㅜ_mask(x, y):
    if x <= w - 3 and y <= h - 2:
        global max_val
        max_val = max(max_val, board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y + 1][x + 1])


def ㅏ_mask(x, y):
    if x <= w - 2 and y <= h - 3:
        global max_val
        max_val = max(max_val, board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 1][x + 1])


def ㅗ_mask(x, y):
    if x <= w - 3 and 1 <= y:
        global max_val
        max_val = max(max_val, board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y - 1][x + 1])


def ㅓ_mask(x, y):
    if 1 <= x and y <= h - 3:
        global max_val
        max_val = max(max_val, board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 1][x - 1])


h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
visit = [[False] * w for _ in range(h)]
max_val = -1

for y in range(h):
    for x in range(w):
        go_regular(0, x, y, 0)
        ㅜ_mask(x, y)
        ㅏ_mask(x, y)
        ㅗ_mask(x, y)
        ㅓ_mask(x, y)

print(max_val)

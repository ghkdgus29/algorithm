import sys

h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def confine(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < w and 0 <= ny < h:
            if board[ny][nx] == 'S':
                return False
            elif board[ny][nx] == 'W':
                continue
            board[ny][nx] = 'D'
    return True


for y in range(h):
    for x in range(w):
        if board[y][x] == 'W':
            if not confine(x, y):
                print(0)
                sys.exit(0)

print(1)
for y in range(h):
    for x in range(w):
        print(board[y][x], end='')
    print()

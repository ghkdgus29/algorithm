import sys


def check(x, y):
    x_offset = [0, 0, -1, 1]
    y_offset = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    length = 0

    while True:
        fail_cnt = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if not (0 <= nx < w and 0 <= ny < h) or board[ny][nx] == '.':
                fail_cnt += 1

        if fail_cnt > 0:
            return length

        for i in range(4):
            check_board[y + dy[i]][x + dx[i]] = True
            dx[i] += x_offset[i]
            dy[i] += y_offset[i]

        length += 1


h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
check_board = [[-1] * w for _ in range(h)]
for y in range(h):
    for x in range(w):
        if board[y][x] == '.':
            check_board[y][x] = True
        else:
            check_board[y][x] = False

ans = []
for y in range(h):
    for x in range(w):
        if board[y][x] == '*':
            length = check(x, y)
            if length > 0:
                check_board[y][x] = True
                ans.append((y + 1, x + 1, length))

for y in range(h):
    for x in range(w):
        if not check_board[y][x]:
            print(-1)
            sys.exit()

print(len(ans))
for each in ans:
    print(*each)

# 6 8
# ....*...
# ...**...
# ..*****.
# ...**...
# ....*...
# ....*...

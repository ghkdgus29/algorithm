dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def move(count, x1, y1, x2, y2, direction):
    if count > 10:
        return

    fall1 = False
    fall2 = False

    if x1 < 0 or x1 >= w or y1 < 0 or y1 >= h:
        fall1 = True

    if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
        fall2 = True

    if fall1 and fall2:  # 둘다 떨어짐
        return

    if fall1 or fall2:  # 하나만 떨어짐
        counts.append(count)
        return

    if board[y1][x1] == '#':        # 만약 현재 위치가 벽인 경우, 이전 위치로 돌아간다.
        x1 -= dx[direction]
        y1 -= dy[direction]
    if board[y2][x2] == '#':
        x2 -= dx[direction]
        y2 -= dy[direction]

    for i in range(4):
        move(count + 1, x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i], i)


h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
counts = []

coin_position = []

for y in range(h):
    for x in range(w):
        if board[y][x] == "o":
            board[y][x] = "."
            coin_position.append(x)
            coin_position.append(y)

move(0, coin_position[0], coin_position[1], coin_position[2], coin_position[3], -1)

if counts:
    print(min(counts))
else:
    print(-1)

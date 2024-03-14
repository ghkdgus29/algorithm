def pick(picks, x, y):
    if len(picks) >= 6:
        make.add(picks)
        return

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < 5 and 0 <= ny < 5:
            pick(picks + board[ny][nx], nx, ny)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
board = [list(input().split()) for _ in range(5)]
make = set()

for y in range(5):
    for x in range(5):
        pick("", x, y)

print(len(make))

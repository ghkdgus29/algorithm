ans_list = []


def tetromino(n, total, x, y, dir):
    if n >= 3:
        ans_list.append(total)
        return

    if x + 1 < w and dir != "left":
        tetromino(n + 1, total + b[y][x + 1], x + 1, y, "right")

    if y + 1 < h and dir != "down":
        tetromino(n + 1, total + b[y + 1][x], x, y + 1, "up")

    if x - 1 >= 0 and dir != "right":
        tetromino(n + 1, total + b[y][x - 1], x - 1, y, "left")

    if y - 1 >= 0 and dir != "up":
        tetromino(n + 1, total + b[y - 1][x], x, y - 1, "down")


h, w = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h)]

for y in range(h):                              # ㅓ 모양을 제외한 나머지 블록
    for x in range(w):
        tetromino(0, b[y][x], x, y, "first")


for y in range(h - 1):                          # ㅓ 모양 블록들 (회전 포함)
    for x in range(w - 2):
        ans_list.append(b[y][x] + b[y][x + 1] + b[y][x + 2] + b[y + 1][x + 1])

for y in range(h - 2):
    for x in range(1, w):
        ans_list.append(b[y][x] + b[y + 1][x] + b[y + 1][x - 1] + b[y + 2][x])

for y in range(1, h):
    for x in range(w - 2):
        ans_list.append(b[y][x] + b[y][x + 1] + b[y - 1][x + 1] + b[y][x + 2])

for y in range(h - 2):
    for x in range(w - 1):
        ans_list.append(b[y][x] + b[y + 1][x] + b[y + 1][x + 1] + b[y + 2][x])

print(max(ans_list))

# d[y][x] = [d[y][x-1][0], d[y-1][x-1][1], d[y-1][x][2]]
# 가로, 대각, 세로

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = [[[0] * 3 for _ in range(n)] for _ in range(n)]

d[0][1][0] = 1

for x in range(2, n):
    if board[0][x] == 0:
        d[0][x][0] = d[0][x-1][0]

for y in range(1, n):
    for x in range(1, n):
        if board[y][x] == 0:
            d[y][x][0] = d[y][x - 1][0] + d[y][x - 1][1]
            d[y][x][2] = d[y - 1][x][1] + d[y - 1][x][2]
        if board[y][x] == 0 and board[y-1][x] == 0 and board[y][x-1] == 0:
            d[y][x][1] = sum(d[y - 1][x - 1])

print(sum(d[-1][-1]))

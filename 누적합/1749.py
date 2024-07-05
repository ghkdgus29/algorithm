h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
s = [[0] * (w + 1) for _ in range(h + 1)]

# s[y][x] = s[y-1][x] + s[y][x-1] + a[y][x] - s[y-1][x-1]

for y in range(1, h + 1):
    for x in range(1, w + 1):
        s[y][x] = s[y - 1][x] + s[y][x - 1] + board[y - 1][x - 1] - s[y - 1][x - 1]

ans = -float('inf')
for y in range(1, h + 1):
    for x in range(1, w + 1):
        for i in range(y):
            for j in range(x):
                ans = max(ans, s[y][x] - s[i][x] - s[y][j] + s[i][j])

print(ans)

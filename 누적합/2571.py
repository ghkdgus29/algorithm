board = [[-10000] * 100 for _ in range(100)]

for _ in range(int(input())):
    w, h = map(int, input().split())

    for y in range(h, h+10):
        for x in range(w, w+10):
            board[y][x] = 1

s = [[0] * 101 for _ in range(101)]

for y in range(1, 101):
    for x in range(1, 101):
        s[y][x] = s[y-1][x] + s[y][x-1] + board[y-1][x-1] - s[y-1][x-1]

ans = 0
for y in range(1, 101):
    for x in range(1, 101):
        for i in range(y):
            for j in range(x):
                ans = max(ans, s[y][x] - s[i][x] - s[y][j] + s[i][j])

print(ans)

# 가져갈 수 있는 사탕 개수의 최대값 구하기

# d[y][x] = max(d[y][x-1], d[y-1][x]) + a[y][x]

h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
candy = [[0] * (w + 1) for _ in range(h + 1)]

candy[1][1] = board[0][0]

for y in range(1, h + 1):
    for x in range(1, w + 1):
        candy[y][x] = max(candy[y][x - 1], candy[y - 1][x]) + board[y - 1][x - 1]

print(candy[-1][-1])

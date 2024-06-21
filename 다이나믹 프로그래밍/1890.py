# 각 칸에는 이동할 수 있는 거리가 적혀있음
# 0는 벽
# 점프 시 방향 변경 불가

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]

d[0][0] = 1
for y in range(n):
    for x in range(n):
        if y < y + a[y][x] < n:
            d[y + a[y][x]][x] += d[y][x]
        if x < x + a[y][x] < n:
            d[y][x + a[y][x]] += d[y][x]

print(d[-1][-1])

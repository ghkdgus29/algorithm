import itertools


def calculate_house_dist(hx, hy, case):
    min_dist = float('inf')
    for cx, cy in case:
        min_dist = min(min_dist, abs(hx - cx) + abs(hy - cy))
    return min_dist


n, chicken_cnt = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            house.append((x, y))
        elif board[y][x] == 2:
            chicken.append((x, y))

ans = float('inf')
for case in itertools.combinations(chicken, chicken_cnt):
    dist = 0
    for hx, hy in house:
        dist += calculate_house_dist(hx, hy, case)
    ans = min(ans, dist)

print(ans)

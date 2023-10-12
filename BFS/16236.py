import heapq

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

shark_x = shark_y = -1

for y in range(n):
    for x in range(n):
        if board[y][x] == 9:
            shark_x, shark_y = x, y
            board[y][x] = 0


def bfs(sx, sy, n, shark_size):             # 아기상어의 다음먹이 위치와 거리를 찾는 bfs
    heap = []                                           # 아기상어의 다음먹이는 가장 거리가 가깝고, 위에 있고, 왼쪽에 있어야 하므로 힙 사용
    dist = [[-1] * n for _ in range(n)]

    dist[sy][sx] = 0
    heapq.heappush(heap, (dist[sy][sx], sy, sx))

    while heap:
        _, y, x = heapq.heappop(heap)                   # 아기상어의 다음 이동 위치를 pop

        if 1 <= board[y][x] < shark_size:               # 만약 아기상어가 먹을 수 있으면 해당 먹이를 먹고 위치 및 이동거리를 반환
            return x, y, dist[y][x]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[ny][nx] == -1 and board[ny][nx] <= shark_size:
                    dist[ny][nx] = dist[y][x] + 1
                    heapq.heappush(heap, (dist[ny][nx], ny, nx))    # 아기상어의 다음 이동 위치를 heap 에 저장

    return sx, sy, 0


ans = 0
exp = 0
size = 2
while True:
    shark_x, shark_y, move_cnt = bfs(shark_x, shark_y, n, size)     # 아기상어가 먹이를 먹은 위치, 먹이를 먹기 까지의 거리 반환

    if move_cnt == 0:                       # 만약 이동거리가 0이면 더 이상 먹을 먹이가 없는 것
        break

    ans += move_cnt
    board[shark_y][shark_x] = 0
    exp += 1
    if size == exp:                         # 상어가 자신의 크기만큼 먹이를 먹으면 덩치를 키운다.
        size += 1
        exp = 0

print(ans)

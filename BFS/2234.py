import collections

dx = [0, -1, 0, 1]  # 수직 성분
dy = [-1, 0, 1, 0]  # 수평 성분
# 서쪽, 북쪽, 동쪽, 남쪽 순
# 서쪽 xxx1, 북쪽벽 xx1x, 동쪽벽 x1xx, 남쪽벽 1xxx
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * m for _ in range(n)]


def bfs(x, y, rooms):
    q = collections.deque()
    q.append((x, y))
    d[x][y] = rooms
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if d[nx][ny] == 0:
                    if (a[x][y] & (1 << k)) == 0:  # 이동방향에 벽이 없다면
                        q.append((nx, ny))
                        d[nx][ny] = rooms
    return cnt


rooms = 0
room = [0]
for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            rooms += 1
            room.append((bfs(i, j, rooms)))

print(rooms)  # 전체 방 개수

ans = 0
for i in range(1, rooms + 1):
    if ans < room[i]:
        ans = room[i]
print(ans)  # 방 최대 넓이

ans = 0
for i in range(n):
    for j in range(m):
        x, y = i, j
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if d[nx][ny] != d[x][y]:
                    if (a[x][y] & (1 << k)) > 0:  # 해당 방향에 벽이 있다면
                        ans = max(ans, room[d[x][y]] + room[d[nx][ny]])
print(ans)

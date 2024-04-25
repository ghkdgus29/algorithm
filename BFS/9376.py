import collections

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(a, x, y):       # 몇 개의 문을 열었는지 계산하는 bfs
    n = len(a)
    m = len(a[0])
    dist = [[-1] * m for _ in range(n)]
    q = collections.deque()
    q.append((x, y))
    dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and a[nx][ny] != '*':
                if a[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))          # 문을 열지 않고 가는 경우, 큐의 왼쪽에 넣어 문을 여는 방식보다 빠르게 도달한다
    return dist


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = ['.' + input() + '.' for _ in range(n)]     # 가로측 가장자리 확장
    n += 2
    m += 2
    a = ['.' * m] + a + ['.' * m]                   # 세로측 가장자리 확장
    d0 = bfs(a, 0, 0)                         # 바깥 외곽에서의 bfs
    x1 = y1 = x2 = y2 = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == '$':
                if x1 == -1:
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j
    d1 = bfs(a, x1, y1)                             # 첫 번째 죄수
    d2 = bfs(a, x2, y2)                             # 두 번째 죄수
    ans = float('inf')

    for i in range(n):
        for j in range(m):                              # 3개의 bfs 결과물이 만나는 지점 중 가장 최소의 문을 여는 지점을 찾는다.
            if a[i][j] == '*':
                continue
            if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
                continue
            cur = d0[i][j] + d1[i][j] + d2[i][j]
            if a[i][j] == '#':                          # 현재 지점이 문이라면, 두 사람이 중복해서 열었으므로 -2를 해준다.
                cur -= 2
            ans = min(ans, cur)
    print(ans)

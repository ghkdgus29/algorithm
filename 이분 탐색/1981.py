import collections

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, minimum, maximum):                       # 시작지점부터 도착지점까지의 경로값들이 최소값과 최대값내에 존재하는지 판별
    if minimum > a[0][0] or maximum < a[0][0]:
        return False
    n = len(a)
    visit = [[False] * n for _ in range(n)]
    queue = collections.deque()
    queue.append((0, 0))
    visit[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[ny][nx] and minimum <= a[ny][nx] <= maximum:   # 다음 노드를 방문하지 않았고, 다음 노드 값이 최소값과 최대값사이에 있다면 이동
                    queue.append((nx, ny))
                    visit[ny][nx] = True

    return visit[-1][-1]            # 만약 도착지점을 도착하지 못했다면, False 가 반환된다.


def check(a, diff):         # 주어진 차이값을 그래프가 만족할 수 있는지 판별
    for minimum in range(200 - diff + 1):       # 최소값을 0 ~ 200-diff 까지 반복
        if bfs(a, minimum, minimum + diff):     # 최소값과 최대값을 반복하여 bfs 판별
            return True
    return False


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
left = 0
right = 200
ans = -1
while left <= right:                    # 최대값과 최소값의 차이를 이분 탐색
    mid = (left + right) // 2
    if check(a, mid):               # 해당 차이를 만족할 수 있다면, 차이를 더 줄여본다.
        right = mid - 1
        ans = mid
    else:                           # 해당 차이를 만족할 수 없다면, 차이를 더 늘린다.
        left = mid + 1

print(ans)

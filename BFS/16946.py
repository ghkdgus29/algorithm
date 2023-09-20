import collections

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
h, w = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(h)]

group = [[-1] * w for _ in range(h)]                # 빈 칸이 몇 번 그룹에 속해있는지 판별하기 위한 리스트
visit = [[False] * w for _ in range(h)]
group_size = []                                     # 해당 그룹이 총 몇 개의 빈 칸으로 이루어졌는지 나타내는 리스트


def bfs(sx, sy):
    group_idx = len(group_size)                     # 그룹 번호 설정
    queue = collections.deque()
    queue.append((sx, sy))
    group[sy][sx] = group_idx
    visit[sy][sx] = True
    group_cnt = 1

    while queue:                                    # 인접한 빈 칸들을 모두 같은 그룹 번호로 묶는다.
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if not visit[ny][nx] and board[ny][nx] == 0:        # 방문하지 않은 빈칸인 경우
                    visit[ny][nx] = True
                    group[ny][nx] = group_idx
                    queue.append((nx, ny))
                    group_cnt += 1                      # 그룹에 해당하는 빈 칸의 개수를 계산

    group_size.append(group_cnt)                        # 그룹 크기 리스트에 현재 그룹의 빈칸 개수를 추가


for y in range(h):
    for x in range(w):
        if board[y][x] == 0 and not visit[y][x]:        # 빈칸인 경우, 그룹으로 묶기
            bfs(x, y)

for y in range(h):
    for x in range(w):          # 반복문을 돌면서, 벽인 경우 인접한 4칸의 그룹을 조사하여 갈 수 있는 칸 수를 계산
        if board[y][x] == 0:                      # 빈 칸인 경우
            print(0, end='')
        else:                                     # 벽인 경우
            near_group = set()                                  # 인접 그룹을 묶기 위한 set
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < w and 0 <= ny < h:
                    if board[ny][nx] == 0:                      # 만약 인접 영역이 빈칸이면, 해당 영역의 그룹 번호를 인접 그룹 set에 추가
                        near_group.add(group[ny][nx])
            ans = 1
            for group_idx in near_group:                        # 인접 그룹 영역의 개수들을 모두 정답에 더한다.
                ans += group_size[group_idx]
            print(ans % 10, end='')
    print()

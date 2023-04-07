import collections


def bfs(s_x, s_y, e_x, e_y):
    d = [[-1] * length for _ in range(length)]      # -1로 모두 초기화, -1은 방문하지 않음을 나타내기도 함
    queue = collections.deque()

    queue.append((s_x, s_y))
    d[s_y][s_x] = 0

    while queue:
        x, y = queue.popleft()

        if x == e_x and y == e_y:
            return d[y][x]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length:
                if d[ny][nx] == -1:
                    queue.append((nx, ny))
                    d[ny][nx] = d[y][x] + 1         # 다음 이동 횟수 = 이전 이동 횟수 + 1


dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]       # 나이트 이동 방향

t = int(input())

for _ in range(t):
    length = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    print(bfs(start_x, start_y, end_x, end_y))

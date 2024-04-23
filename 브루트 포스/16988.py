# 주어진 판에서 돌 2개를 두어 죽일 수 있는 상대돌의 최대개수를 구하라
# 1 <- 내꺼, 2 <- 상대꺼
import collections

h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
ans = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def check_die():
    visit = [[False] * w for _ in range(h)]
    total_cnt = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] == 2 and not visit[y][x]:
                cnt = 0
                dead = True
                queue = collections.deque()
                queue.append((x, y))
                visit[y][x] = True
                while queue:
                    cnt += 1
                    xx, yy = queue.pop()
                    for i in range(4):
                        nx = dx[i] + xx
                        ny = dy[i] + yy
                        if 0 <= nx < w and 0 <= ny < h:
                            if board[ny][nx] == 2 and not visit[ny][nx]:
                                queue.append((nx, ny))
                                visit[ny][nx] = True
                            elif board[ny][nx] == 0:
                                dead = False
                if dead:
                    total_cnt += cnt
    return total_cnt


for y1 in range(h):
    for x1 in range(w):
        if board[y1][x1] == 0:
            board[y1][x1] = 1

            for y2 in range(h):
                for x2 in range(w):
                    if x1 == x2 and y1 == y2:
                        continue
                    if board[y2][x2] == 0:
                        board[y2][x2] = 1

                        ans = max(ans, check_die())

                        board[y2][x2] = 0

            board[y1][x1] = 0

print(ans)

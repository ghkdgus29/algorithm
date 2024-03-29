dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def inside(x, y):
    return (0 <= x < w and 0 <= y < h)


def can_go(x, y, visit):
    return inside(x, y) and board[y][x] == '.' and not visit[y][x]


def check_end(visit):
    for y in range(h):
        for x in range(w):
            if board[y][x] == '.':
                if not visit[y][x]:
                    return False
    return True


def go(x, y, dir, cnt, visit):
    visit[y][x] = True
    if check_end(visit):
        global ans
        ans = min(ans, cnt)
        visit[y][x] = False
        return
    nx = dx[dir] + x
    ny = dy[dir] + y

    if can_go(nx, ny, visit):
        go(nx, ny, dir, cnt, visit)
    else:
        for i in range(4):
            nnx = dx[i] + x
            nny = dy[i] + y
            if can_go(nnx, nny, visit):
                go(nnx, nny, i, cnt + 1, visit)

    visit[y][x] = False


def one_spot():
    cnt = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] == '.':
                cnt += 1
    return cnt == 1


case_cnt = 0
while True:
    case_cnt += 1
    try:
        ans = float('inf')
        h, w = map(int, input().split())
        board = [list(input()) for _ in range(h)]
        visit = [[False] * w for _ in range(h)]

        for y in range(h):
            for x in range(w):
                if board[y][x] == '.':
                    for i in range(4):
                        nx = dx[i] + x
                        ny = dy[i] + y
                        if can_go(nx, ny, visit):
                            go(x, y, i, 1, visit)

        if ans == float('inf'):
            ans = -1

        if one_spot():
            ans = 0

        print("Case " + str(case_cnt) + ": " + str(ans))

    except EOFError:
        break

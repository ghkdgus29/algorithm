dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
LIMIT = 10


class Result:
    def __init__(self, moved, hole, x, y):
        self.moved = moved                          # 구슬이 움직일 수 있음을 의미
        self.hole = hole                            # 구슬이 구멍에 들어감을 의미
        self.x = x
        self.y = y


def gen(k):                             # 들어온 k 값을 4진수 10자리로 변환
    a = [0] * LIMIT                     # a[0] -> LSB, a[9] -> MSB
    for i in range(LIMIT):
        a[i] = (k & 3)
        k >>= 2
    return a


def simulate(a, k, x, y):                       # 구슬 이동
    if a[y][x] == '.':                          # 구슬이 이미 hole 에 들어간 경우
        return Result(False, False, x, y)

    moved = False
    while True:
        nx, ny = x + dx[k], y + dy[k]
        ch = a[ny][nx]
        if ch == '#':                                       # 구슬이 벽돌을 만난 경우
            return Result(moved, False, x, y)
        elif ch in 'RB':                                    # 구슬이 다른 구슬을 만난 경우
            return Result(moved, False, x, y)
        elif ch == '.':                                     # 이동할 수 있는 빈칸인 경우
            a[y][x], a[ny][nx] = a[ny][nx], a[y][x]
            x, y = nx, ny
            moved = True
        elif ch == 'O':                                     # 구슬이 구멍에 빠진 경우
            a[y][x] = '.'
            moved = True
            return Result(moved, True, x, y)


def check(a, dirs):                             # 구슬을 이동시킨 횟수를 계산하는 메서드
    h = len(a)
    w = len(a[0])
    rx, ry = 0, 0
    bx, by = 0, 0

    for y in range(h):                          # 구슬 위치 찾기
        for x in range(w):
            if a[y][x] == 'R':
                rx, ry = x, y
            elif a[y][x] == 'B':
                bx, by = x, y

    cnt = 0
    for k in dirs:                              # 방향 배열 (4진법 배열) 순서대로 구슬판 기울이기, 최대 10번의 방향 변경
        cnt += 1
        hole1 = hole2 = False
        while True:                         # 모든 구슬이 멈출때까지 반복 이동시키기 위해 무한 반복 while 문 사용
            p1 = simulate(a, k, rx, ry)
            rx, ry = p1.x, p1.y                 # 빨간 구슬 위치 갱신

            p2 = simulate(a, k, bx, by)
            bx, by = p2.x, p2.y                 # 파란 구슬 위치 갱신

            if not p1.moved and not p2.moved:       # 두 구슬이 모두 이동을 멈추면 반복문 탈출
                break
            if p1.hole:
                hole1 = True
            if p2.hole:
                hole2 = True

        if hole2:                               # 파란 구슬이 빠진 경우 정답이 될 수 없다.
            return -1
        if hole1:                               # 빨간 구슬이 빠진 경우
            return cnt

    return -1           # 10번의 방향 변경이 끝났음에도 구슬을 넣지 못한 경우 정답이 될 수 없다.


def valid(dirs):                                        # 방향 배열중 의미 없는 방향 배열을 솎아 낸다.
    l = len(dirs)
    for i in range(l - 1):
        if dirs[i] == 0 and dirs[i + 1] == 1:           # 아래쪽으로 이동한 다음, 위쪽으로 바로 이동하는 것은 의미가 없다.
            return False
        if dirs[i] == 1 and dirs[i + 1] == 0:           # 위쪽으로 이동한 다음, 아래쪽으로 바로 이동하는 것은 의미가 없다.
            return False
        if dirs[i] == 2 and dirs[i + 1] == 3:           # 오른쪽으로 이동한 다음, 왼쪽으로 바로 이동하는 것은 의미가 없다.
            return False
        if dirs[i] == 3 and dirs[i + 1] == 2:           # 왼쪽으로 이동한 다음, 오른쪽으로 바로 이동하는 것은 의미가 없다.
            return False
        if dirs[i] == dirs[i + 1]:                      # 같은 방향으로 두번 이동하는 것은 의미가 없다.
            return False
    return True


n, m = map(int, input().split())
original = [input() for _ in range(n)]
ans = -1
for k in range(1 << (LIMIT * 2)):               # 0 ~ 4^10-1 까지 k를 돌린다.
    dirs = gen(k)
    if not valid(dirs):                         # 의미 없는 방향 배열에 대해 계산하지 않는다.
        continue
    a = [list(row) for row in original]
    cur = check(a, dirs)
    if cur == -1:
        continue
    if ans == -1 or ans > cur:
        ans = cur                               # 최소 횟수를 구한다.

print(ans)

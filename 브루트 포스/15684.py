import sys

LEFT, RIGHT = 1, 2


def start(c):                       # c번째에서 출발해서 도착한 사다리 지점을 반환
    r = 1
    while r <= h:                   # r = 현재 높이, h = 전체 높이
        if garo[r][c] == LEFT:
            c += 1
        elif garo[r][c] == RIGHT:
            c -= 1
        r += 1
    return c


def go():                       # 사다리 검사
    for i in range(1, w):
        res = start(i)
        if res != i:
            return False
    return True


w, m, h = map(int, input().split())
garo = [[0] * (w + 1) for _ in range(h + 1)]
for _ in range(m):  # 가로선 잇기
    x, y = map(int, input().split())
    garo[x][y] = LEFT
    garo[x][y + 1] = RIGHT

a = []
for i in range(1, h + 1):
    for j in range(1, w):
        if garo[i][j] != 0:  # 고른 칸의 왼쪽, 고른 칸에 가로선이 있는 경우
            continue
        if garo[i][j + 1] != 0:  # 고른 칸의 오른쪽에 가로선이 있는 경우
            continue
        a.append((i, j))  # 고를 수 있는 가로선 경우의 수 모으기

ans = float('inf')
if go():  # 가로선을 만들지 않아도 되는 경우
    print(0)
    sys.exit(0)

for i in range(len(a)):         # i 번째 칸에 첫 번째 가로선 설치
    x1, y1 = a[i]
    if garo[x1][y1] != 0 or garo[x1][y1 + 1] != 0:
        continue

    garo[x1][y1] = LEFT
    garo[x1][y1 + 1] = RIGHT
    if go():                    # 첫 번째 가로선을 설치한 후 검사
        ans = min(ans, 1)

    for j in range(i + 1, len(a)):    # j 번째 칸에 두 번째 가로선 설치
        x2, y2 = a[j]
        if garo[x2][y2] != 0 or garo[x2][y2 + 1] != 0:
            continue
        garo[x2][y2] = LEFT
        garo[x2][y2 + 1] = RIGHT
        if go():                      # 두 번째 가로선을 설치한 후 검사
            ans = min(ans, 2)

        for k in range(j + 1, len(a)):  # k 번째 칸에 두 번째 가로선 설치
            x3, y3 = a[k]
            if garo[x3][y3] != 0 or garo[x3][y3 + 1] != 0:
                continue
            garo[x3][y3] = LEFT
            garo[x3][y3 + 1] = RIGHT
            if go():                    # 세 번째 가로선을 설치한 후 검사
                ans = min(ans, 3)

            garo[x3][y3] = 0        # roll back
            garo[x3][y3 + 1] = 0
        garo[x2][y2] = 0
        garo[x2][y2 + 1] = 0
    garo[x1][y1] = 0
    garo[x1][y1 + 1] = 0
print(ans if ans != float('inf') else -1)

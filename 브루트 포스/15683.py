dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def check(origin, copy, x, y, dir):             # 한 방향으로 칠하기
    h = len(origin)
    w = len(origin[0])

    while 0 <= y < h and 0 <= x < w:
        if origin[y][x] == 6:
            break
        copy[y][x] = 1
        x += dx[dir]
        y += dy[dir]


def go(origin, cctv, index, dirs):
    if len(cctv) == index:
        h = len(origin)
        w = len(origin[0])
        copy = [row[:] for row in origin]
        for i, (what, x, y) in enumerate(cctv):
            if what == 1:
                check(origin, copy, x, y, dirs[i])              # cctv 1
            elif what == 2:
                check(origin, copy, x, y, dirs[i])
                check(origin, copy, x, y, (dirs[i] + 2) % 4)    # cctv 2
            elif what == 3:
                check(origin, copy, x, y, dirs[i])
                check(origin, copy, x, y, (dirs[i] + 1) % 4)    # cctv 3
            elif what == 4:
                check(origin, copy, x, y, dirs[i])
                check(origin, copy, x, y, (dirs[i] + 1) % 4)
                check(origin, copy, x, y, (dirs[i] + 2) % 4)    # cctv 4
            elif what == 5:
                check(origin, copy, x, y, dirs[i])
                check(origin, copy, x, y, (dirs[i] + 1) % 4)
                check(origin, copy, x, y, (dirs[i] + 2) % 4)
                check(origin, copy, x, y, (dirs[i] + 3) % 4)    # cctv 5
        cnt = 0

        for i in range(h):
            for j in range(w):
                if copy[i][j] == 0:
                    cnt += 1

        return cnt

    ans = 100
    for i in range(4):
        temp = go(origin, cctv, index + 1, dirs + [i])      # 4가지 방향을 넣어가며 재귀
        if ans > temp:
            ans = temp
    return ans


h, w = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(h)]
cctv = []

for y in range(h):
    for x in range(w):
        if 1 <= origin[y][x] <= 5:
            cctv.append((origin[y][x], x, y))               # cctv 넣기

print(go(origin, cctv, 0, []))

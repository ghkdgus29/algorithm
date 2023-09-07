LIMIT = 5

DOWN = 0
UP = 1
LEFT = 2
RIGHT = 3


def gen(k):                         # 4진법 변환을 통해 방향 배열 생성
    a = [0] * LIMIT
    for i in range(LIMIT):
        a[i] = (k & 3)
        k >>= 2
    return a


def check(a, dirs):
    d = [row[:] for row in a]

    for dir in dirs:                                        # 방향 배열의 방향들을 반복 순회
        merged = [[False] * n for _ in range(n)]                # 병합 여부 체크

        while True:                                                 # 더 이상 블록들을 움직일 수 없는 경우까지 반복
            movable = False                                     # 블록들을 더 움직일 수 있는지 여부
            if dir == DOWN:                                   # 아래로 블록들 이동
                for y in range(n - 2, -1, -1):                  # 맨 아래부터 블록 검사 (맨 아래에서 한칸 위부터 시작해서 위로 검사)
                    for x in range(n):
                        if d[y][x] == 0:                        # 현재블록이 0 인 경우
                            continue
                        if d[y + 1][x] == 0:                    # 현재블록이 0이 아니고, 아래가 비어 있는 경우, 현재블록을 아래로 이동
                            d[y + 1][x] = d[y][x]
                            merged[y + 1][x] = merged[y][x]
                            d[y][x] = 0
                            movable = True
                        elif d[y + 1][x] == d[y][x]:                        # 현재블록이 0이 아니고, 바로 아래 블록이 현재블록과 같은 경우
                            if not merged[y][x] and not merged[y + 1][x]:   # 현재블록과 바로 아래블록이 한번도 병합하지 않은 블록인 경우, 병합
                                d[y + 1][x] *= 2
                                merged[y + 1][x] = True
                                d[y][x] = 0
                                movable = True
            elif dir == UP:                                 # 위로 블록들 이동
                for y in range(1, n):
                    for x in range(n):
                        if d[y][x] == 0:
                            continue
                        if d[y - 1][x] == 0:
                            d[y - 1][x] = d[y][x]
                            merged[y - 1][x] = merged[y][x]
                            d[y][x] = 0
                            movable = True
                        elif d[y - 1][x] == d[y][x]:
                            if not merged[y][x] and not merged[y - 1][x]:
                                d[y - 1][x] *= 2
                                merged[y - 1][x] = True
                                d[y][x] = 0
                                movable = True
            elif dir == LEFT:                              # 왼쪽으로 블록들 이동
                for x in range(1, n):
                    for y in range(n):
                        if d[y][x] == 0:
                            continue
                        if d[y][x - 1] == 0:
                            d[y][x - 1] = d[y][x]
                            merged[y][x - 1] = merged[y][x]
                            d[y][x] = 0
                            movable = True
                        elif d[y][x - 1] == d[y][x]:
                            if not merged[y][x] and not merged[y][x - 1]:
                                d[y][x - 1] *= 2
                                merged[y][x - 1] = True
                                d[y][x] = 0
                                movable = True
            elif dir == RIGHT:                          # 오른쪽으로 블록들 이동
                for x in range(n - 2, -1, -1):
                    for y in range(n):
                        if d[y][x] == 0:
                            continue
                        if d[y][x + 1] == 0:
                            d[y][x + 1] = d[y][x]
                            merged[y][x + 1] = merged[y][x]
                            d[y][x] = 0
                            movable = True
                        elif d[y][x + 1] == d[y][x]:
                            if not merged[y][x] and not merged[y][x + 1]:
                                d[y][x + 1] *= 2
                                merged[y][x + 1] = True
                                d[y][x] = 0
                                movable = True
            if not movable:                             # 블록들이 이동할 수 있는 빈칸이나, 병합할 수 있는 블록들이 없는 경우, 반복문 탈출
                break

    max_val = max([max(row) for row in d])              # 블록에서 최대값 반환
    return max_val


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for k in range(4 ** LIMIT):
    dirs = gen(k)
    ans = max(ans, check(board, dirs))

print(ans)

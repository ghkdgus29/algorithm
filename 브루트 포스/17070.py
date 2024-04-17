import sys


def check(x, y, state):
    if state == HORIZONTAL:
        return board[y][x - 1] == board[y][x] == 0
    elif state == DIAGONAL:
        return board[y][x] == board[y - 1][x] == board[y][x - 1] == board[y - 1][x - 1] == 0
    else:
        return board[y][x] == board[y - 1][x] == 0


def go(x, y, state):
    if x == y == n - 1:
        global ans
        ans += 1
        return

    for dx, dy, next_state in direction[state]:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < n and 0 <= ny < n:
            if check(nx, ny, next_state):
                go(nx, ny, next_state)


HORIZONTAL = 'horizontal'
DIAGONAL = 'diagonal'
VERTICAL = 'vertical'

ans = 0
direction = {HORIZONTAL: [(1, 0, HORIZONTAL), (1, 1, DIAGONAL)],
             DIAGONAL: [(0, 1, VERTICAL), (1, 1, DIAGONAL), (1, 0, HORIZONTAL)],
             VERTICAL: [(0, 1, VERTICAL), (1, 1, DIAGONAL)]}
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

go(1, 0, HORIZONTAL)

print(ans)

# 파이썬 시간초과 컷이 빡세서, 위 코드는 75% 정도에서 실패함
# 파이썬 통과코드는 현재 방향에서, 정확하게 더 봐야하는 칸들만 체크해줘야 통과함
# 시간복잡도와 상관없고, 많은 분기가 생겨 코드 가독성이 떨어지므로 해당 답은 아래에 첨부만 함


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def go(x, y, direction):
    if x == n - 1 and y == n - 1:
        return 1
    ans = 0
    if direction == 0:  # -
        if y + 1 < n and a[x][y + 1] == 0:
            ans += go(x, y + 1, 0)
        if x + 1 < n and y + 1 < n and a[x][y + 1] == 0 and a[x + 1][y] == 0 and a[x + 1][y + 1] == 0:
            ans += go(x + 1, y + 1, 1)
    elif direction == 1:  # dig
        if y + 1 < n and a[x][y + 1] == 0:
            ans += go(x, y + 1, 0)
        if x + 1 < n and a[x + 1][y] == 0:
            ans += go(x + 1, y, 2)
        if x + 1 < n and y + 1 < n and a[x][y + 1] == 0 and a[x + 1][y] == 0 and a[x + 1][y + 1] == 0:
            ans += go(x + 1, y + 1, 1)
    elif direction == 2:  # |
        if x + 1 < n and a[x + 1][y] == 0:
            ans += go(x + 1, y, 2)
        if x + 1 < n and y + 1 < n and a[x][y + 1] == 0 and a[x + 1][y] == 0 and a[x + 1][y + 1] == 0:
            ans += go(x + 1, y + 1, 1)
    return ans


print(go(0, 1, 0))

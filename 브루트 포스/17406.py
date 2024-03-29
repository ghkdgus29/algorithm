import copy
import itertools


def rotate(origin_board, copy_board, sx, sy, ex, ey):
    n = ex - sx + 1
    if n == 1:
        return copy.deepcopy(copy_board), copy_board

    for x in range(sx + 1, ex + 1):
        copy_board[sy][x] = origin_board[sy][x - 1]

    for y in range(sy + 1, ey + 1):
        copy_board[y][ex] = origin_board[y - 1][ex]

    for x in range(ex - 1, sx - 1, -1):
        copy_board[ey][x] = origin_board[ey][x + 1]

    for y in range(ey - 1, sy - 1, -1):
        copy_board[y][sx] = origin_board[y + 1][sx]

    return rotate(origin_board, copy_board, sx + 1, sy + 1, ex - 1, ey - 1)


def find_row_min(board):
    ans = float('inf')

    for row in board:
        ans = min(ans, sum(row))

    return ans


h, w, count = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
rotate_calculations = []
for _ in range(count):
    rotate_calculations.append(list(map(int, input().split())))

ans = float('inf')
for calculations in itertools.permutations(rotate_calculations):
    origin_board = copy.deepcopy(board)
    copy_board = copy.deepcopy(board)
    for r, c, s in calculations:
        r -= 1
        c -= 1
        origin_board, copy_board = rotate(origin_board, copy_board, c - s, r - s, c + s, r + s)
    ans = min(ans, find_row_min(copy_board))

print(ans)

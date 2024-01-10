def make_star(board, x, y, size):
    if size <= 3:
        for i in range(3):
            board[y][x + i] = True

            if i != 1:
                board[y + 1][x + i] = True

            board[y + 2][x + i] = True
        return

    for y_offset in range(0, size, size // 3):
        for x_offset in range(0, size, size // 3):
            if x_offset == size // 3 and y_offset == size // 3:
                continue
            make_star(board, x + x_offset, y + y_offset, size // 3)


n = int(input())
board = [[False] * n for _ in range(n)]
make_star(board, 0, 0, n)

for y in range(n):
    for x in range(n):
        if board[y][x] is True:
            print('*', end='')
        else:
            print(' ', end='')
    print()

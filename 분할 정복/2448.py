def star(x, y, height):     # 가장 위의 꼭지점 좌표가 입력으로 들어온다.
    if height == 3:             # 높이가 3인 경우 제일 작은 삼각형
        board[y][x] = True                                  # 첫 번째 줄
        board[y + 1][x - 1] = board[y + 1][x + 1] = True    # 두 번째 줄
        for i in range(x - 2, x + 3):                       # 세 번재 줄
            board[y + 2][i] = True

        return

    star(x, y, height // 2)                                 # 큰 삼각형의 윗 삼각형
    star(x - height // 2, y + height // 2, height // 2)     # 큰 삼각형의 왼쪽 아래 삼각형
    star(x + height // 2, y + height // 2, height // 2)     # 큰 삼각형의 오른쪽 아래 삼각형


n = int(input())
board = [[False] * (n * 2 - 1) for _ in range(n)]
star(n - 1, 0, n)

for y in range(n):
    for x in range(2 * n - 1):
        if board[y][x]:
            print('*', end='')
        else:
            print(' ', end='')
    print()

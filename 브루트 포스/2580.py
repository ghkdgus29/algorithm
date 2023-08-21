def square(x, y):
    return (y // 3) * 3 + (x // 3)


def go(board_number):           # board_number는 board의 몇 번째 칸인지를 나타낸다. 0 ~ 80 번 까지의 보드 번호가 존재한다.
    if board_number == 81:              # board 가 성공적으로 완성
        for y in range(9):
            print(*board[y])
        return True

    y = board_number // 9               # board_number 로 y 값 구하기
    x = board_number % 9                # board_number 로 x 값 구하기
    if board[y][x] != 0:
        return go(board_number + 1)         # 만약 현재 칸이 0이 아니라면 바로 다음칸으로 이동

    else:
        for i in range(1, 10):
            if check_row[y][i] == False and check_col[x][i] == False and check_square[square(x, y)][i] == False:                # 만약 숫자 i 가 입력가능하다면,
                check_row[y][i] = check_col[x][i] = check_square[square(x, y)][i] = True            # 숫자 i 가 있음을 체크
                board[y][x] = i                                                                     # 숫자 i 를 board 에 입력

                if go(board_number + 1):                # 만약 board 가 성공적으로 완성되면
                    return True                         # 더 이상 로직을 진행하지 않는다.

                board[y][x] = 0                                                                     # board 가 성공적으로 진행되지 않았으므로, 0으로 다시 초기화
                check_row[y][i] = check_col[x][i] = check_square[square(x, y)][i] = False           # 숫자 i 를 체크한 것을 다시 원상태로 복귀
    return False            # 제대로 board 가 완성되지 못함


board = [list(map(int, input().split())) for _ in range(9)]
check_row = [[False] * 10 for _ in range(9)]                        # n 번째 row 에 1 ~ 9 중 어떤 숫자가 있는 지 체크
check_col = [[False] * 10 for _ in range(9)]                        # n 번째 col 에 1 ~ 9 중 어떤 숫자가 있는 지 체크
check_square = [[False] * 10 for _ in range(9)]                     # n 번째 3x3 정사각형에 1 ~ 9 중 어떤 숫자가 있는 지 체크

for y in range(9):
    for x in range(9):
        if board[y][x] != 0:
            check_row[y][board[y][x]] = True
            check_col[x][board[y][x]] = True
            check_square[square(x, y)][board[y][x]] = True          # board 에 이미 존재하는 숫자들에 대해 체크

go(0)

def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row + col]:
        return False
    if check_dig2[row - col + n - 1]:
        return False

    return True


def calc(row):
    if row == n:                                        # 모든 row 의 퀸 위치를 결정하면 종료
        return 1

    ans = 0
    for col in range(n):                                # 어떤 column 에 퀸을 놓을지 for 문 반복
        if check(row, col):                                     # 만약 다른 퀸들이 접근할 수 없으면
            check_dig[row + col] = True
            check_dig2[row - col + n - 1] = True
            check_col[col] = True
            board[row][col] = True                              # 현재 위치에서 (board[row][col]) 퀸이 갈 수 있는 지역들을 체크

            ans += calc(row + 1)                                # 이번 row 의 퀸의 위치가 정해지면, 다음 row 로 내려간다.

            check_dig[row + col] = False
            check_dig2[row - col + n - 1] = False
            check_col[col] = False
            board[row][col] = False                             # 재귀 동작이 끝나면 다시 원상복귀

    return ans


n = int(input())
ans = 0
board = [[False] * n for _ in range(n)]
check_col = [False] * n                                 # 세로열에 퀸이 존재하는지 체크
check_dig = [False] * (2 * n)                           # ↗ 대각선에 퀸이 존재하는지 체크
check_dig2 = [False] * (2 * n)                          # ↖ 대각선에 퀸이 존재하는지 체크
print(calc(0))

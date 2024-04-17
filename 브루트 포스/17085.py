h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
ans = 0

for y1 in range(h):
    for x1 in range(w):
        s1 = 0
        while True:
            if y1 - s1 < 0 or y1 + s1 >= h:
                break
            if x1 - s1 < 0 or x1 + s1 >= w:
                break
            if board[y1 - s1][x1] != '#' or board[y1 + s1][x1] != '#':
                break
            if board[y1][x1 - s1] != '#' or board[y1][x1 + s1] != '#':
                break

            board[y1 - s1][x1] = board[y1 + s1][x1] = board[y1][x1 - s1] = board[y1][x1 + s1] = '*'     # 첫 번째 십자가 결정

            for y2 in range(h):
                for x2 in range(w):
                    s2 = 0
                    while True:
                        if y2 - s2 < 0 or y2 + s2 >= h:
                            break
                        if x2 - s2 < 0 or x2 + s2 >= w:
                            break
                        if board[y2 - s2][x2] != '#' or board[y2 + s2][x2] != '#':
                            break
                        if board[y2][x2 - s2] != '#' or board[y2][x2 + s2] != '#':
                            break

                        area = (4 * s1 + 1) * (4 * s2 + 1)                          # 두 번째 십자가 결정 후 넓이 계산

                        ans = max(ans, area)

                        s2 += 1
            s1 += 1

        s1 = 0                                                                      # 첫 번째 십자가 그린 부분을 다시 지우기
        while True:
            if y1 - s1 < 0 or y1 + s1 >= h:
                break
            if x1 - s1 < 0 or x1 + s1 >= w:
                break
            if board[y1 - s1][x1] != '*' or board[y1 + s1][x1] != '*':
                break
            if board[y1][x1 - s1] != '*' or board[y1][x1 + s1] != '*':
                break

            board[y1 - s1][x1] = board[y1 + s1][x1] = board[y1][x1 - s1] = board[y1][x1 + s1] = '#'
            s1 += 1

print(ans)

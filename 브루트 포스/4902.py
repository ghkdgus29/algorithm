def calc(row, left_column, right_column, sum):
    if row < 1 or row > n:
        return
    if left_column < 1 or right_column > 2 * row - 1:
        return
    sum += s[row][right_column] - s[row][left_column - 1]       # left 삼각형부터 right 삼각형까지의 한 줄씩 더한다.
    global ans
    ans = max(ans, sum)
    if left_column % 2 == 0:                                # 역삼각형
        calc(row - 1, left_column - 2, right_column, sum)
    else:                                                   # 삼각형
        calc(row + 1, left_column, right_column + 2, sum)


tc = 0
while True:
    tc += 1
    inputs = list(map(int, input().split()))
    n = inputs[0]
    if n == 0:
        break
    ans = float('-inf')
    a = [[]]                # 삼각형
    s = [[]]                # 삼각형 누적합
    k = 1
    for i in range(1, n + 1):
        a.append([0] * (2 * i))
        s.append([0] * (2 * i))
        for j in range(1, 2 * i):
            a[i][j] = inputs[k]
            k += 1
            s[i][j] = s[i][j - 1] + a[i][j]
    for i in range(1, n + 1):               # 시작할 삼각형의 row 결정
        for j in range(1, 2 * i):           # 시작할 삼각형의 column 결정 (row가 커질수록 선택할 수 있는 삼각형이 많아짐)
            calc(i, j, j, 0)
    print(str(tc) + '. ' + str(ans))

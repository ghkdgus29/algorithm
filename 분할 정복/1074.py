def split(n, x, y):
    if n == 1:
        return 2 * y + x

    else:
        if x < 2 ** (n - 1):
            if y < 2 ** (n - 1):                                                # 왼쪽 위, 분할된 정사각형에 위치
                return split(n - 1, x, y)
            else:                                                               # 왼쪽 아래, 분할된 정사각형에 위치
                return split(n - 1, x, y - (2 ** (n - 1))) + 2 ** (2 * n - 2) * 2                   # 분할된 정사각형 2개가 뒤에 있다.
        else:
            if y < 2 ** (n - 1):                                                # 오른쪽 위, 분할된 정사각형에 위치
                return split(n - 1, x - (2 ** (n - 1)), y) + 2 ** (2 * n - 2)                          # 분할된 정사각형 1개가 뒤에 있다.
            else:                                                               # 오른쪽 아래, 분할된 정사각형에 위치
                return split(n - 1, x - (2 ** (n - 1)), y - (2 ** (n - 1))) + 2 ** (2 * n - 2) * 3  # 분할된 정사각형 3개가 뒤에 있다.


n, y, x = map(int, input().split())
print(split(n, x, y))

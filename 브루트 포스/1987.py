dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def go(x, y):
    check[ord(board[y][x]) - ord('A')] = True
    ans = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if not check[ord(board[ny][nx]) - ord('A')]:
                ans = max(go(nx, ny), ans)

    check[ord(board[y][x]) - ord('A')] = False
    return ans + 1


h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
check = [False] * 26

print(go(0, 0))

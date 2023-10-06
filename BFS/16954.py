import collections
import copy

dx = [0, 1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

board = [(list(input())) for _ in range(8)]
boards = []

for i in range(8):
    boards.append(copy.deepcopy(board))

    board.pop()
    board.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])

visit = [[False] * 8 for _ in range(8)]

queue = collections.deque()
queue.append((0, 7, 0))

while queue:
    x, y, t = queue.popleft()

    if t >= 8:
        visit[0][7] = 1
        break

    if boards[t][y][x] == '#':
        continue

    for i in range(9):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 8 and 0 <= ny < 8:
            if boards[t][ny][nx] == '.':
                queue.append((nx, ny, t + 1))

print(1 if visit[0][7] else 0)

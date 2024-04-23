# 매직 스퀘어로 변경하는 비용의 최솟값을 구하라

def is_magic_square(matrix):
    fivot = sum(matrix[0])
    if not (fivot == sum(matrix[1]) == sum(matrix[2])):
        return False

    for x in range(3):
        col = 0
        for y in range(3):
            col += matrix[y][x]
        if col != fivot:
            return False

    dig1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
    dig2 = matrix[0][2] + matrix[1][1] + matrix[2][0]

    if not (fivot == dig1 == dig2):
        return False

    return True


def calculate_cost(matrix):
    cost = 0
    for y in range(3):
        for x in range(3):
            cost += abs(matrix[y][x] - board[y][x])
    return cost


def pick(a):
    if len(a) == 9:
        matrix = [a[0:3], a[3:6], a[6:9]]
        if is_magic_square(matrix):
            global ans
            ans = min(ans, calculate_cost(matrix))
        return

    for i in range(1, 10):
        if i not in a:
            pick(a + [i])


ans = float('inf')
board = [list(map(int, input().split())) for _ in range(3)]
pick([])
print(ans)

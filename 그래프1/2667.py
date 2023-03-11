def calculate_block(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 0

    if graph[y][x] == 0:
        return 0

    graph[y][x] = 0
    count = 1

    count += calculate_block(y + 1, x)  # 아래로
    count += calculate_block(y - 1, x)  # 위로
    count += calculate_block(y, x + 1)  # 오른쪽으로
    count += calculate_block(y, x - 1)  # 왼쪽으로

    return count


n = int(input())

graph = [list(map(int, list(input()))) for _ in range(n)]
block_count = []

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            block = calculate_block(y, x)
            block_count.append(block)

print(len(block_count))
print('\n'.join(map(str, sorted(block_count))))

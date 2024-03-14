mask_map = {1: [[0], [0, 0, 0, 0]], 2: [[0, 0]], 3: [[0, 0, 1], [1, 0]], 4: [[1, 0, 0], [0, 1]], 5: [[0, 0, 0], [0, 1], [1, 0, 1], [1, 0]],
            6: [[0, 0, 0], [0, 0], [0, 1, 1], [2, 0]], 7: [[0, 0, 0], [0, 2], [1, 1, 0], [0, 0]]}

w, block_number = map(int, input().split())
board = list(map(int, input().split()))


def find_offset(start, size):
    offset = board[start:start + size]
    minimum = min(offset)
    offset = [i - minimum for i in offset]
    return offset


ans = 0

for mask in mask_map[block_number]:
    for i in range(w - len(mask) + 1):
        offset = find_offset(i, len(mask))
        if offset == mask:
            ans += 1

print(ans)

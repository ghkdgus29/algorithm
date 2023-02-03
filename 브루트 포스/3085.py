def find_longest():
    longest = 1
    for y in range(n):
        cnt = 1
        for x in range(1, n):               # 가장 긴 가로열 찾기
            if b[y][x] == b[y][x - 1]:
                cnt += 1
            else:
                cnt = 1
            longest = max(longest, cnt)

    for x in range(n):
        cnt = 1
        for y in range(1, n):               # 가장 긴 세로열 찾기
            if b[y][x] == b[y - 1][x]:
                cnt += 1
            else:
                cnt = 1
            longest = max(longest, cnt)

    return longest


n = int(input())
b = [list(input()) for _ in range(n)]
longest = find_longest()

for y in range(n):
    for x in range(n - 1):                  # 오른쪽과 교환
        b[y][x], b[y][x + 1] = b[y][x + 1], b[y][x]
        longest = max(longest, find_longest())
        b[y][x], b[y][x + 1] = b[y][x + 1], b[y][x]

for y in range(n - 1):
    for x in range(n):                      # 아래쪽과 교환
        b[y][x], b[y + 1][x] = b[y + 1][x], b[y][x]
        longest = max(longest, find_longest())
        b[y][x], b[y + 1][x] = b[y + 1][x], b[y][x]

print(longest)

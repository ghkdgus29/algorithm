def divide(sx, sy, r):
    if r < 1:
        return

    start = numbers[sy][sx]
    for y in range(sy, sy + r):
        for x in range(sx, sx + r):
            if start != numbers[y][x]:
                for i in range(3):
                    for j in range(3):
                        divide(sx + i * r // 3, sy + j * r // 3, r // 3)
                return

    ans[start + 1] += 1


n = int(input())

numbers = [list(map(int, input().split())) for _ in range(n)]

ans = [0, 0, 0]

divide(0, 0, n)
print(*ans)


# divide(sx, sy, r // 3)
# divide(sx + r // 3, sy, r // 3)
# divide(sx + 2 * r // 3, sy, r // 3)
#
# divide(sx, sy + r // 3, r // 3)
# divide(sx + r // 3, sy + r // 3, r // 3)
# divide(sx + 2 * r // 3, sy + r // 3, r // 3)
#
# divide(sx, sy + 2 * r // 3, r // 3)
# divide(sx + r // 3, sy + 2 * r // 3, r // 3)
# divide(sx + 2 * r // 3, sy + 2 * r // 3, r // 3)

# 를 for 문으로 간소화

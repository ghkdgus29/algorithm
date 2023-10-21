n = int(input())

schedules = [tuple(map(int, input().split())) for _ in range(n)]
schedules.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0
for each in schedules:
    if each[0] >= end:
        cnt += 1
        end = each[1]

print(cnt)

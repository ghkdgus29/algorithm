import sys

# d[i] = max(d[j]) , (j는 i의 선행리스트)

n = int(input())
d = [0] * (n + 1)
for i in range(1, n + 1):
    given = list(map(int, sys.stdin.readline().split()))
    need_time = given[0]

    finish_time = 0
    for j in given[2:]:
        finish_time = max(d[j], finish_time)
    d[i] = finish_time + need_time

print(max(d))

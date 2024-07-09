# 파괴해야하는 장애물의 최솟값, 구간 개수
# 석순 종유석 순으로 입력됨
import sys

w, h = map(int, input().split())
up = [0] * h
down = [0] * h

for i in range(w):
    num = int(sys.stdin.readline()) - 1
    if i % 2 == 0:  # 석순
        up[num] += 1
    else:
        down[num] += 1

for i in range(h - 2, -1, -1):
    up[i] += up[i + 1]
    down[i] += down[i + 1]

cnt = 0
min_val = float('inf')
for i in range(h):
    if up[i] + down[h - i - 1] < min_val:
        cnt = 1
        min_val = up[i] + down[h - i - 1]
    elif up[i] + down[h - i - 1] == min_val:
        cnt += 1

print(min_val, cnt)

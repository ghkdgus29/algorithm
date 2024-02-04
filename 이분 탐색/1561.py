import sys

p, n = map(int, input().split())
a = list(map(int, input().split()))
if p <= n:
    print(p)
    sys.exit(0)

left = 0
right = 2000000000 * 1000000

while left <= right:        # 분(시간)을 이분 탐색한다.
    mid = (left + right) // 2
    begin = 0                   # mid 분에 최초로 탄 사람 순서
    end = n                     # mid 분까지 탄 모든 사람 수
    for i in range(n):
        end += mid // a[i]      # mid 분까지 놀이기구를 탄 사람 수
    begin = end
    for i in range(n):
        if mid % a[i] == 0:
            begin -= 1          # 정확히 mid 분에 놀이기구를 탄 사람 수를 뺀다
    begin += 1

    if p < begin:               # 마지막 사람 순서가 mid 분에 최초로 탄 사람 순서보다 앞선 경우
        right = mid - 1             # 시간을 줄여본다
    elif p > end:               # 마지막 사람 순서가 mid 분까지 탄 사람 수보다 많은 경우
        left = mid + 1              # 시간을 늘려본다
    else:                       # 마지막 사람이 mid 분에 탄 경우 (마지막 사람 순서값이 begin ~ end 사이에 있는 경우)
        for i in range(n):
            if mid % a[i] == 0:
                if p == begin:
                    print(i + 1)        # 배열값이 0부터 시작하니까 1 더해준다.
                    sys.exit(0)
                begin += 1


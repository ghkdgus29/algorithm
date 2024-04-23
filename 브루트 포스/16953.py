# 2를 곱한다 -> 2로 나누어 떨어진다면, 2로 나눈다.
# 1을 추가한다 -> 맨 끝이 1이라면, 1을 뺀다
import sys

a, b = map(int, input().split())
cnt = 1
while b > 0:
    if b == a:
        print(cnt)
        sys.exit(0)

    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        break

    cnt += 1

print(-1)

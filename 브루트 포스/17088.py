import sys

n = int(input())
b = list(map(int, input().split()))

if n == 1:
    print(0)
    sys.exit()

ans = -1
for d1 in range(-1, 1 + 1):
    for d2 in range(-1, 1 + 1):             # 초항과 그 다음항만 결정하면 등차수열인지 판별할 수 있다.
        change = 0
        if d1 != 0:
            change += 1
        if d2 != 0:
            change += 1
        b0 = b[0] + d1                      # 초항 결정
        diff = (b[1] + d2) - b0             # 등차 결정
        ok = True
        bn = b0 + diff                      # n 번째 항 결정
        for i in range(2, n):               # 2번째 항부터 n 번째 항까지 판별
            bn += diff
            if b[i] == bn:
                continue
            if b[i] - 1 == bn:
                change += 1
            elif b[i] + 1 == bn:
                change += 1
            else:
                ok = False                  # 등차 - 1 ~ 등차 + 1 범위를 벗어난 경우
                break

        if ok:
            if ans == -1 or ans > change:
                ans = change

print(ans)

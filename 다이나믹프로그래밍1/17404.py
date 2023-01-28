# 중간부분
# d[n][0] = min(d[n-1][1], d[n-1][2]) + p[0]
# d[n][1] = min(d[n-1][0], d[n-1][2]) + p[1]
# d[n][2] = min(d[n-1][0], d[n-1][1]) + p[2]

n = int(input())
p = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
d = [[0] * 3 for _ in range(1001)]
ans = 1000 * 1000 + 1

for s in range(3):  # 첫번째 집의 색을 설정하기 위한 for문
    for i in range(3):  # 첫번째 집의 색을 고정
        if s == i:
            d[1][i] = p[1][i]
        else:
            d[1][i] = 1000 * 1000 + 1

    for i in range(2, n + 1):  # 직선 형태의 거리라 생각하고 계산
        d[i][0] = min(d[i - 1][1], d[i - 1][2]) + p[i][0]
        d[i][1] = min(d[i - 1][0], d[i - 1][2]) + p[i][1]
        d[i][2] = min(d[i - 1][0], d[i - 1][1]) + p[i][2]

    for i in range(3):
        if s != i:                      # 첫번째 집과 마지막 집의 색이 다른 경우에 대해서만 최소비용 갱신
            ans = min(ans, d[n][i])

print(ans)

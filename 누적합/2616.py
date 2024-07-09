# 3대의 소형기관차로 운송할 수 있는 최대 손님 수
# d[i][j] -> i번째 소형기관차 선택, j번째 객차를 고려했을때의 최대 승객 수
# d[i][j] = max( d[i-1][j-cnt] + s[j] - s[j-cnt], d[i][j-1] )

n = int(input())
a = list(map(int, input().split()))
cnt = int(input())

s = [0]
for val in a:
    s.append(s[-1] + val)

d = [[0] * (n + 1) for _ in range(3)]
d[0][0] = 0
for i in range(cnt, n + 1):
    d[0][i] = max(d[0][i - 1], s[i] - s[i - cnt])

for i in range(1, 3):
    for j in range(cnt, n + 1):
        d[i][j] = max(d[i - 1][j - cnt] + s[j] - s[j - cnt], d[i][j - 1])


print(d[2][-1])

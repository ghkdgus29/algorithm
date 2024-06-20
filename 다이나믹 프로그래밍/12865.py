# 배낭에 넣을 수 있는 물건들 가치의 최댓값

# d[i][j] -> i번째 물건까지 확인했고, 배낭에 넣은 물건 무게의 합이 j일때 가치의 최대값

# d[i][j] = d[i-1][j], i번째 물건을 배낭에 넣지 않은 경우
#         = d[i-1][j-w[i]] + v[i], i번째 물건을 배낭에 넣은 경우

thing_cnt, limit = map(int, input().split())
values = []
weight = []
d = [[0] * (limit+1) for _ in range(thing_cnt)]
for _ in range(thing_cnt):
    w, v = map(int, input().split())
    weight.append(w)
    values.append(v)

for i in range(weight[0], limit+1):
    d[0][i] = values[0]

for i in range(1, thing_cnt):
    for j in range(limit + 1):
        d[i][j] = d[i-1][j]
        if j - weight[i] >= 0:
            d[i][j] = max(d[i][j], d[i - 1][j - weight[i]] + values[i])

print(d[-1][-1])

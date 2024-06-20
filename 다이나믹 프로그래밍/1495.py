# 마지막 곡 볼륨 최대값 구하기

# d[i][j] -> i번째 곡의 볼륨 j
# d[i][j] = d[i-1][j-v[i]] or d[i-1][j+v[i]]


song_cnt, start, limit = map(int, input().split())
v = list(map(int, input().split()))
d = [[False] * (limit + 1) for _ in range(song_cnt)]

if start - v[0] >= 0:
    d[0][start - v[0]] = True
if start + v[0] <= limit:
    d[0][start + v[0]] = True

for i in range(1, song_cnt):
    for j in range(limit + 1):
        if j - v[i] >= 0:
            d[i][j] = d[i - 1][j - v[i]]
        if j + v[i] <= limit:
            d[i][j] = d[i][j] or d[i - 1][j + v[i]]

ans = -1
for idx, val in enumerate(d[-1]):
    if val:
        ans = idx
print(ans)

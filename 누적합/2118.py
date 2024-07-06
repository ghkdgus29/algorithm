# .  1  .   2    .  3   .  4  .  5
#
#
#
# 0 1 3 6 10   15   16 18 21 25
#
#
# 0 과 1 사이의 거리 a[0]
# 0과 2 사이의 거리 a[0] + a[1] = s[2]
#
# 2 와 4 사이의 거리 -> s[4] - s[2] , 반대는 s[7] - s[4] (7과 4 사이의 거리)

n = int(input())
a = [int(input()) for _ in range(n)]

s = [0]
for val in a:
    s.append(s[-1] + val)

for val in a[:-1]:
    s.append(s[-1] + val)

ans = -1
for i in range(n-1):
    for j in range(i, n):
        dist = min(s[j] - s[i], s[i+n] - s[j])
        ans = max(ans, dist)

print(ans)

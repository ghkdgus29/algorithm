n = int(input())
a = [0] + list(map(int, input().split()))
d = [-1001] * (n + 1)
dr = d[:]

d[1] = a[1]
for i in range(2, n + 1):  # 앞에서 부터 최대 연속합을 구한다.
    d[i] = a[i]

    if d[i] < d[i - 1] + a[i]:
        d[i] = d[i - 1] + a[i]


dr[n] = a[n]
for i in range(n - 1, 0, -1):  # 뒤에서 부터 최대 연속합을 구한다.
    dr[i] = a[i]

    if dr[i] < dr[i + 1] + a[i]:
        dr[i] = dr[i + 1] + a[i]


ans = max(d)  # 하나도 빼지 않은 경우의 최대 연속합을 구한다.


for i in range(2, n):                   # 하나를 뺀 경우의 최대 연속합을 구한다.
    if ans < d[i - 1] + dr[i + 1]:
        ans = d[i - 1] + dr[i + 1]          # i 번째 수를 뺀 최대 연속합을 의미한다.


print(ans)

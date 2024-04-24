n, m = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * n
s[0] = a[0]
for i in range(1, n):
    s[i] = a[i] + s[i - 1]
s = [0] + s
left = right = 0
cnt = 0
while left <= n and right <= n:
    if s[right] - s[left] >= m:         # 구간합이 타겟보다 크거나
        if s[right] - s[left] == m:     # 같으면
            cnt += 1
        left += 1
    else:                               # 구간합이 타겟보다 작으면
        right += 1

print(cnt)

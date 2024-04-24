a = [True] * 400_0000
a[0] = False
a[1] = False
for i in range(2, len(a)):
    if a[i]:
        for j in range(i + i, len(a), i):
            a[j] = False

s = [0]

for idx, is_prime, in enumerate(a):
    if is_prime:
        s.append(s[-1] + idx)

n = int(input())
cnt = 0
left = right = 0
while left < len(s) and right < len(s):
    if s[right] - s[left] >= n:  # 구간합이 타겟보다 크거나
        if s[right] - s[left] == n:  # 같으면
            cnt += 1
        left += 1
    else:                           # 구간합이 타겟보다 작으면
        right += 1

print(cnt)

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * n

s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]
s = [0] + s

left = right = 0
length = float('inf')
while left <= n and right <= n:
    if s[right] - s[left] >= m:
        left += 1
        if left == 0:
            l = right
        else:
            l = right - left + 1
        length = min(length, l)
    else:
        right += 1

print(length if length != float('inf') else 0)

n, target = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for val in a:
    s.append(s[-1] + val)

ans = float('inf')
left = 0
right = 0
while right < len(s):
    if s[right] - s[left] < target:
        right += 1
    else:
        ans = min(ans, right - left)
        left += 1

print(ans if ans != float('inf') else 0)

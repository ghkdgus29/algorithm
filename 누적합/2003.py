n, target = map(int, input().split())
a = list(map(int ,input().split()))
s = [0]
for val in a:
    s.append(s[-1] + val)

ans = 0
left = 0
right = 0
while right < len(s):
    if s[right] - s[left] < target:
        right += 1
    else:
        if s[right] - s[left] == target:
            ans += 1
        left += 1

print(ans)

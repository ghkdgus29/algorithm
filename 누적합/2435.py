n, k = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for val in a:
    s.append(s[-1] + val)

ans = -float('inf')
for i in range(n - k + 1):
    ans = max(ans, s[i + k] - s[i])

print(ans)

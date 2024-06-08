n, m = map(int, input().split())
s = set([input() for _ in range(n)])
ans = 0
for _ in range(m):
    if input() in s:
        ans += 1
print(ans)
